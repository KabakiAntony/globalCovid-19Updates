function formatNumber(num) {
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
  }


fetch('https://globalcovid19updates.herokuapp.com/global')
.then(response=>response.json())
.then(({data,status,error})=>{
    if(status === 200){
        document.getElementById('global-summary').innerHTML=`
        <h4>Last update : ${data[0].asAt}</h4>
        ${data.map(function(globalSummary){
            return `
            <label>Total confirmed cases</label>
            <p id="confirmed-cases">${formatNumber(globalSummary.confirmedCases)}</p>
            <label>Active cases</label>
            <p id="active-cases">${formatNumber(globalSummary.activeCases)}</p>
            <label>Recoveries</label>
            <p id="recoveries">${formatNumber(globalSummary.Recoveries)}</p>
            <label>Deaths</label>
            <p id="deaths">${formatNumber(globalSummary.Deaths)}</p>
            `
        }).join('')}
        `
        }
    else{
        console.log(error, status)
    }
})
.catch((err)=>{
    console.log(err)

});
fetch('https://globalcovid19updates.herokuapp.com/global/summary')
.then(response=>response.json())
.then(({data,status,error})=>{
    if(status === 200){
        document.getElementById('show-updates').innerHTML=`
        <table class="holder">
            <tr>
            <th>Country</th>
            <th>Confirmed Cases</th>
            <th>Active Cases</th>
            <th>Recoveries</th>
            <th>Deaths</th>
            </tr>
            
            </table>
        ${data.map(function(globalData){
            return `
            <table class="holder">
            <tr>
            <td id="td-country">${globalData.country}</td>
            <td id="td-confirmed-cases">${formatNumber(globalData.confirmedCases)}</td>
            <td id="td-active-cases">${formatNumber(globalData.activeCases)}</td>
            <td id="td-recoveries">${formatNumber(globalData.Recoveries)}</td>
            <td id="td-deaths">${formatNumber(globalData.Deaths)}</td>
            </tr>
            
            </table>
            `
        }).join('')}
        `
        

    }
    else{
        console.log(error, status)
    }
})
.catch((err)=>{
    console.log(err)

});