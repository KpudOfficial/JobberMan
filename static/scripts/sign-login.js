let signupBtn = document.getElementById('signup-btn');
let forms = document.querySelector('.forms');

let login = document.getElementById('login');
let signup = document.getElementById('signup');
let loginLink = document.getElementById('login-link');
let signupLink = document.getElementById('signup-link');
let newAccount = document.querySelector('.new-account');

loginLink.addEventListener('click',()=>{
    login.classList.add('active');
    signup.classList.remove('active');
});
signupLink.addEventListener('click',()=>{
    signup.classList.add('active');
    login.classList.remove('active');
});

signupBtn.addEventListener('click',(e)=>{
    e.preventDefault();
    forms.classList.add('non-active');
    newAccount.style.display = 'block';
    //e.preventDefault()==false;
});