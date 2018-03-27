# bespin 

bespin is a repository with 
scripts for allocating cloud resources
for automated testing of dahak workflows.

See [charlesreid1.github.io/dahak-bespin](https://charlesreid1.github.io/dahak-bespin).

Inspiration: [terraform-aws-consul](https://github.com/hashicorp/terraform-aws-consul)

Terraform module organization:

* root: This folder shows an example of Terraform code that uses the consul-cluster module to deploy a Consul cluster in AWS.
* modules: This folder contains the reusable code for this Module, broken down into one or more modules.
* examples: This folder contains examples of how to use the modules.
* test: Automated tests for the modules and examples.

