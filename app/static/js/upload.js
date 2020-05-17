const casesForm = document.getElementById('cases-data');
const caseFile = document.getElementById('caseFile');
const countryForm = document.getElementById('country-data');
const countryFile = document.getElementById('countryFile');

token = localStorage.getItem('user');

casesForm.addEventListener('submit',(e)=>{
    e.preventDefault();

    const form_data = new FormData();
    form_data.append('caseCsv',caseFile.files[0]);

    fetch(`/auth/admin/upload/cases?in=`+token,{
        method : 'POST',
        body:form_data
    })
    .then(response => response.json())
    .then(({data,status,error}) => {
        if (status === 200){
            console.log(data);
            document.getElementById('cases-upload-feedback').innerText = data;
        }
        else if (status === 401)
        {
            console.log(error,status);
            document.getElementById('cases-upload-feedback').innerText = error;
        }
        else{
            console.log(error,status);
            document.getElementById('cases-upload-feedback').innerText = error;
        }    
    })
    .catch((err) => {
        console.log(err)
        document.getElementById('cases-upload-feedback').innerText = err;
    });
});

countryForm.addEventListener('submit',(e)=>{
    e.preventDefault();

    const country_data = new FormData();
    country_data.append('countryCsv',countryFile.files[0]);

    fetch(`/auth/admin/upload/country?in=`+token,{
        method : 'POST',
        body:country_data
    })
    .then(response => response.json())
    .then(({data,status,error}) => {
        if (status === 200){
            console.log(data)
            document.getElementById('cases-upload-feedback').innerText = data;
        }
        else if (status === 401)
        {
            console.log(error)
            document.getElementById('cases-upload-feedback').innerText = error+''+status;
        }
        else{
            console.log(error)
            document.getElementById('cases-upload-feedback').innerText = error +''+status;
        }    
    })
    .catch((err) => {
        console.log(err)
        document.getElementById('cases-upload-feedback').innerText = err + "unknown error";

    });
});
