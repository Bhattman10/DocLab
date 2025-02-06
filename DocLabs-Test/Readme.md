DocLabs-Test demonstrates elementary backend functionaility using a tester frontend written in JS.
### Setting up the envrionment
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
