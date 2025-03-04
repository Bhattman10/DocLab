# DocLabs

Google Docs extension that provides Real-time Collaborative Programming (RCP) in one or multiple languages. The collaborative editing environment will be leveraged to create a quick, portable, shared software development environment for quick code demos/sketches.

## Getting Started w/ Dev Environment

The following steps outline how to set up the dev environment w/ VS Code.

### Step 1: Download Docker & Extensions

Download Docker & the following VS Code extensions:
1. Remote Connect
2. Dev Containers

### Step 2: Start Developement Container

1. Click remote connect in the bottom left, then "Clone Repository in Container Volume".
2. Enter the respository "Bhattman10/DocLabs".
3. Select the branch you want to develop.

*The container uses an Ubuntu base image with Python. All requirements are automatically donaloded once the container is built. View & edit the deployment JSON in the folder "devcontainer".*

### Step 3: Execute Services

Run the Flask API in DocLabs/Backend:
```
flask --app main.py --debug run --host=0.0.0.0 --port=5000
```
Run the testing suite in DocLabs/Frontend:
```
pytest
```
### Step 4: Debugging

The launch.json is preset for debugging "Backend/main.py" & "Tests/test_scenarios.py" via debuggy.

### Step 5: Exiting

You can exit the dev environment simply by closing the remote connection. The environment image will automatically be saved to your docker dameon.