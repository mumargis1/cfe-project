const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`

    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)

    console.log(loginObjectData, bodyStr)

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err =>{
        console.log('err', err)
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access )
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML="<pre>"+ JSON.stringify(data) + "<pre>"
    }
}
function getProductList() {
    const endpoint = `${baseEndpoint}/products/`
    const options = {
        method : "GET",
        headers : {
            "Content-Type": "application/json"
        }
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
        writeToContainer(data)
    })
}
