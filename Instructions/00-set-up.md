---
lab:
    title: 'Set up: Create an Azure Machine Learning workspace'
---

# Create and Explore an Azure Machine Learning Workspace

In this exercise, you will create and explore an Azure Machine Learning workspace.

## Create an Azure Machine Learning workspace

As its name suggests, a workspace is a centralized place to manage all of the Azure ML assets you need to work on a machine learning project.

1. In the [Azure portal](https://portal.azure.com), create a new **Machine Learning** resource, specifying the following settings:

    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Create a new resource group*
    - **Workspace name**: *Enter a unique name for your workspace*
    - **Region**: *Select the region closest to you*
    - **Storage account**: *Use the default*
    - **Key vault**: *Use the default*
    - **Application insights**: *Use the default*
    - **Container registry**: None 

2. When the workspace and its associated resources have been created, view the workspace in the portal.
3. Launch the Azure Machine Learning Studio by selecting the link in the portal, or navigate to [https://ml.azure.com](https://ml.azure.com).

## Create compute assets

To learn how to work with GPUs within Azure Machine Learning, you'll work with a GPU compute cluster. A compute cluster scales down after inactivity and will be more cost-efficient. For control activities that are not very compute demanding, you'll use a CPU compute instance.

1. In Azure Machine Learning studio, open the **Compute** page.  
2. On the **Compute instances** tab, add a new compute instance with the following settings. You'll use this as a workstation to run code in notebooks.
    - **Compute name**: *enter a unique name*
    - **Location**: *The same location as your workspace*
    - **Virtual machine type**: CPU
    - **Virtual machine size**: Standard_DS3_v2

### Create a compute cluster

3. On the **Compute clusters** tab, add a new compute cluster with the following settings. You'll use this to execute code that needs GPUs.
    - **Location**: *The same location as your workspace*
    - **Virtual machine priority**: Low priority
    - **Virtual machine type**: GPU
    - **Virtual machine size**: Standard_NC6S_V3 (you may have to choose **Select from all options** to expand the list of sizes)
    - Select **Next**.
    - **Compute name**: *enter a unique name*
    - **Minimum number of nodes**: Leave at default 0.
    - **Maximum number of nodes**: Select 1 node.
    - Select **Create**.

> **Important:** To run the exercises, you need to use a NCv3 series compute which features NVIDIA's Tesla V100 GPU.

## Clone the repo

1. In Azure Machine Learning Studio, open the **Notebooks** page.
2. Select **Terminal** or the **Open terminal** icon to open a terminal. Check that the **Compute** is set to your compute instance and that the current path is the **/users/your-user-name** folder. You may have to wait until the compute instance is running.
3. Enter the following command to clone a Git repository containing notebooks, data, and other files to your workspace:

    ```bash
    git clone https://github.com/MicrosoftLearning/mslearn-deep-learning mslearn-deep-learning
    ```

4. When the command has completed, in the **Notebooks** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/mslearn-deep-learning** folder has been created.
5. Close the terminal pane, terminating the session.

> **Tip**: The instructions for the exercises are in the **Instructions** folder. The necessary notebooks, scripts, and artifacts are in the **Allfiles** folder.

## Stop your compute instance when done with the exercises

If you've finished exploring Azure Machine Learning for now, you should shut down your compute instance to avoid incurring unnecessary charges in your Azure subscription. The compute cluster automatically scales down to 0 nodes when idle.

1. In Azure Machine Learning studio, on the **Compute** page, select your compute instance.
2. Click **Stop** to stop your compute instance. When it has shut down, its status will change to **Stopped**.

> **Note**: Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat this lab to create the workspace and prepare the environment first.
