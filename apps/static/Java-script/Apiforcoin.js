let egyrateele = document.querySelector(".egyrate");
let egyratedateele = document.querySelector(".egyratedate");
let baseoneele = document.querySelector(".basetwo");


let usdrateele = document.querySelector(".usdrate");
let usdratedateele = document.querySelector(".usdratedate");
let basetwoele = document.querySelector(".baseone");

let raerateele = document.querySelector(".raerate");
let rawratedateele = document.querySelector(".rawratedate");
let basethreeele = document.querySelector(".basethree");




let qarrateelement  = document.querySelector(".qarrate");
let qarratedateelement = document.querySelector(".qarratedate");
let qarbaseelement = document.querySelector(".qarbase");

let kwdrateelement = document.querySelector(".kwdrate");
let kwdratedateelement = document.querySelector(".kwdratedate");
let kwdbaseelement = document.querySelector(".kwdbase");

let eurrateelement = document.querySelector(".eurrate");
let eurratedateelement = document.querySelector(".eurratedate");
let eurbaseelement = document.querySelector(".eurbase");


fetch("https://api.currencyfreaks.com/v2.0/rates/latest?apikey=1493891aa6f34902aeaa75981dce0424").then((result)=>{
    //console.log(result);
    let myData = result.json();
    return myData;
}).then((currency) => {
    //console.log(currency.rates);
    //console.log(currency.rates["EGP"]);
    let egyrate = currency.rates["EGP"];
    egyrateele.innerHTML = ` price is : ${egyrate}`;
    let egyratedate= currency.date;
    egyratedateele.innerHTML= ` Date : ${egyratedate}`;
    let baseone = currency.base;
    baseoneele.innerHTML = `Based : ${baseone}`;


    let usdrate = currency.rates["USD"];
    usdrateele.innerHTML = ` price is :  ${usdrate}`;
    let usdratedate = currency.date;
    usdratedateele.innerHTML =  ` Date : ${usdratedate} `;
    let basetwo = currency.base;
    basetwoele.innerHTML = ` Based : ${basetwo}`;

    let raerate = currency.rates["SAR"];
    raerateele.innerHTML = ` price is :  ${raerate}`;
    let rawratedate = currency.date;
    rawratedateele.innerHTML =  ` Date : ${rawratedate} `;
    let basethree = currency.base;
    basethreeele.innerHTML = ` Based : ${basethree}`;

    let qarrate = currency.rates["QAR"];
    qarrateelement.innerHTML = `price is ${qarrate}`;
    let qardate = currency.date;
    qarratedateelement.innerHTML = `data : ${qardate}`;
    let qarbase = currency.base;
    qarbaseelement.innerHTML = `Base  :${qarbase}`;


    let kwdrate = currency.rates["KWD"];
    kwdrateelement.innerHTML = `price ${kwdrate}`;
    let kwdratedate = currency.date;
    kwdratedateelement.innerHTML = `Date : ${kwdratedate}`;
    let kwdbase = currency.base;
    kwdbaseelement.innerHTML = `Base : ${kwdbase}`;


    let eurrate = currency.rates["EUR"];
    eurrateelement.innerHTML = `price is ${eurrate}`;
    let eurdate = currency.date;
    eurratedateelement.innerHTML = ` Date ${eurdate} `;
    let eurbase = currency.base;
    eurbaseelement.innerHTML = `Base: ${eurbase}`;

    //console.log(currency.date);
    //console.log(currency.rates["SAR"]);
});


///https://api.currencyfreaks.com/v2.0/rates/latest?apikey=77ab61e52437433d8757b9cb121dff1cdh