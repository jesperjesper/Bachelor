## Testing your IDS

This is the example branch for students. Create your own branch by copying this example branch, so that your branch contains the CI file used to trigger the test for your IDS. Whenever new files or new changes are pushed or made to this branch, the CI file will react upon a push event and trigger a pipeline in master where the code will be tested

### Prerequisites

This section assumes that you have your own branch, which also contains the files located in the example branch gruppeX.

### 1. Cloning the repository

First, you will have to clone the repository by executing the following commands:

```bash
git clone https://gitlab.internal.uia.no/bachelor/bachelor-testing.git
cd bachelor/bachelor-testing.git
```

### 2. Creating a Dockerfile

You will have to create a Dockerfile which can be used with Docker, in order to test your IDS. This dockerfile must contain all necessary steps needed to take in order to run your IDS in a Docker container.


### 3. Pushing your code to your branch

Once you have a working Dockerfile and is ready to test your IDS, so can you push your code and Dockerfile to gitlab using the following command:

```bash
git add <all_relevant_files>
git commit -m "<your_push_comment>"
git push origin <your_branch_name>
```

Once everything has been pushed to gitlab within your branch, then a test will be triggered and run in the master branch using the code and Dockerfile you pushed.


