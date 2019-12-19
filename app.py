# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

lightList = []
@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/XDK', methods=['POST'])
def printXDK():

    # For debugging
    light = str(request.json['light'])
    print("The current light value:" + light + " lux")
    lightList.append(light)

    # Return the response in json format
    return light

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.json['name']
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality

# A welcome message to test our server
@app.route('/')
def index():
    printHtml = "<h1>Welcome to the light measurement !!</h1> "
    printHtml = printHtml + '''
        <table class="tg">
        <tr>
            <th class="tg-0pky">Number</th>
            <th class="tg-0pky">Light value</th>
        </tr>'''
    num = 1
    for value in lightList:
        print(help(value))
        help(value)
        printHtml = printHtml + '''
        <tr>
            <td class="tg-0pky">''' +num+'''</td>
            <td class="tg-0pky">''' +value+'''</td>
        </tr>
        '''
        num = num + 1

    printHtml = printHtml + '</table>'

    return printHtml

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)