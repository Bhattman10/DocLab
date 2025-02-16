### What is DocLabs-Test?

Here you can experiment with backend functionaility. Test.js emulates how Google App Scripts will interact with the Flask API.

### Setting up the envrionment

Requirements: Python 3.13.1 Base Version

1. In the DocLabs-Test directory, create the virtual environment:

```
python3 -m venv .venv
```

Then, start the virtual environment:

```
. .venv/bin/activate
```

2. Within the activated environment, use the following command to install Flask:

```
pip install Flask
```

3. To run the application, enter the following:

```
flask --app test run
```

Currently, test is the name of the python file running flask. Change this argument if necessary.

### How do you trigger a request to the server?

Use Node.js to run the JavaScript file, which sends a JSON file to the Flask server. It then waits for the server to respond with its own JSON containing the execution result.

```
node test.js
```
