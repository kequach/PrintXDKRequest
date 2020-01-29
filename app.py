# app.py
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

lightList = []

@app.route('/example')
def example():
    return "Hello, World!"

@app.route('/XDK', methods=['POST'])
def printXDK():

    # For debugging
    light = str(request.json['light'])
    print("The current light value:" + light + " lux")
    lightList.append(light)

    # Return the response in json format
    return light

# Browser print
@app.route('/')
def index():
    return render_template('index.html', lightList=lightList)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)