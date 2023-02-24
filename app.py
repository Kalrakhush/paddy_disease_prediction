import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
#Loading models
Diseases=pickle.load(open('Plant Diseases.pkl','rb'))


@app.route('/')
def home():
    return render_template("images_mat.html")



@app.route('/predict_diseases',methods=['POST'])
def predict():
    '''
    For Rendering results on html gui'''

    int_features=[float(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    output=Diseases.predict(final_features) 

    if(int(output)==0):
        prediction = "Blast"
    elif(int(output)==1):
        prediction = "Hispa"
    elif(int(output)==2):
        prediction = "False Smut"
    elif(int(output)==3):
        prediction = "Stem Rot"    


    return render_template("images_mat.html",prediction_text="The predicted disease is:"+prediction)

    

if __name__=='__main__':    
    app.run(debug = True)  # it will automatically revoke changes
    