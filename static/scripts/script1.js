let subMenu1 = document.querySelector('.sub-menu1');
let subMenu2 = document.querySelector('.sub-menu2');

subMenu1.addEventListener('click',()=>{
    if(document.querySelector('.dropdown-1').style.display === 'none'){
        document.querySelector('.dropdown-1').style.display = 'block';
        document.querySelector('.dropdown-2').style.display = 'none'
    }else{
        document.querySelector('.dropdown-1').style.display = 'none';
    }
});
subMenu2.addEventListener('click',()=>{
    if(document.querySelector('.dropdown-2').style.display === 'none'){
        document.querySelector('.dropdown-2').style.display = 'block';
        document.querySelector('.dropdown-1').style.display = 'none'
    }else{
        document.querySelector('.dropdown-2').style.display = 'none';
    }
});

let jobAtts = document.querySelectorAll('.attributes');
jobAtts.forEach(jobAtt=>{
    console.log(jobAtt.dataset.mode);
});