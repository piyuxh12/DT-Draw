function startDraw() {
    let name = document.getElementById("name").value;
    let phone = document.getElementById("phone").value;

    if (name && phone) {
        fetch('/lucky_draw', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, phone })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = `Congratulations ${name}! You won a ${data.prize}.`;
        });
    } else {
        alert("Please enter your name and phone number.");
    }
}
