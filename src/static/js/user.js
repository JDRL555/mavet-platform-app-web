const user_img = document.querySelector(".user_img")

function userOptionsHandler(){
  const userOptions = document.querySelector(".subnav")
  if(userOptions.style.opacity == 0){
    userOptions.style.visibility = "visible"
    userOptions.style.opacity = 1
  }else{
    userOptions.style.opacity = 0
    setTimeout(() => userOptions.style.visibility = "hidden", 500)
  }   
}

user_img.addEventListener("click", userOptionsHandler)