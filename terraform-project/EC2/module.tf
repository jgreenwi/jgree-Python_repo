# ---module/ ec2.tf ---
module "EC2" {
    source = "./ec2"
    ami = var.ami
    instance_type = var.instance_type
    
}