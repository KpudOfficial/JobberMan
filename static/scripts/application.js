document.querySelectorAll('.nav-item').forEach(item=>{
    item.style.display = 'none';
});

let logo = document.querySelector('.nav-item');
logo.style.display = 'block';
logo.style.marginBottom = '0%';

logo.addEventListener('click',()=>{
    window.location.href = "/index";
});

applyButton = document.querySelector('#apply-button');
function loadForm(){
    document.querySelector('#job-application').style.display = 'block';
    document.querySelector('#job-info').style.display = "none";
    document.querySelector('.load-form').style.display = 'none';
        document.querySelector('.load-form').style.zIndex = '999';
        document.querySelector('.load-form').style.animationPlayState = 'pause';
}
function loadAnimation(){
        document.querySelector('.load-form').style.display = 'block';
        document.querySelector('.load-form').style.zIndex = '999';
        document.querySelector('.load-form').style.animationPlayState = 'running';
    }
applyButton.addEventListener('click',()=>{
    setTimeout(loadAnimation,1000);
    setTimeout(loadForm,4000);


    // clearTimeout(to1)
    // clearTimeout(to2)
});

