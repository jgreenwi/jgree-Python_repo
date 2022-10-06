#terraform ec2 instance
#resource: where and how you want to complete your code : registry.terraform.io
#find your desired os/environment and copy into terminal
#Provider section below
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
#in the search bar on the registry search ec2 instance resource block

resource "aws_instance" "my_server" {
  ami           = "ami-026b57f3c383c2eec"
  instance_type = "t2.micro"
  user_data = file("build_apache.sh")
  tags = {
    Name = "HelloWorld"
  }
}