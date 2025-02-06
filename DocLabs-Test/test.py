from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return "DocLabs ONLINE"

@app.route('/', methods=['POST'])
def json():

    # Get the JSON data from the request
    data = request.get_json()

    # Assign variables w/ JSON data
    session_id = data.get('session_id')
    language = data.get('language')
    file_name = data.get('file_name')
    code = data.get('code')

    # Make directory cooresponding to session id
    os.makedirs(session_id, exist_ok=True) 

    # Move to the directory
    try:
        os.chdir(session_id)
        print("Current working directory changed to:", os.getcwd())
    except FileNotFoundError:
        print("Directory not found:", id)
    except Exception as e:
        print("An error occurred:", e)

    # Execute the code
    if language == "Python":
        result = executePython(file_name, code)
    else:
        result = "Invalid language parameter."
    
    # Move back to parent dir and delete session
    os.chdir("..")
    os.rmdir(session_id)
    
    # Return the result as a JSON
    data = {'result' : result}
    return jsonify(data)

def executePython(file_name, code):
    with open(file_name, "w") as f:
        f.write(code)
    result = subprocess.run(["python3", file_name], capture_output=True, text=True)
    stdout_output = result.stdout
    os.remove(file_name)
    return stdout_output
