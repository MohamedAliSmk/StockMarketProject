
let tex= document.querySelectorAll(".finance-education li ");
//let texArray = Array.from(tex);
//console.log(texArray);
let content  = document.querySelectorAll(".community-content > div");
//let community = document.querySelector(".community");
//console.log(content);
//   console.log(tex);

tex.forEach((ele) => {
    ele.addEventListener("click",function(e){
        //console.log(e);
        tex.forEach((ele)=>{
            ele.classList.remove("activee");
        });
        e.currentTarget.classList.add("activee");
        content.forEach((div) => {
            div.style.display='none';
        });
        //console.log(e.currentTarget.dataset.cont);
        document.querySelector(e.currentTarget.dataset.cont).style.display='block';
        //document.querySelector(e.currentTarget.dataset.cont).style.display='block';
    });
});


// tex.forEach(function(ele){
//     ele.onclick= function(){
//         tex.forEach(function(ele){
//             ele.classList.remove("activee");
//         });
//         this.classList.add("activee"); 
//     };
// });
