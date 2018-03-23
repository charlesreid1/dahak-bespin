# bespin: via terraform

## install

[link](https://www.terraform.io/downloads.html)

mac:

```
brew install terraform
```

## how it works

terraform is cloud platform independent.

define infrastructure with a config file.

`example.tf`

We will leave out the AWS access and secret key, 
and terraform will look in `~/.aws/credentials`
of the machine running terraform
(the one launching jobs).

Requires setup beforehand.

```
provider "aws" {
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

Start by initializing terraform:

```
$ terraform init
```

Now request the resources specified:

```
$ terraform apply
```

This will display a lot of information
about the resources requested - the 
execution plan.

If the plan is successfully created,
terraform will wait for input.
Type yes to proceed.

Insepct current state with

```
$ terraform show
```

