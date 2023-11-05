## Diabetes Prediction

According to IDF (the International Diabetes Federation) 1 in 10 people are living with diabetes: https://idf.org/. 
By 2045, IDF projections show that 1 in 8 adults, approximately 783 million, will be living with diabetes, an increase of 46%. 

Over 90% of people with diabetes have type 2 diabetes, which is driven by socio-economic, demographic, environmental, and genetic factors. The key contributors to the rise in type 2 diabetes include:
<li> Urbanisation
<li> An ageing population
<li> Decreasing levels of physical activity
<li> Increasing overweight and obesity prevalence

However, it is possible to reduce the impact of diabetes by taking preventive measures for type 2 diabetes and providing early diagnosis and proper care for all types of diabetes. These measures can help people living with the condition avoid or delay complications.

### Project Overview
Diabetes is a chronic medical condition that affects millions of people worldwide. Early diagnosis and prediction of diabetes can be crucial for timely intervention and better management of the disease. This machine learning project aims to build a predictive model for diabetes diagnosis based on medical records. The model shouldn't be used for self-diagnosis, rather as a recommendation to visit medical professional.

The project involves data preprocessing, feature selection, model training, and evaluation to develop an accurate and reliable predictive model for diabetes. I utilized a publicly available dataset containing various attributes related to diabetes diagnosis and health metrics. The dataset is available on Kaggle platform (https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset).

### Data
Dataset can be downloaded from kaggle (https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) or found in this repo (diabetes_prediction_dataset.csv).

### Work notebook
In the notebook you can find:
<li> Data preparation and data cleaning
<li> EDA
<li> Model selection process and parameter tuning

https://github.com/olkudrina/diabetes_ml/blob/master/diabetes_project.ipynb

### Final model
Final model script can be found here: https://github.com/olkudrina/diabetes_ml/blob/master/xgboost_diabetes_train.py

It consists of loading the dataset, performing transformation, training model and fittin dictvestorizer, as well as exporting model to .bin file for further use.

### App
In https://github.com/olkudrina/diabetes_ml/blob/master/diabetes_predict.py the model is loaded and served via a web service using Flask.

### Docker
The file for building image is here: https://github.com/olkudrina/diabetes_ml/blob/master/Dockerfile, with dependencies located here: https://github.com/olkudrina/diabetes_ml/blob/master/requirements.txt
To create image, please run 

![image](https://github.com/olkudrina/diabetes_ml/assets/66033001/24ba5d31-42a2-4fae-aebb-8156bbf28353)

To run the service, please use

![image](https://github.com/olkudrina/diabetes_ml/assets/66033001/df68ac38-73a7-4788-8a22-05d6255c4c7f)

To send the request to the service, please use

![image](https://github.com/olkudrina/diabetes_ml/assets/66033001/f1ffa034-388b-4bbe-8ece-0112fcea6c81)


Developed as mid-term project for ML zoomcamp (https://github.com/DataTalksClub/machine-learning-zoomcamp) 
