function openLoginPopup() {
    document.getElementById('loginPopup').style.display = 'block';
}


document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();

    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    if (login === "admin" && senha === "admin") {
        alert("Acesso liberado!");
        closeLoginPopup();
        window.location.href = "home.html";
    } else {
        alert("Acesso negado! Verifique seu usuário e senha.");
    }
});

window.addEventListener('load', function () {
    var notification = document.getElementById('notification');
    notification.style.display = 'block';
});
