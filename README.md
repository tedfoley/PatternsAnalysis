# PatternsAnalysis
Categorization and ML Analysis of User Computer Usage Patterns Data

***The data required to execute this code is not publicly accessible and therefore is not included in this repository.***

The repository consists of three folders:

***Only the "Main Project" folder contains the real code for the final project***

1. Main Project - This is where the code for the final version of the project resides. It can be run in the following order:

DataUpload - uploads, cleans, and categorizes the data using ada-embeddings
SurveyUpload - uploads and cleans the survey data

The three "ML" files:

SurveyML - performs simple statistical analysis (mostly regressions) on the survey data
DataML - attempts more advanced predictions using gradient boosted trees
EmbeddingML - the most ambitious part of the project, implements a LSTM neural net to predict survey outcomes based on the embedded user data

----------------------------------------

2. Webscraping - This folder contains an old attempt to webscrape information about applications from the internet to be used for the embeddings (do not run)
3. Old Categorization - This folder contains an old attempt to categorize the apps by directly querying a local LLM or OpenAI gpt model (do not run)