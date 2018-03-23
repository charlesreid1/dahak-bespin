provider "aws" {
  region     = "us-west-1"
}
resource "aws_instance" "example" {
    ami           = "ami-07585467"
    instance_type = "t2.micro"
    provisioner "local-exec" {
        command = "echo ${aws_instance.example.public_ip} > ip_address.txt"
    }
}
