const sidebar_bg    = document.querySelector(".sidebar_bg")

const open_sidebar  = document.querySelector(".open_sidebar")
const close_sidebar = document.querySelector(".close_sidebar") 

sidebar_bg.style.opacity = 0

function openSideBar(){
  const sidebar_bg  = document.querySelector(".sidebar_bg")
  const sidebar     = document.querySelector(".sidebar")
  sidebar_bg.style.visibility = "visible"
  sidebar_bg.style.opacity = 1
  sidebar.style.transform = "translateX(0%)"
}

function closeSideBar(){
  const sidebar_bg  = document.querySelector(".sidebar_bg")
  const sidebar     = document.querySelector(".sidebar")
  sidebar_bg.style.opacity = 0
  sidebar.style.transform = "translateX(100%)"
  setTimeout(()=>sidebar_bg.style.visibility = "hidden", 500)
}

open_sidebar.addEventListener("click", openSideBar)
close_sidebar.addEventListener("click", closeSideBar)