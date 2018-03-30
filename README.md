# bespin 

bespin is a repository with 
scripts for allocating cloud resources
for automated testing of dahak workflows.

See [charlesreid1.github.io/dahak-bespin](https://charlesreid1.github.io/dahak-bespin).

Inspiration: [terraform-aws-consul](https://github.com/hashicorp/terraform-aws-consul)

Terraform module organization:

* root: This folder shows an example of Terraform code that uses a terraform module to deploy a cluster in AWS.
* module: This folder contains the reusable code for this Module
* examples: This folder contains examples of how to use the module.
* test: Automated tests for the module and examples.

