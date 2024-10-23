# Testing of Intrusion Detection Systems

This repository contains files used for testing Intrusion Detection Systems (IDS). The pipeline used for the test is triggered upon push commands to the worker branches which contains a specific CI file. Once a pipeline has been started, it will first fetch and make sure it has all relevant code from both the master branch and the worker branch which triggered the pipeline. Then it will create two docker containers, one which will contain and host the IDS in question and the other will replay and send all network traffic. The output of the docker container logs will then be cleaned in order to fit the JSON format, and will then be tested by comparing it to expected output.

## Creating a worker branch for testing

### Prerequisites

This section assumes that you have the necessary permissions in this repository to create new branches and copy the contents of others.

### Create your worker branch

First, you will have to create your own branch and copy the files in the gruppeX branch. This can either easily be done by cpoying the gruppeX branch using the Gitlab UI in the root of the repository, or by executing the following commands in your terminal:

```bash
git clone https://gitlab.internal.uia.no/bachelor/bachelor-testing.git
cd bachelor/bachelor-testing.git
git checkout -b <new_branch_name> gruppeX
git push origin <new_branch_name>
```

## How to choose what Pytest file to use

In order to edit what pytest file the testing environment should use, so does one simply have to edit the testing stage in the CI file. There, if one can choose what pytest file to use by changing the corresponding name in the following command:

```bash
- pytest -v <name_of_pytest_file> --color=yes
```

## How to change the network traffic being replayed

In the test network traffic will be replayed and sent accross the docker containers. This network traffic can be altered simply by either exchanging the PCAP file allready in use with a new one. Or by adding a new PCAP file in the sender/ folder containing new captured network traffic, and then changing what PCAP file is used in sender/test.py:
```bash
# Read packets from the PCAP file
packets = rdpcap("<name_of_pcap_file>")
```

## Reviewing the results from a test

The results from a test can be reviewed here in Gitlab by accessing the pipeline section and reviewing the corresponding logs from the specific pipeline.

