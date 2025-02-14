// JS Fetch API Docs -> https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
// Our deployed version will utilize Google's version of Fetch.

verify();
send();

// Verify if Flask API is up and running
async function verify() {

    // This is the API url
    const url = "http://127.0.0.1:5000/";

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
    } catch (error) {
        console.error(error.message);
    }
}

// Send data to the server and recieve the execution result
async function send() {

    // Have some headers included here... do we need them?
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    files = [
        ["main.py", 'import my_functions\nname = "Ethan"\ngreeting = my_functions.greet(name)\nprint(greeting)\nx = 5\ny = 3\nsum_result = my_functions.add(x, y)\nprint(f"The sum of {x} and {y} is {sum_result}")'],
        ["my_functions.py", 'def greet(name):\n\treturn f\"Hello, {name}!\"\n\ndef add(a, b):\n\treturn a + b']
    ]

    const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        // Change the contents of the JSON to experiment!
        body: JSON.stringify(
            {
                session_id: '12345',
                files: files
            }
        ),
        headers: myHeaders,
    })
        // These commands wait for the JSON response from the server.
        // Is this proper syntax for the POST method? ChatGPT says no...
        .then(response => response.json())
        .then(data => { console.log(data.result); });
}