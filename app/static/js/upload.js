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
        // headers : {'Authorization':'Bearer '+ token},
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

