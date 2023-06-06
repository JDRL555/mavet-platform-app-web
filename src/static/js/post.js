const form_bg  = document.querySelector(".form_bg")
form_bg.style.opacity = 0

function openForm(){
  const form_bg  = document.querySelector(".form_bg")
  const form     = document.querySelector("form")
  form_bg.style.visibility = "visible"
  form_bg.style.opacity = 1
}

function closeForm(){
  const form_bg  = document.querySelector(".form_bg")
  const form     = document.querySelector("form")
  const filename      = document.querySelector(".filename")
  form_bg.style.opacity = 0
  filename.innerHTML    = ""
  form.reset()
  setTimeout(()=>form_bg.style.visibility = "hidden", 500)
}

function changeInput(){
  const inputFile     = document.querySelector(".file")
  const filename      = document.querySelector(".filename")
  filename.innerHTML  = `Imagen seleccionada: ${inputFile.value}`
}