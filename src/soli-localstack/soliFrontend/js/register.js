function register(e) {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:8000/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
        .then(res => res.json())
        .then(data => {
            if (data.message === "User registered successfully") {
                alert("Registration successful!");
                window.location.href = "login.html";
            } else {
                alert(data.message || "Error registering");
            }
        })
        .catch(() => alert("Error registering user"));
}
