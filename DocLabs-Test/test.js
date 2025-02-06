verify();
send();

async function verify() {
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

async function send() {

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: JSON.stringify(
            {
                session_id: '12345',
                language: 'Python',
                file_name: 'hello.py',
                code: 'print("Hello World!")'
            }
        ),
        headers: myHeaders,
    })
        .then(response => response.json())
        .then(data => { console.log(data.result); });
}
