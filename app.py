import setup_and_run_website
import sys
import os
from datetime import datetime
from flask import Flask, render_template, send_from_directory
from flask import url_for, redirect, jsonify, request
import on_demand

#from flask_s3 import FlaskS3


#from flask.ext.assets import Environment, Bundle

#-----------------------------
# initialization
# -----------------------------

app = Flask(__name__)
app.config['jsflask'] = 'jsflask'
#s3 = FlaskS3(app)


app.config.update(
    DEBUG=True,
)

#------------------------------
#Configuration
#------------------------------

#ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/js')

#app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

###################
# main page
###################
@app.route('/')
def base():
    print 'index hit'
    return render_template('index.html')

###################
# about page
###################
@app.route('/about')
def about():
    print 'about hit'
    return render_template('about.html')

###################
# contact us page
###################
@app.route('/contact')
def contact():
    print 'contact hit'
    return render_template('contact.html')





###################
#image upload and eval script!
###################
app.config['UPLOAD_FOLDER'] = 'uploads'
@app.route('/upload', methods=['POST'])
def upload():
    MAX_FILESIZE = 1000000; #1 mb
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        print 'hit'
    
        file1 = request.files['file1']
        size1 = len(file1.read());
        print size1
        file2 = request.files['file2']
        size2 = len(file2.read());
        print size2
        if ((size1 < MAX_FILESIZE) and (size2 < MAX_FILESIZE)):
            if file1 and file2 and allowed_file(file1.filename) and allowed_file(file2.filename):



                now = datetime.now()
                filename1 = os.path.join(app.config['UPLOAD_FOLDER'], "%s_1.%s" % (now.strftime("%Y-%m-%d-%H-%M-%S-%f"), file1.filename.rsplit('.', 1)[1]))
                print filename1
                file1.save(filename1)
                filename2 = os.path.join(app.config['UPLOAD_FOLDER'], "%s_2.%s" % (now.strftime("%Y-%m-%d-%H-%M-%S-%f"), file2.filename.rsplit('.', 1)[1]))
                print filename2
                file2.save(filename2)
                
                ##############
                # now call matlab call!!!!
                ###############
                try:
                    if on_demand.decide(setup_and_run_website.matlab_scripts_dir,
                                        setup_and_run_website.params_scripts_dir,
                                        os.path.abspath(filename1),
                                        os.path.abspath(filename2)
                                    ):
                        return_object = jsonify(success=True,reason_code='')
                        print 'success!'
                    else:
                        return_object = jsonify(success=False,reason_code='')
                except Exception as e:
                    return_object = jsonify(success=False, reason_code="".join("error!",e.message))
                ################

                # now delete the images..
                os.remove(filename1) 
                os.remove(filename2) 
            else:
                return_object = jsonify(success=False, reason_code='Image File too big! 160x160px!') 
            return return_object

ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#------------------------------
#launch
#------------------------------

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=80)

