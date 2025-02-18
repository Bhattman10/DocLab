# DocLabs

Google Docs extension that provides Real-time Collaborative Programming (RCP) in one or multiple languages. The collaborative editing environment will be leveraged to create a quick, portable, shared software development environment for quick code demos/sketches.

## How to Run & Test the Backend

1. Verify that Docker is downloaded to your system and that you are logged in.
2. Run the following to start/refresh the backend & testing suite:

```
docker compose up -d --build
```

3. Run the following to view the pytest results:

```
docker compose logs tests
```

4. To shut down the service, run the following:

```
docker compose down
```
