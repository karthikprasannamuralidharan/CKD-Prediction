from flask import Flask, render_template 
import numpy as np
import joblib
import pandas as pd

from flask import request
app = Flask(__name__,template_folder='templates')


def gfr(forgfr):
    if len(forgfr) == 8:
        age = int(forgfr[0])
        #print("age "+str(age))
        gen = forgfr[1]
        #print("gen "+str(gen))
        race = forgfr[2]
        #print("race "+str(race))
        sc = forgfr[5]
        #print("sc "+str(sc))
        #print(forgfr)
        if age >= 18:
            if gen == 1:
                if race == 1:
                    if float(sc) <= 0.9: 
                        GFR = 163 * ( (sc/0.9)**(-0.411)) * ((0.993)**age)
                    else:
                        GFR = 163 * ( (sc/0.9)**(-1.209)) * ((0.993)**age)
                else:
                    if float(sc) <= 0.9: 
                        GFR = 141 * ( (sc/0.9)**(-0.411)) * ((0.993)**age)
                    else:
                        GFR = 141 * ( (sc/0.9)**(-1.209)) * ((0.993)**age)
            else:
                if race == 1:
                    if float(sc) <= 0.7: 
                        GFR = 166 * ( (sc/0.9)**(-0.329)) * ((0.993)**age)
                    else:
                        GFR = 166 * ( (sc/0.9)**(-1.209)) * ((0.993)**age)
                else:
                    if float(sc) <= 0.7: 
                        GFR = 144 * ( (sc/0.9)**(-0.329)) * ((0.993)**age)
                    else:
                        GFR = 144 * ( (sc/0.9)**(-0.411)) * ((0.993)**age)   
        #print(GFR)
        stage = " "
        if GFR > 90:
            stage = "Stage 1 : Normal kidney function but urine findings or structural abnormalities or genetic trait point to kidney disease"
        elif GFR >= 60 or GFR <= 89 :
            stage = "Stage 2 : Mildly reduced kidney function, and other findings (as for stage 1) point to kidney disease"
        elif GFR >= 30 or GFR <= 59 :
            stage = "Stage 3 : Moderately reduced kidney function"
        elif GFR >= 15 or GFR <= 29 :
            stage = "Stage 4 : Severely reduced kidney function"
        elif GFR < 15 :
            stage = "Stage 5 : Very severe, or end-stage kidney failure"
        print(stage)
        return GFR,stage

def predict(values):
    if len(values) == 8:
        model = joblib.load('./model/ckd.pkl')
        scaler = joblib.load('./model/scaler.bin')
       # print(model)
        values = np.asarray(values)
        #print(type(values))
        values = values[3:]
        #print(values)
        #print("values",values)
        #print(values.shape)
        values = pd.DataFrame(values.reshape(-1,5), columns = ['hemo', 'pcv', 'sc', 'sg', 'rbcc'])
        #print(df[0:1])
        values = scaler.transform(values)
        df = pd.DataFrame(values.reshape(-1,5), columns = ['hemo', 'pcv', 'sc', 'sg', 'rbcc'])
       # print(values)
        val = model.predict(df)
        #print("val",val)
        val = val[0]
        return val
#17.10	41.0	0.80	1.020	5.2
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/prediction', methods = ['POST', 'GET'])
def predict_ckd():
    pred = ""
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            #print(to_predict_dict)
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            #print(to_predict_list)
            pred = predict(to_predict_list)
            forgfr,stage = gfr(to_predict_list)
            #print(pred)
            return render_template("pred.html", pred = pred,forgfr=int(forgfr),stage=stage)

    except:
        pred = "Please enter valid Data"
        return render_template("pred.html", pred = pred)

    return render_template('prediction.html')
    

if __name__ == '__main__':
    app.run(debug=True)


 