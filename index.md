---
title: Online Hosted Instructions
permalink: index.html
layout: home
---

# Train compute-intensive models with Azure Machine Learning

This repository contains the hands-on lab exercises for the [self-paced modules on Microsoft Learn](add link). The exercises are designed to accompany the learning materials and enable you to practice using the technologies they describe.

These exercises requires an Azure subscription and rights to create a GPU Virtual Machine. If you do not already have an Azure subscription, sign up at [https://azure.microsoft.com](https://azure.microsoft.com). To check the available GPU VMs, you can run the `az vm list-skus` command from the Azure Cloud Shell.

{% assign labs = site.pages | where_exp:"page", "page.url contains '/Instructions'" %}
| Module | Lab |
| --- | --- | 
{% for activity in labs  %}| {{ activity.lab.module }} | [{{ activity.lab.title }}{% if activity.lab.type %} - {{ activity.lab.type }}{% endif %}]({{ site.github.url }}{{ activity.url }}) |
{% endfor %}
