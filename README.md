**Project Title: Chronic Kidney Disease (CKD) Classification**

**Objective**: The project aims to develop and evaluate machine learning and deep learning models for the classification of Chronic Kidney Disease (CKD) based on a dataset with various clinical features.

**Key Steps and Components:**

**Data Preparation:**

The project begins by loading and preprocessing the CKD dataset.
Data cleaning is performed, including replacing missing values (e.g., using K-nearest neighbors imputation).
The dataset is divided into features (X) and the target variable (y).
Feature Selection:

**Two feature selection methods are employed:**
Method 1: Feature importances are calculated to select the most relevant features.
Method 2: SelectKBest is used with F-statistic scores to choose the best features.
Both methods are explored for different numbers of selected features.
Machine Learning Models:

**Three classification algorithms are trained and evaluated:**
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
Decision Tree (DT)
Grid search is used to optimize hyperparameters for each algorithm.

**Deep Learning Models:**
Convolutional Neural Networks (CNNs) are employed for feature extraction and classification.
Different subsets of features are used as input to the CNN models.
The models are trained and evaluated using metrics like accuracy, precision, recall, F1-score, classification reports, and confusion matrices.

**Model Evaluation:**

The project reports the performance metrics of each model for various feature selections, including accuracy, recall, precision, and F1-score.
Confusion matrices and classification reports are used to assess model performance.
Class imbalance is handled using class weights to address potential bias.

**Model Persistence:**

The best-performing SVM model and a feature scaler are saved using joblib for future use.
New data can be preprocessed using the saved scaler and classified using the saved SVM model.

**Results:**

Performance metrics for the three machine learning models are reported, showing that SVM achieved the highest accuracy, precision, and F1-score.

**Summary:**
This project focuses on the classification of CKD using machine learning and deep learning techniques. It explores different feature selection methods and models to find the best combination for accurate CKD classification. The SVM model stands out as the top-performing model, achieving high accuracy, precision, and F1-score. These results provide valuable insights into building a robust CKD classification system.
