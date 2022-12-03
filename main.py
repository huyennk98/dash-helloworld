from flask import Flask
# app.layout = html.Div(id='example-div-element')

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return("Hello world")

if __name__ == "__main__":
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
