function login(e) {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:8000/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
        .then(res => res.json())
        .then(data => {
            if (data && data.access) {
                localStorage.setItem("token", data.access);
                window.location.href = "upload.html";
            } else {
                alert("Invalid credentials");
            }
        })
        .catch(() => alert("Error logging in"));
}
