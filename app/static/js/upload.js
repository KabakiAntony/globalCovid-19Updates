const casesForm = document.getElementById('cases-data');
const countryForm = document.getElementById('country-data');
const caseFile = document.getElementById('caseFile');
const countryFile = document.getElementById('country-file');
token = localStorage.getItem('user');

casesForm.addEventListener('submit',(e)=>{
    e.preventDefault();

    const form_data = new FormData();
    form_data.append('csvFile',caseFile.files[0]);

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
            document.getElementById('cases-upload-feedback').innerText = error;
        }
        else{
            console.log(error,status);
            document.getElementById('cases-upload-feedback').innerText = error;
        }    
    })
    .catch(err => console.log(err));
});