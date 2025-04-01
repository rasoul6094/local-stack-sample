document.getElementById("loading").style.display = "block";

fetch("http://127.0.0.1:8000/get/", {
    method: "GET",
    headers: {
        "Authorization": `Bearer ${localStorage.getItem("token")}`
    }
})
    .then(response => {
        if (response.status === 401) {
            window.location.href = "login.html";
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("loading").style.display = "none";
        if (data.statusCode === 200) {
            const galleryContainer = document.getElementById("gallery");

            Object.keys(data.body).forEach(username => {
                const userHeading = document.createElement("h3");
                userHeading.textContent = username;
                galleryContainer.appendChild(userHeading);

                const audioContainer = document.createElement("div");
                audioContainer.className = "audio-container";
                galleryContainer.appendChild(audioContainer);

                const audioFiles = data.body[username];
                audioFiles.forEach((audioUrl) => {
                    const audioElement = document.createElement("audio");
                    audioElement.controls = true;
                    audioElement.src = audioUrl.replace(/https?:\/\/[^\/]+/, "http://127.0.0.1:4566");
                    audioContainer.appendChild(audioElement);
                });
            });
        }
    })
    .catch(error => console.error("Error fetching music:", error));
