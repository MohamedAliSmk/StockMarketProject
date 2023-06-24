
let company= document.querySelectorAll(".allEllement li ");
//let texArray = Array.from(tex);
//console.log(texArray);
let companycontent  = document.querySelectorAll(".theChildContent > div");
//let community = document.querySelector(".community");
//console.log(content);
//   console.log(tex);

company.forEach((ele) => {
    ele.addEventListener("click",function(e){
        //console.log(e);
        company.forEach((ele)=>{
            ele.classList.remove("activee");
        });
        e.currentTarget.classList.add("activee");
        companycontent.forEach((div) => {
            div.style.display='none';
        });
        //console.log(e.currentTarget.dataset.cont);
        document.querySelector(e.currentTarget.dataset.cont).style.display='block';
        //document.querySelector(e.currentTarget.dataset.cont).style.display='block';
    });
});
