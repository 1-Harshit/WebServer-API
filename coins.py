from flask import request, jsonify, Flask, render_template
import json

# Why flask? Because it's the first thing google gave me
app = Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of a list of dictionaries.
FILENAME = "out.txt"

# IDK why I'm printing this
print("kuch to ho rhaa hai...")

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
        <p>To see Number of coins to a roll number: <a href="/coins">Click Here</a></p>
        </body></html>'''


# A route to return all of the available entries in our rcoin.
@app.route('/all', methods=['GET'])
def api_all():
    return jsonify(rcoin)

# 
@app.route('/coins', methods=['GET', 'POST'])
def coins():
    # Check if roll was provided as part of the URL.
    # If roll is provided, assign it to a variable. Else ask for it.
    if 'roll' in request.args:
        roll = str(request.args['roll'])
    elif request.method == "POST":
       # getting input with name = fname in HTML form
       roll = str(request.form.get("roll"))
    else:
        return '''<html>    
            <head><title>How rich are you?</title></head>
            <body>
            <form action = "/coins" method = "post">
            <label for="roll">Enter Roll:</label><br>
            <input type="text" id="roll" name="roll" placeholder="Y18-Y19-Y20 Roll"><br>
            <button type="submit">Search</button>
            </form>
            </body></html>'''
    
    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for entry in rcoin:
        if entry['roll'] == roll:
            results.append(entry)
            break

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

# Error404
@app.errorhandler(404)
def page_not_found(e):
    return '''<h1>404</h1><p>The resource could not be found.</p>
    <p>To view the homepage: <a href="/">Click Here</a></p>''', 404

# Listen on port 8080
app.run(port=8080)
