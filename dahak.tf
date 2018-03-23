# Set the region
provider "aws" {
  region     = "us-west-1a"
}

# VPC
resource "aws_vpc" "dahakvpc" {
  cidr_block = "10.99.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}

# VPC subnet
resource "aws_subnet" "dahaksubnet" {
  vpc_id     = "${aws_vpc.dahakvpc.id}"
  cidr_block = "10.99.0.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-west-1a"
  tags {
    Name = "namedahaksubnet"
  }
}

# Internet gateway
resource "aws_internet_gateway" "dahakgw" {
  vpc_id = "${aws_vpc.dahakvpc.id}"
  tags {
    Name = "namedahakgw"
  }
}

# Route
resource "aws_route" "internet_access" {
  route_table_id         = "${aws_vpc.vpc_tuto.main_route_table_id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = "${aws_internet_gateway.dahakgw.id}"
}

# Route table
resource "aws_route_table" "private_route_table" {
    vpc_id = "${aws_vpc.dahakvpc.id}"
    tags {
        Name = "Private route table"
    }
}

# Associate route table with subnet
resource "aws_route_table_association" "dahaksubnet_association" {
    subnet_id = "${aws_subnet.dahaksubnet.id}"
    route_table_id = "${aws_vpc.vpc_tuto.main_route_table_id}"
}

# spy
resource "aws_instance" "spy" {
    ami           = "ami-07585467"
    instance_type = "t2.micro"
    provisioner "local-exec" {
        command = "echo ${aws_instance.spy.public_ip} > spy_ip_address.txt"
    }
}

# yeti
resource "aws_instance" "yeti" {
    ami           = "ami-07585467"
    instance_type = "m5.2xlarge"
    provisioner "local-exec" {
        command = "echo ${aws_instance.yeti.public_ip} > yeti_ip_address.txt"
    }
}

