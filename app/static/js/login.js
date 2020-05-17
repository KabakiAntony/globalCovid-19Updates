// this will handle login
let email = document.getElementById('email')
let password = document.getElementById('password')
let submitForm = document.getElementById('login')

submitForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    signInData ={
        email:email.value,
        password:password.value
    }
    login(signInData);
});
function login(signInData){
    fetch(`/auth/admin/signin`,{
    method : 'POST',
    headers :{
        'Content-Type': 'application/json',
    },
    body:JSON.stringify(signInData)
})
.then(response => response.json())
.then(({data,status,error}) => {
    if (status === 200){
        localStorage.setItem('user',data);
        callToast();
        location.href='/auth/admin/upload?in='+data;
    }
    else if (status === 401)
    {
        document.getElementById('error').innerText = error;
    }
    else if(status === 404){
        document.getElementById('email-error').innerText = error;
    }
    else{
        cosole.log(error,status);
    }    
})
.catch(err => console.log(err));
}
function callToast() {
    var snackbar = document.getElementById("login-success");
    snackbar.className = "show";
    setTimeout(function(){ snackbar.className = snackbar.className.replace("show", ""); }, 3000);
}
