let btn = document.querySelector('.fa-eye'); 

btn.addEventListener('click', () => {
    let inputSenha = document.querySelector('#senha'); 

    if (inputSenha.getAttribute('type') === 'password') {
        inputSenha.setAttribute('type', 'text'); 
    } else {
        inputSenha.setAttribute('type', 'password');
    }
});

function entrar() {
    let usuario = document.querySelector('#usuario');
    let userlabel = document.querySelector('#admin');

    let senha = document.querySelector('#senha');
    let senhalabel = document.querySelector('#admin');
}
