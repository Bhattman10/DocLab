# DocLabs

Google Docs extension that provides Real-time Collaborative Programming (RCP) in one or multiple languages. The collaborative editing environment will be leveraged to create a quick, portable, shared software development environment for quick code demos/sketches.

## Test & Developement Guide

The backend runs on containers to streamline the developement process. The following steps outline how to get started with testing and development of the project via Docker.

### Step 1: Download & initialize Docker.

1. Download Docker Desktop & create an account.
2. Make sure Docker Desktop is open. This ensures the daemon is online.
3. Navigate to the project directory and open a terminal. Enter the following:
```
docker login -u [username] -p [password]
```

### Step 2: Create the containers.

Use the following command to compile & create the containers:

```
docker compose up --build --no-start
```

Docker compose mounts the containers w/ local source files so that changes are applied automatically.

### Step 3: Run the backend server.

Enter the following to run the server:

```
docker start -a backend
```

### Step 4: Run the testing suite.

In a new terminal, enter the following:

```
docker start -a tests
```

### Step 5: Shut down the backend.

Enter the following to gracefully shut down the containers:

```
docker compose down
```