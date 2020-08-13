import os
import platform
import sys

from flask import Flask
from flask import render_template
from flask import request
from flask import abort, redirect, url_for

app = Flask(__name__, template_folder='templates')


def sys_info():
    if platform.system() == "Windows":
        print('Windows')
        os.system('chcp 1252') # Windows the best!1!!
    elif platform.system() == "Linux":
        print('Linux')
    elif platform.system() == "Darwin":
        print('Mac')
    else:
        print('Unknown OS')

def html_encode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ('&', '&amp;'),
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            (' ', '&nbsp;'),
            ('\n', '<br>')
        )
    for code in htmlCodes:
        s = s.replace(code[0], code[1])
    return s

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_command():
    error = None
    command = str(request.form['command'])
    response = html_encode(os.popen(command).read())
    print(response)
    if request.method == 'POST':
        return render_template('index.html',
        command=html_encode(command),
        response=response)
    return response

if __name__ == "__main__":
    sys_info()
    app.debug = True
    app.run()
