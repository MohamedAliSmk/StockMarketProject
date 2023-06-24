
let upbutton = document.getElementById("up");

window.onscroll = function(){
    if(window.scrollY >= 2000){
        //console.log(` scrolling Y value is ${ window.scrollY} `);
        upbutton.style.display='block';
    }else{
        upbutton.style.display='none';
    }
};

upbutton.onclick = function(){
    window.scrollTo({
        left:0,
        top:0,
        behavior:"smooth"
    });
};