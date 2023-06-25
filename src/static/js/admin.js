const btns            = document.querySelectorAll(".admin_option")
const request_option  = document.querySelector(".request_option")
const modal_bg        = document.querySelector(".modal_bg")

request_option.addEventListener("click", () => window.location = "/post/request")

function edit_delete_operations(i, table, rows, edit_btn, delete_btn, from){
  for(let e = 0; e < edit_btn.length; e++){
    edit_btn[e].addEventListener("click", () => {
      const cols          = rows[e].querySelectorAll(".register_cols")
      const save_btn      = document.createElement("td")
      const cancel_btn    = document.createElement("td")
      const original_cols = []

      save_btn.setAttribute("class", "save_btn")
      cancel_btn.setAttribute("class", "cancel_btn")
      
      save_btn.innerText    = "Guardar"
      cancel_btn.innerText  = "Cancelar"
      
      for (let c = 1; c < cols.length; c++) {
        let input = document.createElement("input")
        
        if(i == 6 || i == 7){
          input = document.createElement("select")
        }

        original_cols.push(cols[c].innerHTML)
        
        input.value = cols[c].innerHTML

        cols[c].innerHTML = ""
        cols[c].appendChild(input)
      }

      edit_btn[e].parentNode.replaceChild(save_btn, edit_btn[e])
      delete_btn[e].parentNode.replaceChild(cancel_btn, delete_btn[e])

      cancel_btn.addEventListener("click", () => { 
        edit_btn[e]    = document.createElement("td")
        delete_btn[e]  = document.createElement("td")

        edit_btn[e].setAttribute("class", "edit_col")
        delete_btn[e].setAttribute("class", "delete_col")
        
        edit_btn[e].innerText = "Editar"
        delete_btn[e].innerText = "Eliminar"

        save_btn.parentNode.replaceChild(edit_btn[e], save_btn)
        cancel_btn.parentNode.replaceChild(delete_btn[e], cancel_btn)

        original_cols.forEach((col, c) => cols[c + 1].innerHTML = col)
      })
    })

  }

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
      
      title.innerText = `Seguro de eliminar el usuario con el id ${id.innerText}?` 
      accept_btn.innerText = "Aceptar"
      cancel_btn.innerText = "Cancelar"
      
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
      
      console.log(id.innerHTML, from) 
    })
  }
}

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

    const table       = modal.querySelector(".modal_content")
    let edit_btn      = table.querySelectorAll(".edit_col")
    let delete_btn    = table.querySelectorAll(".delete_col")
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
        
        old_table.parentNode.replaceChild(new_table, old_table)

        rows        = new_table.querySelectorAll(".register_rows")
        edit_btn    = new_table.querySelectorAll(".edit_col")
        delete_btn  = new_table.querySelectorAll(".delete_col")

        edit_delete_operations(i, new_table, rows, edit_btn, delete_btn, from)
      })
    }
    
    edit_delete_operations(i, table, rows, edit_btn, delete_btn, from)

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