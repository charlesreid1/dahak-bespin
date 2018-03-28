# ---------------------------------------------------------------------------------------------------------------------
# ENVIRONMENT VARIABLES
# Define these secrets as environment variables
# ---------------------------------------------------------------------------------------------------------------------

# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

# ---------------------------------------------------------------------------------------------------------------------
# OPTIONAL PARAMETERS
# These parameters have reasonable defaults.
# ---------------------------------------------------------------------------------------------------------------------

variable "ami_id" {
  description = "The ID of the AMI to run in the cluster."
  default     = ""
}

variable "aws_region" {
  description = "The AWS region to deploy into (e.g. us-east-1)."
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "What to name the dahak cluster and all of its associated resources"
  default     = "dahak-test-cluster"
}

variable "spy_instance_type" {
  description = "The type of instance to deploy for the spy node."
  default     = "t2.micro"
}

variable "num_yeti_servers" {
  description = "The number of yeti workers to deploy."
  default     = 1
}

variable "yeti_instance_type" {
  description = "The type of instance to deploy for the yeti workers."
  default     = "m5.4xlarge"
}

### variable "cluster_tag_key" {
###   description = "The tag the EC2 Instances will look for to automatically discover each other and form a cluster."
###   default     = "consul-servers"
### }

variable "ssh_key_name" {
  description = "The name of an EC2 Key Pair that can be used to SSH to the EC2 Instances in this cluster. Set to an empty string to not associate a Key Pair."
  default     = ""
}

variable "spot_price" {
  description = "The maximum hourly price to pay for EC2 Spot Instances."
  default     = "0.28"
}
