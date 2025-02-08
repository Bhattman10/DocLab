from flask import Flask, request, jsonify
import os
import subprocess
import shutil

app = Flask(__name__)

def create_file(file_name, code):
    with open(file_name, "w") as f:
        f.write(code)

def extract_file_type(string):
    index_of_dot = string.index('.')
    return string[index_of_dot:]

def executePython(file_name):
    result = subprocess.run(["python3", file_name], capture_output=True, text=True)
    stdout_output = result.stdout
    return stdout_output

@app.route('/')
def hello():
    return "DocLabs ONLINE"

@app.route('/', methods=['POST'])
def json():

    # Get the JSON data from the request
    data = request.get_json()

    # Assign variables w/ JSON data
    session_id = data.get('session_id')
    files = data.get('files')
    number_of_files = len(files)

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

    # Create the files in the directory
    for i in range(number_of_files):
        create_file(files[i][0], files[i][1])
    
    # Store values of main file
    file_to_execute = files[0][0]
    file_type = extract_file_type(file_to_execute)

    # Execute the main file
    if file_type == ".py":
        result = executePython(file_to_execute)
    else:
        result = "Invalid language parameter."
    
    # Move back to parent dir and delete session
    os.chdir("..")
    path = "./" + session_id
    try:
        shutil.rmtree(path)
        print(f"Directory '{path}' and its contents have been removed successfully.")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Return the result as a JSON
    data = {'result' : result}
    return jsonify(data)