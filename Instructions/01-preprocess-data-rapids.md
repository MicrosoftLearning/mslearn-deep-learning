---
lab:
    title: 'Load and preprocess data with RAPIDS'
    module: 'Module: Preprocessing large datasets with Azure Machine Learning'
---

# Load and preprocess data with RAPIDS

To use GPUs to load and preprocess data, data scientists can work with the RAPIDS framework. More specifically, with the cuDF library. In this exercise, you'll use cuDF to preprocess data with a GPU cluster in Azure Machine Learning.

## Before you start

If you have not already done so, complete the *[Set-up](00-set-up.md)* exercise to create an Azure Machine Learning workspace, compute instance, compute cluster, and clone the notebooks required for this exercise.

## Create an environment

1. In Azure Machine Learning studio, view the **Environments** page.
2. In the **Custom environments** tab, create a new environment with the following settings:
    - **Name**: rapids-mlflow
    - **Description**: *Optional*
    - **Choose environment type**: Dockerfile
    - **Dockerfile**: Copy and paste the code below:

        ```
        FROM rapidsai/rapidsai:21.10-cuda11.0-runtime-ubuntu18.04-py3.7
        RUN apt-get update && \
        apt-get install -y fuse && \
        source activate rapids && \
        pip install azureml-mlflow && \
        pip install azureml-dataprep
        ```
3. After reviewing and creating the environment, Azure Machine Learning will automatically build the environment. You can view its progress in the **Details** tab of the environment.

## Open the notebook

Most of the work will be done by our compute cluster which uses GPUs. To get the data and to submit the RAPIDS job, we will use notebooks supported by the compute instance.

1. In [Azure Machine Learning studio](https://ml.azure.com), view the **Compute** page for your workspace; and on the **Compute Instances** tab, start your compute instance if it is not already running.
2. Navigate to the **Notebooks** page in the Studio.
3. Run through all cells of the `01-copy-data.ipynb` notebook to copy the flight data to the default datastore.
4. Run through all cells of the `02-process-data.ipynb` to submit the Python script which loads and preprocesses the flight data with cuDF using the GPU compute cluster.

> **Tip**: To run a code cell, select the cell you want to run and then use the **&#9655;** button to run it.

## Stop your compute instance when done with the exercises

If you've finished exploring Azure Machine Learning for now, you should shut down your compute instance to avoid incurring unnecessary charges in your Azure subscription. The compute cluster automatically scales down to 0 nodes when idle.

1. In Azure Machine Learning studio, on the **Compute** page, select your compute instance.
2. Click **Stop** to stop your compute instance. When it has shut down, its status will change to **Stopped**.

> **Note**: Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat this lab to create the workspace and prepare the environment first.
