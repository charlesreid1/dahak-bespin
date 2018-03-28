# dahak cluster

(work in progress)

This folder contains a [Terraform module](https://www.terraform.io/docs/modules/usage.html)
to deploy a dahak cluster consisting of a VPC, a spy monitoring node, and one or more yeti worker nodes.

## using this module

This folder defines a Terraform module, which you can use in your
code by adding a `module` configuration and setting its `source` parameter 
to URL of this folder:

```hcl
module "dahak_cluster" {
  # TODO: update this 
  source = "github.com/hashicorp/terraform-aws-consul//modules/consul-cluster?ref=v0.0.5"

  # TODO: update this
  # amazon image ID
  ami_id = "ami-abcd1234"

  # Configure and start the nodes
  user_data = <<-EOF
              #!/bin/bash
              /opt/consul/bin/run-consul --server --cluster-tag-key consul-cluster
              EOF

  # ... See variables.tf for the other parameters you must define for the consul-cluster module
}
```

Note the following parameters:

* `source`: Use this parameter to specify the URL of the terraform module we are using.
  The double slash (`//`) is intentional and required. Terraform uses it to specify subfolders within a Git repo.
  The `ref` parameter specifies a specific Git tag in this repo. It enures you are using a fixed version of the repo.

* `ami_id`: Use this parameter to specify the amazon machine image to install on the nodes on the cluster.

* `user_data`: Use this parameter to specify user data (cloud init scripts).

You can find the other parameters in [variables.tf](variables.tf).

Check out the [consul-cluster example](https://github.com/hashicorp/terraform-aws-consul/tree/master/MAIN.md) for fully-working sample code.

