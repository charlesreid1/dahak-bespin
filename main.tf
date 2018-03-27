# TODO:
# - vpc?
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
  source = "git::git@github.com:hashicorp/terraform-aws-consul.git/modules/consul-cluster?ref=v0.0.1"

  cluster_name  = "${var.cluster_name}-server"
  cluster_size  = "${var.num_servers}"
  instance_type = "t2.micro"
  spot_price    = "${var.spot_price}"

  # The EC2 Instances will use these tags to automatically discover each other and form a cluster
  cluster_tag_key   = "${var.cluster_tag_key}"
  cluster_tag_value = "${var.cluster_name}"

  ami_id    = "${var.ami_id}"
  user_data = "${data.template_file.user_data_server.rendered}"

  vpc_id     = "${data.aws_vpc.default.id}"
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

data "template_file" "user_data_server" {
  # FIXME
  template = "${file("${path.module}/examples/root-example/user-data-server.sh")}"

  vars {
    cluster_tag_key   = "${var.cluster_tag_key}"
    cluster_tag_value = "${var.cluster_name}"
  }
}


# ============================
# Allocate Yeti Node
# ============================
# Yeti node is a beefy node.

module "yeti_server" {
  # When using these modules in your own templates, you will need to use a Git URL with a ref attribute that pins you
  # to a specific version of the modules, such as the following example:
  source = "git::git@github.com:hashicorp/terraform-aws-consul.git/modules/consul-cluster?ref=v0.0.1"

  cluster_name  = "${var.cluster_name}-server"
  cluster_size  = "${var.num_servers}"
  instance_type = "m5.4xlarge"
  spot_price    = "${var.spot_price}"

  # The EC2 Instances will use these tags to automatically discover each other and form a cluster
  cluster_tag_key   = "${var.cluster_tag_key}"
  cluster_tag_value = "${var.cluster_name}"

  ami_id    = "${var.ami_id}"
  user_data = "${data.template_file.user_data_server.rendered}"

  vpc_id     = "${data.aws_vpc.default.id}"
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

data "template_file" "user_data_server" {
  # FIXME
  template = "${file("${path.module}/examples/root-example/user-data-server.sh")}"

  vars {
    cluster_tag_key   = "${var.cluster_tag_key}"
    cluster_tag_value = "${var.cluster_name}"
  }
}


