# DocLabs

Google Docs extension that provides Real-time Collaborative Programming (RCP) in one or multiple languages. The collaborative editing environment will be leveraged to create a quick, portable, shared software development environment for quick code demos/sketches.

## How to Run & Test DocLabs

### Step 1: Set up Docker.

1. Download Docker Desktop & create an account.
2. Navigate to the project directory and open a terminal. Enter the following:
```
docker login -u [username] -p [password]
```

### Step 2: Compile & run the backend.

To start the backend \(or make backend changes take effect\) enter the following:

```
docker compose up -d --no-deps --build backend
```

You can view the backend logs on Docker Desktop, or run the following command:

```
docker compose logs backend
```

### Step 3: Compile & run the testing suite.

To run the testing suite & see results \(plus make changes to testing suite take effect\) enter the following:

```
docker compose up --no-deps --build tests
```

### Step 4: Gracefully shut down the running containers.
```
docker compose stop
```