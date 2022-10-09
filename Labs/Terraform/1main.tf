#terraform ec2 instance
#resource: where and how you want to complete your code : registry.terraform.io
#find your desired os/environment and copy into terminal

#Set your Provider section below # Configure the AWS Provider

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0" #this is a version constraint
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

#create VPC
resource "aws_vpc" "jgree_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "jgree_vpc"
  }
}

#Now let's create our Public Subnets
resource "aws_subnet" "jgree_public_1" {
  vpc_id                  = aws_vpc.jgree_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
 
}

resource "aws_subnet" "jgree_public_2" {
  vpc_id                  = aws_vpc.jgree_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
 
}

#Create your private subnets

resource "aws_subnet" "jgree_private_1" {
  vpc_id                  = aws_vpc.jgree_vpc.id
  cidr_block              = "10.0.3.0/24"
  availability_zone       = "us-east-1a"

}


resource "aws_subnet" "jgree_private_2" {
  vpc_id                  = aws_vpc.jgree_vpc.id
  cidr_block              = "10.0.4.0/24"
  availability_zone       = "us-east-1b"

}

#Insert Public Route table below
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.jgree_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
    tags = {
    Name = "public_rt"
  }
}

#internet gateway code below
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.jgree_vpc.id
  tags = {
    Name = "igw"
  }
}

#security groups for Public VPC : Web Layer Tier 1

resource "aws_security_group" "tf_public_sg" {
#arguments
  name = "tf_public_sg"
  vpc_id      = aws_vpc.jgree_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      =  ["0.0.0.0/16"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
   
  }

  tags = {
    Name = "tf_public_sg"
  }
}

#Create Security group for the ALB

resource "aws_security_group" "alb_sg" {
  name        = "alb_sg"
  description = "security group for the application load balancer"
  vpc_id      = aws_vpc.jgree_vpc.id
  
  ingress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }


  tags = {
    Name = "alb_sg"
  }
}


#Edit route table subnet association
resource "aws_route_table_association" "pub1" {
  subnet_id      = aws_subnet.jgree_public_1.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "pub2" {
  subnet_id      = aws_subnet.jgree_public_2.id
  route_table_id = aws_route_table.public_rt.id
}


#in the search bar on the registry search ec2 instance resource block

resource "aws_instance" "webserver_ec" {
  ami           = "ami-026b57f3c383c2eec"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.tf_public_sg.id]
  user_data = file("build_apache.sh")
  subnet_id = aws_subnet.jgree_public_1.id
  tags = {
    Name = "HelloWorld"
  }
}

#Second EC2 instance 
resource "aws_instance" "webserver_ec2" {
  ami           = "ami-026b57f3c383c2eec"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.tf_public_sg.id]
  user_data = file("build_apache.sh")
  subnet_id = aws_subnet.jgree_public_2.id
  tags = {
    Name = "HelloWorld"
  }
}

#Create ALB
# tier 2
resource "aws_lb" "jgree-alb" {
  name               = "jgree-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.tf_public_sg.id]
  subnets            = [aws_subnet.jgree_public_1.id, aws_subnet.jgree_public_2.id]
  tags = { 
  Environment = "jgree_env"
  }
}

resource "aws_lb_target_group" "lbtarget" {
  name     = "lbtarget"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.jgree_vpc.id
}

# Create ALB listener for web access
resource "aws_lb_listener" "jgree-alb" {
  load_balancer_arn = aws_lb.jgree-alb.arn
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn =  aws_lb_target_group.lb_target.arn
  }
}

#Create Target group (https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_target_group)
resource "aws_lb_target_group" "lb_target" {
  name       = "target"
  depends_on = [aws_vpc.jgree_vpc]
  port       = "80"
  protocol   = "HTTP"
  vpc_id     = aws_vpc.jgree_vpc.id
  health_check {
    interval            = 70
    path                = "/var/www/html/index.html"
    port                = 80
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 60
    protocol            = "HTTP"
    matcher             = "200,202"
  }
}
resource "aws_lb_target_group_attachment" "acquire_targets_mki" {
  target_group_arn = aws_lb_target_group.lb_target.arn
  target_id        = aws_instance.webserver_ec.id
  port             = 80
}
resource "aws_lb_target_group_attachment" "acquire_targets_mkii" {
  target_group_arn = aws_lb_target_group.lb_target.arn
  target_id        = aws_instance.webserver_ec2.id
  port             = 80
}
#Create RDS MySqL Database
# attach Private Subnets we created earlier to your RDS
resource "aws_db_subnet_group" "rdb_subnet" {
  name       = "rdb_subnet"
  subnet_ids = [aws_subnet.jgree_private_1.id, aws_subnet.jgree_private_2.id]
  
}

resource "aws_security_group" "db_sg" {
  name        = "db_sg"
  description = "allow traffic only from web tier"
  vpc_id      = aws_vpc.jgree_vpc.id

   ingress {
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.tf_public_sg.id]
    cidr_blocks     = ["0.0.0.0/0"]
  }

  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.tf_public_sg.id]
    cidr_blocks     = ["10.0.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
#Complete tier 3
# Database instance in private subnet 1
resource "aws_db_instance" "db1" {
  allocated_storage           = 5
  storage_type                = "gp2"
  engine                      = "mysql"
  engine_version              = "5.7"
  instance_class              = "db.t2.micro"
  db_subnet_group_name        = "rdb_subnet"
  vpc_security_group_ids      = [aws_security_group.db_sg.id]
  parameter_group_name        = "default.mysql5.7"
  db_name                     = "jgree-db"
  username                    = "admin"
  password                    = "password"
  allow_major_version_upgrade = true
  auto_minor_version_upgrade  = true
  backup_retention_period     = 35
  backup_window               = "22:00-23:00"
  maintenance_window          = "Sat:00:00-Sat:03:00"
  multi_az                    = false
  skip_final_snapshot         = true
}
