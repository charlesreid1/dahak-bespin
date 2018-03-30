# TODO:
# - vpc?
#
# Note:
# - it is the source directive that links the module code with the module block
# 
# ============================
# Dahak Workflows Cluster
# ============================
#
# Deploy a VPC and a single cluster
# consisting of a single spy node
# (monitoring and benchmarking)
# and a variable number of yeti 
# nodes (worker nodes).

provider "aws" {
  region = "${var.aws_region}"
}

# seehttps://github.com/hashicorp/terraform/issues/14399
terraform {
  required_version = ">= 0.9.3, != 0.9.5"
}

# ============================
# Allocate Spy Node
# ============================
# Spy node is a simple micro instance.

module "spy_server" {
  # When using these modules in your own templates, you will need to use a Git URL with a ref attribute that pins you
  # to a specific version of the modules, such as the following example:
  #source = "git::git@github.com:hashicorp/terraform-aws-consul.git/modules/consul-cluster?ref=v0.0.1"
  source = "./module"

  cluster_name  = "${var.cluster_name}-spy"
  cluster_size  = "1"
  instance_type = "${var.spy_instance_type}"
  spot_price    = "${var.spot_price}"

  ### # The EC2 Instances will use these tags to automatically discover each other and form a cluster
  ### cluster_tag_key   = "${var.cluster_tag_key}"
  ### cluster_tag_value = "${var.cluster_name}"

  ami_id    = "${var.ami_id}"
  user_data = "${data.template_file.spy_user_data.rendered}"

  vpc_id     = "${data.aws_vpc.dahakvpc.id}"
  subnet_ids = "${data.aws_subnet_ids.default.ids}"

  # To make testing easier, we allow Consul and SSH requests from any IP address here but in a production
  # deployment, we strongly recommend you limit this to the IP address ranges of known, trusted servers inside your VPC.
  allowed_ssh_cidr_blocks = ["0.0.0.0/0"]

  allowed_inbound_cidr_blocks = ["0.0.0.0/0"]
  ssh_key_name                = "${var.ssh_key_name}"

  tags = [
    {
      key                 = "Environment"
      value               = "development"
      propagate_at_launch = true
    },
  ]
}

# ============================
# Deploy Spy Node
# ============================
# Actually deploy the infrastructure
# (apt-get scripts, Python, docker, 
# containers, etc.) to spy.

data "template_file" "spy_user_data" {
  template = "${file("${path.module}/dahak-spy/cloud_init/cloud_init.sh")}"

  ### vars {
  ###   cluster_tag_key   = "${var.cluster_tag_key}"
  ###   cluster_tag_value = "${var.cluster_name}"
  ### }
}


# ============================
# Allocate Yeti Node
# ============================
# Yeti node is a beefy node.

module "yeti_server" {
  # When using these modules in your own templates, you will need to use a Git URL with a ref attribute that pins you
  # to a specific version of the modules, such as the following example:
  #source = "git::git@github.com:hashicorp/terraform-aws-consul.git/modules/consul-cluster?ref=v0.0.1"
  source = "./module"

  cluster_name  = "${var.cluster_name}-server"
  cluster_size  = "${var.num_yeti_servers}"
  instance_type = "${var.yeti_instance_type}"
  spot_price    = "${var.spot_price}"

  ### # The EC2 Instances will use these tags to automatically discover each other and form a cluster
  ### cluster_tag_key   = "${var.cluster_tag_key}"
  ### cluster_tag_value = "${var.cluster_name}"

  ami_id    = "${var.ami_id}"
  user_data = "${data.template_file.yeti_user_data.rendered}"

  vpc_id     = "${data.aws_vpc.dahakvpc.id}"
  subnet_ids = "${data.aws_subnet_ids.default.ids}"

  # To make testing easier, we allow Consul and SSH requests from any IP address here but in a production
  # deployment, we strongly recommend you limit this to the IP address ranges of known, trusted servers inside your VPC.
  allowed_ssh_cidr_blocks = ["0.0.0.0/0"]

  allowed_inbound_cidr_blocks = ["0.0.0.0/0"]
  ssh_key_name                = "${var.ssh_key_name}"

  tags = [
    {
      key                 = "Environment"
      value               = "development"
      propagate_at_launch = true
    },
  ]
}

# ============================
# Deploy Yeti Node
# ============================
# Actually deploy the infrastructure
# (apt-get scripts, Python, snakemake, 
# singularity, etc.) to yeti.

data "template_file" "yeti_user_data" {
  template = "${file("${path.module}/dahak-yeti/cloud_init/cloud_init.sh")}"

  ### vars {
  ###   cluster_tag_key   = "${var.cluster_tag_key}"
  ###   cluster_tag_value = "${var.cluster_name}"
  ### }
}

# ============================
# Deploy VPC
# ============================
# Assemble the VPC, subnet,
# internet gateway, DNS, DHCP,

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
  route_table_id         = "${aws_vpc.dahakvpc.main_route_table_id}"
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
# and routing table.
resource "aws_route_table_association" "dahaksubnet_association" {
    subnet_id = "${aws_subnet.dahaksubnet.id}"
    route_table_id = "${aws_vpc.dahakvpc.main_route_table_id}"
}

