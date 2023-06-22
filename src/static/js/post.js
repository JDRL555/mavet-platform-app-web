const close_btn   = document.querySelector(".close_btn")
const file        = document.querySelector(".file")
const form_bg     = document.querySelector(".form_bg")
const create_post = document.querySelector(".create_post")

form_bg.style.opacity = 0

create_post.addEventListener("click", () => {
  const form_bg  = document.querySelector(".form_bg")
  form_bg.style.visibility = "visible"
  form_bg.style.opacity = 1
}) 

close_btn.addEventListener("click", () => {
  const form_bg  = document.querySelector(".form_bg")
  const form     = document.querySelector("form")
  const filename      = document.querySelector(".filename")
  form_bg.style.opacity = 0
  filename.innerHTML    = ""
  form.reset()
  setTimeout(()=>form_bg.style.visibility = "hidden", 500)
})

file.addEventListener("change", () => {
  const inputFile     = document.querySelector(".file")
  const filename      = document.querySelector(".filename")
  filename.innerHTML  = `Imagen seleccionada: ${inputFile.value}`
})