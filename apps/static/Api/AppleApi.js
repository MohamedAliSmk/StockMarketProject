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
    postData(`https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=57dbaca8774ef5359da35c985a6e5433`, { answer: 42 }).then((data) => {
    console.log(data); // JSON data parsed by `data.json()` call
    data.forEach( function(element,index,array) {
        // if(element.calendarYear=="2018"){
        //     console.log(element);
        // }
        // console.log(element);
        // console.log(element.calendarYear);
    });
    let ulstyle = document.querySelector(".companyContent");
    
    console.log(ulstyle);
    
    let acceptedDate = `<li> acceptedDate :  ${data[0].acceptedDate} </li>`;
    let calendarYear = `<li> calendarYear :  ${data[0].calendarYear} </li>`;
    let cik = `<li> cik :  ${data[0].cik} </li>`;
    let costAndExpenses = `<li> costAndExpenses : ${data[0].costAndExpenses} </li>`;
    let costOfRevenue = `<li> costOfRevenue :  ${data[0].costOfRevenue} </li>`;
    let date = `<li> date :  ${data[0].date} </li>`;
    let depreciationAndAmortization = `<li> depreciationAndAmortization :  ${data[0].depreciationAndAmortization} </li>`;
    let ebitda = `<li> ebitda :  ${data[0].ebitda} </li>`;
    let ebitdaratio = `<li> ebitdaratio :  ${data[0].ebitdaratio} </li>`;
    let eps = `<li> eps :  ${data[0].eps} </li>`;
    let epsdiluted = `<li> epsdiluted :  ${data[0].epsdiluted} </li>`;
    let fillingDate = `<li> fillingDate :  ${data[0].fillingDate} </li>`;
    let finalLink = `<li> finalLink :  ${data[0].finalLink} </li>`;
    let generalAndAdministrativeExpenses =  `<li> generalAndAdministrativeExpenses :  ${data[0].generalAndAdministrativeExpenses} </li>`;
    let grossProfit = `<li> grossProfit :  ${data[0].grossProfit} </li>`;
    let grossProfitRatio  = `<li>grossProfitRatio :  ${data[0].grossProfitRatio} </li>`;
    let incomeBeforeTax =  `<li> incomeBeforeTax :  ${data[0].incomeBeforeTax} </li>`;
    let incomeBeforeTaxRatio =  `<li> incomeBeforeTaxRatio :  ${data[0].incomeBeforeTaxRatio} </li>`;
    let incomeTaxExpense = `<li> incomeTaxExpense :  ${data[0].incomeTaxExpense} </li>`;

    let interestExpense = `<li> interestExpense :  ${data[0].interestExpense} </li>`;
    let  interestIncome= `<li> interestIncome :  ${data[0].interestIncome} </li>`;
    let link = `<li> link :  ${data[0].link} </li>`;
    let netIncome = `<li> netIncome :  ${data[0].netIncome} </li>`;
    let netIncomeRatio = `<li> netIncomeRatio :  ${data[0].netIncomeRatio} </li>`;

    let operatingExpenses = `<li> operatingExpenses :  ${data[0].operatingExpenses} </li>`;
    let operatingIncome = `<li> operatingIncome :  ${data[0].operatingIncome} </li>`;
    let operatingIncomeRatio = `<li> operatingIncomeRatio :  ${data[0].operatingIncomeRatio} </li>`;
    let otherExpenses = `<li> otherExpenses :  ${data[0].otherExpenses} </li>`;

    let period = `<li>  period :  ${data[0].period} </li>`;
    let reportedCurrency = `<li> reportedCurrency :  ${data[0].reportedCurrency} </li>`;
    let researchAndDevelopmentExpenses = `<li> researchAndDevelopmentExpenses :  ${data[0].researchAndDevelopmentExpenses} </li>`;
    let  revenue = `<li> revenue :  ${data[0].revenue} </li>`;
    let sellingAndMarketingExpenses = `<li> sellingAndMarketingExpenses :  ${data[0].sellingAndMarketingExpenses} </li>`;
    let sellingGeneralAndAdministrativeExpenses = `<li> sellingGeneralAndAdministrativeExpenses :  ${data[0].sellingGeneralAndAdministrativeExpenses} </li>`;
    
    let symbol = `<li>symbol  :  ${data[0].symbol } </li>`;
    let totalOtherIncomeExpensesNet = `<li> totalOtherIncomeExpensesNet :  ${data[0].totalOtherIncomeExpensesNet} </li>`;
    let weightedAverageShsOut = `<li> weightedAverageShsOut :  ${data[0].weightedAverageShsOut} </li>`;
    let weightedAverageShsOutDil = `<li> weightedAverageShsOutDil :  ${data[0].weightedAverageShsOutDil} </li>`;






    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',acceptedDate);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',calendarYear);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',cik);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',costAndExpenses);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',costOfRevenue);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',date);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',depreciationAndAmortization);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',ebitda);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',ebitdaratio);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',eps);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',epsdiluted);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',fillingDate);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',finalLink);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',generalAndAdministrativeExpenses);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',grossProfit);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',grossProfitRatio);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',incomeBeforeTax);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',incomeBeforeTaxRatio);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',incomeTaxExpense);

    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',interestExpense);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',interestIncome);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',link);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',netIncome);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',netIncomeRatio);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',operatingExpenses);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',operatingIncome);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',operatingIncomeRatio);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',otherExpenses);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',period);

    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',reportedCurrency);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',researchAndDevelopmentExpenses);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend', revenue);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',sellingAndMarketingExpenses);

    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',sellingGeneralAndAdministrativeExpenses);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',symbol);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',totalOtherIncomeExpensesNet);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',weightedAverageShsOut);
    document.querySelector('.companyContent').insertAdjacentHTML('beforeend',weightedAverageShsOutDil);

});

//let apibutton = document.querySelector(".api");
//console.log(apibutton);
