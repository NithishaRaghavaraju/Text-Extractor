from flask import Flask,request, url_for, redirect, render_template
import pickle
from werkzeug.utils import secure_filename
import cv2
app = Flask(__name__,template_folder='templates')
import easyocr
reader = easyocr.Reader(['en'])
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predicted():
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(filename)
    image = cv2.imread(filename)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    c = " "
    for i in range(len(result)):
        char = result[i][1]
        c += char + " "
    r = c
    return render_template("index.html", pred= r)
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
