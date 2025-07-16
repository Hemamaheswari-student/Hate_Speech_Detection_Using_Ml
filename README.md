# 🛡️ Hate Speech Detection System using Machine Learning

This project is a web-based Hate Speech Detection System built with **Python**, **Flask**, and **Bootstrap**. It uses a trained machine learning model to classify whether a given piece of text contains hate speech or not. The system is designed to be simple, responsive, and easily deployable.

---

## 🚀 Features

- 🔍 Detects hate speech from user-input text
- 🧠 Integrated with a trained ML model (`best_model.pkl`)
- 🌐 Responsive user interface using HTML, CSS, and Bootstrap
- 🛠️ Flask backend for handling requests and predictions
- 💬 Real-time prediction results

---

## 🧠 Machine Learning Model

- Developed and trained in Jupyter Notebook
- Uses  SGDClassifier[insert algorithm used, e.g., Logistic Regression, SVM, etc.]
- Saved using `joblib` as `best_model.pkl`

---

## 📁 Project Structure
#here we are using the Flask python webframework
#Before Executing the project the project structure should be like the mentioned below
hate_speech_app/------>(projectfolder)
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── best_model.pkl
├── app.py
└── requirements.txt
#code for saving the machine learning model
----->Save Your Model as best_model.pkl
               -->import joblib
                  joblib.dump(best_model, 'best_model.pkl')
#creating the python virtual environment with the information in requirement.txt
        --->Flask==2.3.2
            joblib
            scikit-learn
#creating python Environment
----->python -m venv venv
#enabling the pyhton environment
------>venv\Scripts\activate on windows and 
#install all the librarires mentioned in requirement.txt
----->pip install -r requirements.txt
#run our Flask app inside that environment
----->python app.py
Open browser and visit http://127.0.0.1:5000
<------Example------->
Input:
You are such an idiot!

Output:
Hate Speech
