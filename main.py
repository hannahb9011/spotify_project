#!/usr/bin/python3
from flask import Flask, render_template, request
import paramiko 

# Our VM's information
host = "129.114.25.206" # public key
username = "cc"
password = "csgroup3"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

stdin, stdout, stderr = client.exec_command("./run_spark.sh")
data = stdout.read().decode()
datasplit = data.split('()()()')

for x in range(len(datasplit1)):
    datasplit[x] = datasplit[x].split("~!")

stdin.close()
client.close()

app = Flask(__name__)


#@app.route('/')
#def root():
#    return render_template('index.html', var=data)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return render_template('index.html', var=data)
    elif request.method == 'GET':
        return render_template('index.html', form=form)
    
    return render_template("index.html")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

