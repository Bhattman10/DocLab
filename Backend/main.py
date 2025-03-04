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


def executePython(file_name, list_of_user_inputs):
    input_data = "\n".join(list_of_user_inputs)
    result = subprocess.run(["python", file_name],
                            capture_output=True, text=True, input=input_data)
    output = result.stdout
    errors = result.stderr

    return output, errors


@app.route('/')
def hello():
    return "DocLabs is running."


@app.route('/', methods=['POST'])
def json():

    # Get the JSON data from the request
    data = request.get_json()

    # Assign variables w/ JSON data
    session_id = data.get('document_id')
    list_of_file_names = data.get('list_of_file_names')
    list_of_code_contents = data.get('list_of_code_contents')
    list_of_user_inputs = data.get('user_input')

    number_of_files = len(list_of_file_names)

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
        create_file(list_of_file_names[i], list_of_code_contents[i])

    # Store contents & attributes of main file
    file_to_execute = list_of_file_names[0]
    file_type = extract_file_type(file_to_execute)

    # Determine the language and execute the main file
    if file_type == ".py":
        standard_output, errors = executePython(
            file_to_execute, list_of_user_inputs)
    else:
        standard_output = ""
        errors = "Invalid language parameter."

    # Move back to parent dir and delete session
    os.chdir("..")
    path = "./" + session_id
    try:
        shutil.rmtree(path)
        print(
            f"Directory '{path}' and its contents have been removed successfully.")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Return the result as a JSON
    data = {
        'standard_output': standard_output,
        'errors': errors
    }
    return jsonify(data)
