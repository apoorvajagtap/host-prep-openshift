# host-prep-openshift
This project automates all the time consuming and redundant tasks which are to be done over all the nodes of cluster before starting the openshift installation playbooks.

User needs should have following pip3 packages:
- paramiko
- pyyaml

User should pass a file which contains all the IPs of the nodes, over which host preparation has to be performed.

This code supports 3.x versions of OpenShift.

All the neccessary file; i.e., exec.py, versionFile.yaml and file with ip list should be located in the same folder.
