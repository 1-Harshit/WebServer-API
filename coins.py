from flask import request, jsonify, Flask
import os

# Why flask? Because it's the first thing google gave me
app = Flask(__name__)
# app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
FILENAME = "db.json"

inFile = open(FILENAME, 'r')
line = inFile.readline()

# This is now my list of all roll and coins
rcoin = json.loads(line)

# home screen
@app.route('/', methods=['GET'])
def home():
    return '''<html><head><title>Coins</title></head>
        <body><h1>Whats poppin</h1>
        <p>So, click on the links. to do things :\</p>
        <p>To view the entire list of database: <a href="/all">Click Here</a></p>
        <p>Post request on '/coins'</p>
        </body></html>'''


# A route to return all of the available entries in our rcoin.
@app.route('/all', methods=['GET'])
def api_all():
    return jsonify(rcoin)

# 
@app.route('/coins', methods=['GET', 'POST'])
def coins():
    # Check if roll was provided as json.
    if request.method == "POST":
       data = dict(request.get_json())
       roll = str(data['rollno'])
    else:
        return 'Only Post method'

    # Loop through the data and match results that fit the requested roll.
    for entry in rcoin:
        if entry['roll'] == roll:
            result = {"coins" : int(entry['coins'])}
            # Use the jsonify function from Flask to return in JSON format.
            return jsonify(result)

    # if no matches found
    return "No record found Please enter valid roll no"

# Error404
@app.errorhandler(404)
def page_not_found(e):
    return '''<h1>404</h1><p>The resource could not be found.</p>
    <p>To view the homepage: <a href="/">Click Here</a></p>''', 404

# Listen on port 8080
app.run(int(os.getenv('PORT', 8080)))
