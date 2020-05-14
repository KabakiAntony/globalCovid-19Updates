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
            document.getElementById('cases-upload-feedback').innerText = "File upload successful";
        }
        else if (status === 401)
        {
            //document.getElementById('error').innerText = error;
        }
        else if(status === 404){
            //document.getElementById('email-error').innerText = error;
        }
        else{
            console.log(error,status);
        }    
    })
    .catch(err => console.log(err,'here is the error'));

});
//upload countries data to the db on submit
countryForm.addEventListener('countrySubmit',(e)=>{
    e.preventDefault();

});