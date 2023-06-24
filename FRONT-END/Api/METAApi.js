// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      //mode: "cors", // no-cors, *cors, same-origin
      //cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      //credentials: "same-origin", // include, *same-origin, omit
        headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
    },
      //redirect: "follow", // manual, *follow, error
      //referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      //body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
    }
    // 8263508c794d9fc6c347f4670860b1a8  NEW api key 
    // 57dbaca8774ef5359da35c985a6e5433
    postData(`https://financialmodelingprep.com/api/v3/income-statement/META?limit=120&apikey=8263508c794d9fc6c347f4670860b1a8`, { answer: 42 }).then((data) => {
    console.log(data); // JSON data parsed by `data.json()` call
    data.forEach( function(element,index,array) {
        //if(element.calendarYear=="2018"){
            console.log(element);
        //}
        // console.log(element);
        // console.log(element.calendarYear);
    });
});

//let apibutton = document.querySelector(".api");
//console.log(apibutton);
