#!flask/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)
CREDENTIAL = {"Eli Lu": "1234567890"}

def checkCredential(content):
    if CREDENTIAL[content['Name']] == content['ID']:
        return True
    else:
        return False

@app.route('/api/login', methods=['POST'])
def login():
    global CREDENTIAL
    content = request.json
    if content is None:
        return jsonify({"status": 'Failure'})
    for k, v in content.items():
        print("{} -> {}".format(k, v))

    if ('Name' in content) & ('ID' in content):
        res = checkCredential(content)
        if res:
            return jsonify({"status": 'Successful'})
        else:
            return jsonify({"status": 'Failure'})

    else:
        return jsonify({"status": 'Failure'})


if __name__ == '__main__':
    app.run(port=8090)