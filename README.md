# Breast-Cancer-Causality
Causal inference is the process of where causes are inferred from data, it refers to an intellectual discipline that considers the assumptions, study designs, and estimation strategies that allow researchers to draw causal conclusions based on data. Causal inference by itself describes a conclusion regarding the effect of a causal variable.

## Background
Causality is usually confused with correlations, leading to the terming of the phrase correlation doesn’t infer causality. Causality can be interpreted as seeking intervention, doing something while correlation is focused on statistics of the features.

With correlation the function behind it is P(X|y) which can be translated as the probability of X given y, the causality function builds on that and makes some slight tweaks adding a do clause to the formula making it P(x|do(y))- the probability of x given that y is done. It also noted the need for causal inference to account for confounders as they introduce correlations that may muddle the causal diagram. Confounders can be defined as variables that have a causal relationship with two variables that are being tested for causality. 

## Project 
This project carries out causal inferencing on breast-cancer data. With the aim of understanding how this features affect the diagnosis of Breast cancer.Detection of Breast cancer is accomplished by revieweing the properties of a cell, this features can be used to classify the cell as malignant or bening. 

We plan to understand how the relationship between these features determine the type of class the cell falls into 

## Repo Layout

**script** Includes scripts used for the processing of data

**logs** run logs for the system

**notebooks** notebooks used for data preprocessing



