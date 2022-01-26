import os

from flask import Flask, render_template, request, redirect, url_for
import decrypt

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        return redirect(url_for('result',
                                password=password))
    return render_template('index.html')


@app.route('/result', methods=['GET'])
def result():
    with open('/root/express_system/password.txt', 'r') as f:
        encrypt_text = f.read()
    password = request.args.get('password')
    if password == decrypt.decrypt_data(encrypt_text):
        os.system(‘bash /root/express_system/open.sh’)
        return render_template("correct.html",
                               password=password)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True, port=8443)
