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
