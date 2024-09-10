from flask import Flask
app = Flask(__name__)

@app.route('/')
def rvce():
         return "<p style='text-align:right'>Go, Change the world</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)