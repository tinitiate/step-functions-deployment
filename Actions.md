# GitHub Actions
- Continuous integration and continuous delivery (CI/CD) is automated through GitHub Actions.
- Along with CI/CD, GitHub Actions allows you to run workflows when other repository events happen. 
  e.g: Adding the labels when new issue is created.

## Components
- GitHub Actions consists of the following components:
  - Workflows
  - Events
  - Jobs
  - Actions
  - Runners

  ![actions](/actions.png)
  
### Workflows
- We can create workflows by defining them in a YAML file, and they will run when triggered by an event in your repository, 
  or at a specified time, or are triggered manually.
- We can have multiple workflows, each of which can perform a different set of tasks. 

### Events
- An event in a repository triggers workflows based on a specific activity.

### Jobs
- Job is a sequence of steps in a workflow.
- All the steps in the job are executed on the same runner.
- We can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel with each other.

### Actions
- Actions are custom GitHub Actions applications that perform frequently repeated tasks.

### Runner
- Workflows are run by runners(server) when they are triggered.
- Each runner can run a single job at a time.
- GitHub provides Ubuntu Linux, Microsoft Windows, and macOS.
