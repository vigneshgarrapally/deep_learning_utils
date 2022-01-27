from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
import yaml
import os
import sys
import shutil
import requests
import importlib
import pandas as pd
from datetime import datetime
import logging
app=Flask(__name__)

with open("config.yaml") as stream:
    settings=yaml.safe_load(stream)

@app.route('/')
def index():
    p=os.path.join("static","images","test_images")
    if os.path.exists(p):
        shutil.rmtree(p)
    return render_template("index.html",date_time=datetime.now(),settings=settings)

@app.route('/displayresults',methods = ['GET', 'POST'])
def displayresults():
    #upload images only using POST METHOD
    if request.method == 'POST':
        file = request.files.getlist("imagenames")
        os.makedirs(os.path.join("static","images","test_images"), exist_ok=True)
        for f in file:
            f.save(os.path.join("static","images","test_images",secure_filename(f.filename)))
        task=request.form['task']
        subtask=request.form['subtask']
        results=make_predictions(task,subtask)
    return render_template("predictions.html",results=results,date_time=datetime.now())



def make_predictions(task,subtask):
    module_path=settings["model"][task][subtask]["inference_script_path"]
    model_path=settings["model"][task][subtask]["model_path"]
    try:
        module_path=os.path.normpath(module_path)
        if os.path.isfile(module_path) and module_path.endswith(".py"):
            if not (module_path in sys.path):
                sys.path.append(os.path.dirname(module_path))
        else:
            logging.warning("Path to Inference Script is not a valid Python file")
        module=importlib.import_module(os.path.splitext(os.path.basename(module_path))[0])
    except ImportError:
        logging.warning("Unable to Import Inference Module.Exiting")
        sys.exit()
    results=module.predictions(model_path=model_path,images_path=os.path.join("static","images"))
    return results

def scrape_image(image_url):
    filename=image_url.split("/")[-1]
    filepath = os.path.join("static","test images",filename)
    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ',filepath)
    else:
        print('Image Couldn\'t be retreived')




if __name__=="__main__":
    try:
        app.run()
    except:
        print("Unable to start application")