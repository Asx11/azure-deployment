from flask import Flask, request, render_template
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from os.path import join, dirname, realpath
import os
from MedNet import MedNet
 
model = torch.load('saved_model')
classliste=['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']


app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/action_page", methods=['GET', 'POST'])
def upload():
    dirnames = join(dirname(realpath(__file__)), 'static/upload')
    UPLOAD_FOLDER = dirnames
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        if request.files:
            file1 = request.files['file1']
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1.filename))
            return   predict(file1)

def scaleImage(y):          
    if(y.min() < y.max()):  
        y = (y - y.min())/(y.max() - y.min()) 
        z = y - y.mean()  
        return z      


def predict(file1):
    img = Image.open(file1)
    my_transforms = transforms.Compose([transforms.ToTensor(),transforms.Resize(64),transforms.Normalize([0.5 ],[0.5 ])])
    xtest= my_transforms(img).unsqueeze(0)
    xtest=scaleImage(xtest)
    yOut = model(xtest)
    indices = yOut.max(1)[1].tolist()[0]
    pred = classliste[indices]
    print(file1.filename)
    return render_template('index.html',prediction_text='Picture: {} '.format(pred),img_filename='static/upload/' + file1.filename )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)