const reviews = [{
    id:1,
    name:"susan smith",
    job: "web developer",
    img:"./bo.avif",
    text:" im baby meggings twee health goth +1. Bicycle rights tumeric chartreuse before they sold out chambray pop-up.Shaman humblebrag picked coloing book salvia hoodie, cold-pressed four dollar toast everyday carry",
},
{
    id:2,
    name:"Bill Anderson",
    job: "THE BOSS",
    img:"/images/activity-02.png",
    text:" Edison bulb put a bird on it humblebrag, marfa pok pok heirloom fashion axe cray stumptown venmo actually seitan. VHS farm-to-table schlitz, edison bulb pop-up 3 wolf moon tote bag street art shabby chic. ",
},
{
    id:3,
    name:"anna johnson",
    job: "web designer",
    img:".",
    text:"Helvetica artisan kinfolk thundercats lumbersexual blue bottle. Disrupt glossier gastropub deep v vice franzen hell of brooklyn twee enamel pin fashion axe.photo booth jean shorts artisan narwhal.",
},
{
    id:4,
    name:"Peter Jones",
    job: " INTERN ",
    img:"",
    text:" Sriracha literally flexitarian irony, vape marfa unicorn. Glossier tattooed 8-bit, fixie waistcoat offal activated charcoal slow-carb marfa hell of pabst raclette post-ironic jianbing swag. ",  
},
];


/// select items
const personimg = document.getElementById("personimg");
const  autor  = document.getElementById("autor");
const  job    = document.getElementById("jop");
const  info   = document.getElementById("info");

const prevbtn =  document.querySelector(".prev-btn");
const nextbtn = document.querySelector(".next-btn");
const randombtn = document.querySelector(".random-btn");

/// det starting item 
let curentItem = 0;

///  load  initial item 
window.addEventListener("DOMContentLoaded", function(){
    showPerson();
});

// show person based on item 
function showPerson(){
    const item = reviews[curentItem];
    personimg.src = item.img ;
    autor.textContent = item.name;
    job.textContent = item.job;
    info.textContent = item.text;
}

/// show  next person 
nextbtn.addEventListener("click",function(){
    curentItem ++;
    if(curentItem > reviews.length -1 ){
        curentItem = 0;
    }
    showPerson();
});

/// show  previous btn 
prevbtn.addEventListener("click",function(){
    curentItem --;
    if(curentItem < 0 ){
        curentItem = reviews.length -1;
    }
    showPerson();
});

/// show  random person 
randombtn.addEventListener("click",function(){
    curentItem = Math.floor(Math.random() * reviews.length);
    showPerson();

});