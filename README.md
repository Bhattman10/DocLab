# DocLabs

Google Docs extension that provides Real-time Collaborative Programming (RCP) in one or multiple languages. The collaborative editing environment will be leveraged to create a quick, portable, shared software development environment for quick code demos/sketches.

## How to Run & Test the Backend

1. Verify that Docker is downloaded to your system and that you are logged in.
2. Navigate to "Backend" and run the following:

```
docker build -t backend .
docker run -dp 5000:5000 backend
```

3. Navigate to "Tests" and run the following:

```
docker build -t tests .
docker run tests
```
