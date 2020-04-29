from flask import Flask
from flask import request,request,render_template,jsonify
from waitress import serve

import pickle
import numpy as np
from PIL import Image
import io

import imgdetect

app = Flask(__name__)
global model
model=pickle.load(open('./model/predictsale_model.pkl','rb'))



@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/plus')
def plus():
    a= int(request.args.get('a'))
    b= int(request.args.get('b'))
    return str(a+b)

#Predict sale
@app.route('/predictsaleprice')
def predictsaleprice():
    return render_template('predictsale.html')

@app.route('/predictresult',methods=['POST'])
def predictresult():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    print(final_features)
    prediction=model.predict(final_features)
    ouput=round(prediction[0],2)

    return render_template('predictsale.html',prediction_text="Predicted Sale: {}".format(ouput))

@app.route('/predictJson',methods=['POST'])
def predictJson():
    #Sample {"rate":5,"sale1":200,"sale2":1000}
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])
    output=round(prediction[0],2)

    return jsonify(output)

@app.route('/detectImage',methods=['POST'])
def detectImage():
    img = request.files["image"].read()
    img = Image.open(io.BytesIO(img))
    npimg=np.array(img)
    return imgdetect.detect_image(npimg)


if __name__ == '__main__':
   #app.debug = True
   #app.run(host='0.0.0.0',port=8000)
   serve(app, host="0.0.0.0", port=8000)
