function uploadMusic(e) {
    e.preventDefault();
    const musicFile = document.getElementById("music").files[0];
    const formData = new FormData();
    formData.append("music", musicFile);

    fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${localStorage.getItem("token")}`
        },
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.status != 200) {
                alert(data.body);
            } else {
                alert("Music uploaded successfully");
            }
            window.location.href = "gallery.html";
        })
        .catch(error => {
            console.error("Error uploading music:", error);
            alert("Error uploading music");
        });
}
