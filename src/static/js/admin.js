const btns            = document.querySelectorAll(".admin_option") // opciones del admin
const request_option  = document.querySelector(".request_option") // ver publicaciones solicitadas
const modal_bg        = document.querySelector(".modal_bg") // ventana para mostrar registros

request_option.addEventListener("click", () => window.location = "/post/request")

//recorre las entidades que el administrador puede manipular (usuarios, eventos, cursos y categorias)
for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", async () => {
    
    let from = ""
    if(i == 0 ) from = "Usuarios" 
    if(i == 1 ) from = "Eventos" 
    if(i == 2 ) from = "Cursos" 
    if(i == 3 ) from = "Categorias" 
    
    const response  = await fetch("/modal", {
      method: "POST",
      body: JSON.stringify(from),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })

    let modal     = await response.text()
    const parser  = new DOMParser()

    modal         = parser.parseFromString(modal, "text/html")
    modal         = modal.body.querySelector(".modal")
    
    modal.style.width = "auto" 
    modal_bg.appendChild(modal)

    modal.style.transform       = "translateY(0px)"
    modal_bg.style.opacity      = 1
    modal_bg.style.visibility   = "visible"

    if(!modal.querySelector(".modal_content")){
      modal.querySelector(".modal_filters").remove()
      const empty       = document.createElement("h1")
      const create_btn  = document.createElement("button")
      const table       = document.createElement("table")
      const tbody       = document.createElement("tbody")

      table.appendChild(tbody)

      create_btn.setAttribute("class", "create_col")
      create_btn.innerText = "Crear"

      empty.innerHTML = "No hay registros aun"
      empty.style.textAlign = "center"

      modal.appendChild(empty)
      modal.appendChild(create_btn)

      create_operation(table, modal, create_btn, from)
    }else{
      const table       = modal.querySelector(".modal_content")
      let edit_btn      = table.querySelectorAll(".edit_col")
      let delete_btn    = table.querySelectorAll(".delete_col")
      let create_btn    = table.querySelector(".create_col")
      let rows          = table.querySelectorAll(".register_rows")
  
      if(modal.querySelector(".modal_filters")){
        const search_btn    = modal.querySelector(".search_btn")
        const filter        = modal.querySelector(".filter")
        let filter_value    = modal.querySelector(".filter_value")
        let filter_selected = filter.options[0].value
  
        filter.addEventListener("change", ()=>filter_selected = filter.options[filter.selectedIndex].value)
  
        search_btn.addEventListener("click", async () => {
          let data = {filter_selected, filter_value: filter_value.value}
          const response = await fetch("/users/filter", {
            method: "POST",
            body: JSON.stringify(data),
            mode: "cors",
            headers: {
              "Content-Type": "application/json",
            },
          })
  
          let new_table   = await response.text()
  
          const parser    = new DOMParser()
          const old_table = modal.querySelector(".modal_content") 
          new_table       = parser.parseFromString(new_table, "text/html")
          new_table       = new_table.body.querySelector(".modal_content")
          
          if(new_table.querySelector(".register_rows")){
            old_table.parentNode.replaceChild(new_table, old_table)
    
            rows        = new_table.querySelectorAll(".register_rows")
            edit_btn    = new_table.querySelectorAll(".edit_col")
            delete_btn  = new_table.querySelectorAll(".delete_col")
            create_btn  = new_table.querySelector(".create_btn") 
    
            edit_operation(new_table, rows, edit_btn, delete_btn, from)
            delete_operation(new_table, delete_btn, from)
            create_operation(new_table, modal, create_btn, from)
          }else{
            const notFound            = document.createElement("h1")
  
            notFound.innerHTML        = "Usuarios no encontrados:/"
            notFound.style.textAlign  = "center"
            notFound.setAttribute("class", "modal_content")
  
            old_table.parentNode.replaceChild(notFound, old_table)
          }
        })
      }
      edit_operation(table, rows, edit_btn, delete_btn, from)
      delete_operation(table, delete_btn, from)
      create_operation(table, modal, create_btn, from)
    }
    const close_btn = modal.querySelector(".close_btn")
    
    close_btn.addEventListener("click", () => {
      modal.style.transform   = "translateY(-200px)"
      modal_bg.style.opacity  = 0
      setTimeout(() => {
        modal_bg.style.visibility = "hidden"
        modal_bg.innerHTML        = ""
      }, 350)
    })  
    
  })
}