import json

# Create some test data for our catalog in the form of a list of dictionaries.
FILENAME = "out.txt"

# IDK why I'm printing this
print("kuch to ho rhaa hai...")

inFile = open(FILENAME, 'r')
line = inFile.readline()

# This is now my list of all roll and coins
rcoin = json.loads(line)

# home screen
roll = "200433"

for entry in rcoin:
    if entry['roll'] == roll:
        print(json.dumps(entry))
