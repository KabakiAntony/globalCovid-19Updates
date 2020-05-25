fetch('https://globalcovid19updates.herokuapp.com/global/summary')
.then(response=>response.json())
.then(({data,status,error})=>{
    if(status === 200){
        console.log(data)
        document.getElementById('show-updates').innerHTML=`
        Covid-19 numbers as at ${data[0].asAt}
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
            <td>${globalData.country}</td>
            <td>${globalData.confirmedCases}</td>
            <td>${globalData.activeCases}</td>
            <td>${globalData.Recoveries}</td>
            <td>${globalData.Deaths}</td>
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