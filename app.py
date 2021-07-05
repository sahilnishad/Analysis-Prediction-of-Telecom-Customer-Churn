from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method=='POST':

        gender = int(request.form['gender'])
        SeniorCitizen = int(request.form['SeniorCitizen'])
        Partner = int(request.form['Partner'])
        Dependents = int(request.form['Dependents'])
        tenure = int(request.form['tenure'])
        PhoneService = int(request.form['PhoneService'])
        MultipleLines = int(request.form['MultipleLines'])
        InternetService = int(request.form['InternetService'])
        OnlineSecurity = int(request.form['OnlineSecurity'])
        OnlineBackup = int(request.form['OnlineBackup'])
        DeviceProtection = int(request.form['DeviceProtection'])
        TechSupport = int(request.form['TechSupport'])
        StreamingMovies = int(request.form['StreamingMovies'])
        Contract = int(request.form['Contract'])
        PaperlessBilling = int(request.form['PaperlessBilling'])
        PaymentMethod = int(request.form['PaymentMethod'])
        MonthlyCharges = float(request.form['MonthlyCharges'])
        TotalCharges = int(request.form['TotalCharges'])

        input = pd.DataFrame([[gender,SeniorCitizen,Partner,Dependents,tenure,
                                PhoneService,MultipleLines,InternetService,OnlineSecurity,
                                OnlineBackup,DeviceProtection,TechSupport,StreamingMovies,
                                Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]])
        
        output = model.predict(input)
        result = output[0]

    if result==0:
        prediction="not churn 😀"

    else:
        prediction="churn 😧"
 

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)