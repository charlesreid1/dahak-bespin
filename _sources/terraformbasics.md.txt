# Terraform Basics

This covers the basics of terraform,
which is the tool we will use to 
automate the deployment of infrastructure
to run dahak workflows.

## Installing Terraform

[terraform binary - link](https://www.terraform.io/downloads.html)

On a Mac:

```
brew install terraform
```

## How Terraform Works 

terraform is independent of the particular cloud platform,
but in this example we'll show how to use AWS.

### Configure terraform

We define infrastructure with a config file, 
with file extension `.tf`:

`example.tf`

If we leave out the AWS access and secret key, 
terraform will look in `~/.aws/credentials`
of the machine running terraform
(the one launching jobs).

This requires setup beforehand
(with boto or aws-cli).

**`example.tf:`**

```
provider "aws" {
  region     = "us-west-1a"
}

resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

### Initializing terraform

Start by initializing terraform 
and preparing it to run in your
current directory:

```
$ terraform init
```

### Requesting resources

Now, request the resources that are 
specified in the `.tf` file
(there should only be ONE `.tf` file):

```
$ terraform apply
```

This will examine the resources 
inside the `.tf` file and compare to
the current resources deployed,
and will create a plan for what needs
to be implemented or changed.

If the execution plan is successfully created,
terraform will print it and await confirmation.

Type `yes` to proceed.

### Inspect resources

Insepct the current state of 
the assets with:

```
$ terraform show
```

### Updating resources

If you want to update the infrastructure 
that terraform is deploying and managing,
you can just update the `.tf` file,
and run the apply command:

```
$ terraform apply
```

As mentioned, terraform will examine
the currently deployed resources and 
compare them to the resources listed 
in the terraform file, and come up with
an execution plan.

### Destroying resources

Once you are ready to get rid of the resources, 
use the destroy command:

```
$ terraform destroy
```

## Using Variables in Terraform

### Input Variables 

You can define input variables in a file `variables.tf`
and use them to set up infrastructure.

**`variables.tf`:**

```
variable "region" {
  default = "us-west-1"
}
```

Now you can use this variable by 
inserting the expression `${var.region}`:

```
provider "aws" {
  region     = "${var.region}"
}
```

This can also be set on the command line:

```
$ terraform apply \
  -var 'region=us-east-1'
```

If you name the varfile something other than `.tf`,
use the `-var-file` command line argument:

```
$ terraform apply \
  -var-file="production.tfvars"
```

### Output Variables 

Output variables are defined in
terraform `.tf` files using `output`:

```
output "ip" {
  value = "${aws_instance.example.public_ip}"
}
```

To see the value, check the output of `terraform apply`
or run:

```
$ terraform output ip
```


