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

let page = 0
window.onscroll = async () => {
  const totalPageHeight = document.body.scrollHeight
  const scrollPoint     = (window.scrollY + window.innerHeight) - 120
  page+=5
  if(scrollPoint >= totalPageHeight){
    let response = await fetch("/post", {
      method: "POST",
      body: JSON.stringify(page),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
    
    if(response) {
      let posts     = await response.text()
      const parser  = new DOMParser()
      posts         = parser.parseFromString(posts, "text/html")
      posts         = posts.body.querySelectorAll(".post")
      const posts_container = document.querySelector(".posts_container")
      for (let i = 0; i < posts.length; i++) {
        posts_container.appendChild(posts[i]) 
      }
    }
  }
}