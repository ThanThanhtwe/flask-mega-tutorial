from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
    <head><title>This is my Index.</title></head>
    <body><h1>Hello San Thawm</h1></body>
    </html>
    '''

if __name__ =="__main__":
    app.run(debug=True)
