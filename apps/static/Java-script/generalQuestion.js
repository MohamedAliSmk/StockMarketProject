// const btn = document.querySelectorAll(".questionBtn");
// btn.forEach(function(btn){
//     btn.addEventListener("click",function(e){
//         //console.log(e.currentTarget);
//         const question = e.currentTarget.parentElement.parentElement;
//         question.classList.toggle("showText");
//     })
// });


const questions = document.querySelectorAll(".question");
questions.forEach(function(question){
    const btn = question.querySelector(".questionBtn");
    btn.addEventListener("click",function(){
        questions.forEach(function(item){
            if(item !== question ){
                item.classList.remove(".showText");
                
            }
            
    });
    question.classList.toggle("showText");
    });
});





