from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your ML model
model = joblib.load('best_model.pkl')  # make sure the model file is saved as 'best_model.pkl'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_text = request.form['user_input']
        prediction = model.predict([user_text])[0]
        label = "Hate Speech" if prediction == 1 else "Not Hate Speech"
        return render_template('result.html', input_text=user_text, result=label)

if __name__ == '__main__':
    app.run(debug=True)
