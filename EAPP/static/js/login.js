async function loginUser() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch('/api/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            User_Email: email,
            User_Password_Hash: password,
        })
    });

    const result = await response.json();
    
    if (response.ok) {
        // Redirect to the next page on successful login
        alert(result.message);
        window.location.href = '/categories';
    } else if (response.status === 404) {
        // Prompt user to register
        alert(result.error);
        window.location.href = '/register';
    } else {
        // Display other errors (e.g., incorrect password)
        alert(result.error);
    }
}