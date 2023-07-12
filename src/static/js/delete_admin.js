// se encarga de cubrir las opciones de eliminar los registros
function delete_operation(table, delete_btn, from){
  for(let d = 0; d < delete_btn.length; d++){
    delete_btn[d].addEventListener("click", () => {
      const rows        = table.querySelectorAll(".register_rows")
      const id          = rows[d].querySelector("td")
      const modal_bg    = document.createElement("div")
      const warning     = document.createElement("div")
      const title       = document.createElement("h1")
      const accept_btn  = document.createElement("button")
      const cancel_btn  = document.createElement("button")
      const body        = document.querySelector("body")
      
      modal_bg.setAttribute("class", "modal_bg")
      warning.setAttribute("class", "modal")
      
      title.innerText       = `Seguro de eliminar el usuario con el id ${id.innerText}?` 
      title.style.padding   = "20px"

      accept_btn.setAttribute("class", "accept_btn")
      cancel_btn.setAttribute("class", "cancel_btn")

      accept_btn.innerText  = "Aceptar"
      cancel_btn.innerText  = "Cancelar"
      
      warning.appendChild(title)
      warning.appendChild(accept_btn)
      warning.appendChild(cancel_btn)

      warning.style.margin      = 0
      warning.style.transform   = "translateY(0px)"
      warning.style.width       = "auto"
      warning.style.height      = "auto"

      modal_bg.style.justifyContent = "center"
      modal_bg.style.alignItems     = "center"
      modal_bg.style.visibility     = "visible"
      modal_bg.style.opacity        = 1
      modal_bg.style.zIndex         = 200
      
      modal_bg.appendChild(warning)
      body.appendChild(modal_bg)

      accept_btn.addEventListener("click", () => {
        let route = ""
        if(from == "Usuarios")    route = "user"
        if(from == "Eventos")     route = "event"
        if(from == "Cursos")      route = "course"
        if(from == "Categorias")  route = "category"

        window.location.href = `/${route}/delete?id=${id.innerHTML}`
      })

      cancel_btn.addEventListener("click", () => {
        warning.style.transform   = "translateY(-200px)"
        modal_bg.style.opacity  = 0
        setTimeout(() => {
          modal_bg.style.visibility = "hidden"
          modal_bg.innerHTML        = ""
        }, 350)
      })
    })
  }
}