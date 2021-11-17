---
lab:
    title: 'Create an Azure Machine Learning workspace'
---

# Create and Explore an Azure Machine Learning Workspace

In this exercise, you will create and explore an Azure Machine Learning workspace.

## Create an Azure Machine Learning workspace

As its name suggests, a workspace is a centralized place to manage all of the Azure ML assets you need to work on a machine learning project.

1. In the [Azure portal](https://portal.azure.com), create a new **Machine Learning** resource, specifying the following settings:

    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Create or select a resource group*
    - **Workspace name**: *Enter a unique name for your workspace*
    - **Region**: *Select the geographical region closest to you*
    - **Storage account**: *Note the default new storage account that will be created for your workspace*
    - **Key vault**: *Note the default new key vault that will be created for your workspace*
    - **Application insights**: *Note the default new application insights resource that will be created for your workspace*
    - **Container registry**: None (*one will be created automatically the first time you deploy a model to a container*)

    > **Note**: When you create an Azure Machine Learning workspace, you can use some advanced options to restrict access through a *private endpoint* and specify custom keys for data encryption. We won't use these options in this exercise - but you should be aware of them!
2. When the workspace and its associated resources have been created, view the workspace in the portal.

## Explore Azure Machine Learning studio

You can manage some workspace assets in the Azure portal, but for data scientists, this tool contains lots of irrelevant information and links that relate to managing general Azure resources. *Azure Machine Learning studio* provides a dedicated web portal for working with your workspace.

1. In the Azure portal blade for your Azure Machine Learning workspace, click the link to launch studio; or alternatively, in a new browser tab, open [https://ml.azure.com](https://ml.azure.com). If prompted, sign in using the Microsoft account you used in the previous task and select your Azure subscription and workspace.

    > **Tip** If you have multiple Azure subscriptions, you need to choose the Azure *directory* in which the subscription is defined; then choose the subscription, and finally choose the workspace.
2. View the Azure Machine Learning studio interface for your workspace - you can manage all of the assets in your workspace from here.
3. In Azure Machine Learning studio, toggle the &#9776; icon at the top left to show and hide the various pages in the interface. You can use these pages to manage the resources in your workspace.

## Create compute assets

One of the benefits of Azure Machine Learning is the ability to create cloud-based compute on which you can run experiments and training scripts at scale.

1. In Azure Machine Learning studio, view the **Compute** page. This is where you'll manage compute resources for your data science activities. There are four kinds of compute resource you can create:
    - **Compute instances**: Development workstations that data scientists can use to work with data and models.
    - **Compute clusters**: Scalable clusters of virtual machines for on-demand processing of experiment code.
    - **Inference clusters**: Deployment targets for predictive services that use your trained models.
    - **Attached compute**: Links to other Azure compute resources, such as Virtual Machines or Azure Databricks clusters.

    For this exercise, you'll create a compute instance so you can run some code on CPUs, and a compute cluster so you can run code on GPUs.

### Create a compute instance

2. On the **Compute instances** tab, add a new compute instance with the following settings. You'll use this as a workstation to run code in notebooks.
    - **Compute name**: *enter a unique name*
    - **Location**: *The same location as your workspace*
    - **Virtual machine type**: CPU
    - **Virtual machine size**: Standard_DS11_v2
    - **Total Available Quotas**: This shows dedicated cores available.
    - **Show advanced settings**: Note the following settings, but do not select them: 
        - **Enable SSH access**: Unselected *(you can use this to enable direct access to the virtual machine using an SSH client)*
        - **Enable virtual network**: Unselected *(you would typically use this in an enterprise environment to enhance network security)*
        - **Assign to another user**: Unselected *(you can use this to assign a compute instance to a data scientist)*

### Create a compute cluster

3. On the **Compute clusters** tab, add a new compute cluster with the following settings. You'll use this to execute code that needs GPUs.
    - **Location**: *The same location as your workspace*
    - **Virtual machine priority**: Low priority
    - **Virtual machine type**: GPU
    - **Virtual machine size**: Standard_NC6S_V3 (you may have to choose **Select from all options** to expand the list of sizes)
    - Select **Next**.
    - **Compute name**: *enter a unique name*
    - **Minimum number of nodes**: Leave at default 0.
    - **Maximum number of nodes**: Select 2 nodes.
    - Select **Create.

> **Important:** To run the exercises, you need to use a NCv3 series compute which features NVIDIA's Tesla V100 GPU.

## Create an environment

1. In Azure Machine Learning studio, view the **Environments** page.
2. In the **Custom environments** tab, create a new environment with the following settings:
    - **Name**: rapids-mlflow
    - **Description**: *Optional*
    - **Choose environment type**: Dockerfile
    - **Dockerfile**: Copy and paste the code below:

        ```
        FROM rapidsai/rapidsai-dev:0.18-cuda10.2-devel-ubuntu18.04-py3.7
        RUN apt-get update && \
        apt-get install -y fuse && \
        source activate rapids && \
        pip install azureml-mlflow && \
        pip install azureml-dataprep
        ```
3. After reviewing and creating the environment, Azure Machine Learning will automatically build the environment. You can view its progress in the **Details** tab of the environment.

## Clone the repo

1. In Azure Machine Learning Studio, open the **Notebooks** page.
2. Select **Terminal** or the **Open terminal** icon to open a terminal. Check that the **Compute** is set to your compute instance and that the current path is the **/users/your-user-name** folder.
3. Enter the following command to clone a Git repository containing notebooks, data, and other files to your workspace:
4. Enter the following command to clone a Git repository containing notebooks, data, and other files to your workspace:

    ```bash
    git clone https://github.com/MicrosoftLearning/mslearn-deep-learning mslearn-deep-learning
    ```

4. When the command has completed, in the **My files** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/mslearn-deep-learning** folder has been created.
5. Close the terminal pane, terminating the session.

> **Tip**: The instructions for the exercises are in the **Instructions** folder. The necessary notebooks, scripts, and artifacts are in the **Allfiles** folder.

## Stop your compute instance when done with the exercises

If you've finished exploring Azure Machine Learning for now, you should shut down your compute instance to avoid incurring unnecessary charges in your Azure subscription. The compute cluster automatically scales down to 0 nodes when idle.

1. In Azure Machine Learning studio, on the **Compute** page, select your compute instance.
2. Click **Stop** to stop your compute instance. When it has shut down, its status will change to **Stopped**.

> **Note**: Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat this lab to create the workspace and prepare the environment first.
