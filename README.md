DEMO LINK [Click Here](https://drive.google.com/file/d/1n2HQsCaE5FNy5dq8m8DLfEbgFHlNw7Pt/view?usp=sharing)
<br>



# Career Path Predictor
Your Career Decision Goal is just a few Questions Away !

An ML WebApp that can help any person who is quite confused about his future career prospects.
## Description

- This is a Machine Learning Model that uses Supervised Machine Learning technique to suggest a proper career goal for the user.
- The Front‑end part of the model is built by importing Streamlit library and along with Custom CSS(Cascading Style Sheets).
- The users must answer few specific career‑based questions and this ML WebApp analyses the answer patterns via Supervised Machine Learning algorithm and then predicts Career Path suitable for that user.
## Technologies

**Client:** Streamlit, HTML, CSS(Cascading Style Sheets)

**ML Algorithm:** Random Forest Classifier


## Challenges Faced

- Initially, the project was based on K-Nearest Neighbours(KNN) Algorithm that had a quite lesser Accuracy of approximately 85%.
- Then we tried many Supervised techniques like Logistic Regression, Decision Trees, Support Vector Classifier but all of them had the similar range of Accuracy.
- Finally, an increase in accuracy was made possible by the help of Random Forest Classifier, which is an Ensemble Based Technique.
- By using Random Forest Technique the accuracy of our model shot up by 15%, giving us an accuracy of 98%.
## Installation

You can install and run the project by running Main1.py program by using `streamlit` command.

```bash
  streamlit run Main1.py
```
    
## Dataset

- The Dataset file consist of 19 coloumns that can be considered as the features for training the dataset.
- Each attribute value within a record is an answer for the particular question(column/attribute name).
- Every record is mapped to one of the 10 Career Path Options that are available for now and will be updated more for the next version.

