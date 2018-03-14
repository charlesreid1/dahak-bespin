# dahak-boto

This repo contains scripts that use boto3, the Python API 
provided by AWS, to request AWS resources for running 
dahak workflows.

```
               __                        __          
  ____ ___  __/ /_____  ____ ___  ____ _/ /____      
 / __ `/ / / / __/ __ \/ __ `__ \/ __ `/ __/ _ \     
/ /_/ / /_/ / /_/ /_/ / / / / / / /_/ / /_/  __/     
\__,_/\__,_/\__/\____/_/ /_/ /_/\__,_/\__/\___/      
         ____   __  __                               
  ____ _/ / /  / /_/ /_  ___                         
 / __ `/ / /  / __/ __ \/ _ \                        
/ /_/ / / /  / /_/ / / /  __/                        
\__,_/_/_/   \__/_/ /_/\___/                         
   __  __    _                                       
  / /_/ /_  (_)___  ____ ______                      
 / __/ __ \/ / __ \/ __ `/ ___/                      
/ /_/ / / / / / / / /_/ (__  )                       
\__/_/ /_/_/_/ /_/\__, /____/                        
                 /____/                              
```

## What is it? 

The intention behind dahak-boto is to provide a push-button
solution to running workflows. Automating the workflows and
removing the user and SSH from the process of runinng workflows
makes it possible to automate testing and allows analysts to
focus on work that matters - high-level monitoring and parameter
studies - instead of low-level details like maintaining a spreadsheet
of which instances are running which cases. 

## How boto3 works

To interface with the AWS API, you use the boto library.
The boto library provides various objects and methods.
Many of the methods correspond to a general class of requests,
e.g., you have an object to represent EC2 and methods to 
represent actions like getting a list of all instances,
or getting a network given a VPC ID.

Most of the requests are highly customizable and accept
comlpicated JSON inputs. This can make boto challenging to use.

## What dahak-boto does

dahak-boto is intended to automate dahak workflows,
which can be run using a single subnet architecture.
A virtual private cloud (VPC) network is set up to 
allow AWS nodes to talk to one another.

## Networking Infrastructure

See [Networking.md](/Networking.md) for more about the networking 
details. Short version: one network with one subnet.



