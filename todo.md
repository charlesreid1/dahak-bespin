# todo list

vpc subcommand:
- [x] build
- [ ] info
- [ ] destroy
    - will require expanding stash files
    - check that there is no yeti node
    - check that there is no spy node
    - check that there is no security group
    - delete subnet
    - delete routing table
    - delete internet gateway
    - delete dhcp
    - delete network interface
- [x] stash

security subcommand:
- [ ] build
- [ ] destroy
- [ ] port add
- [ ] port rm
- [ ] ip add
- [ ] ip rm
- [ ] info
- [ ] stash

spy subcommand:
- [ ] spy build
    - like vpc - check if dotfile exists
- [ ] spy destroy
- [ ] spy info
- [ ] spy stash

yeti subcommand:
- [ ] yeti build
    - global label counter 
    - yeti1, yeti2, yeti3, etc.
- [ ] yeti destroy
    - grep nodes with yeti in label
- [ ] yeti info
- [ ] yeti stash


