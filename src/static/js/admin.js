const btns            = document.querySelectorAll(".admin_option")
const request_option  = document.querySelector(".request_option")
const modal_bg        = document.querySelector(".modal_bg")

request_option.addEventListener("click", () => window.location = "/post/request")

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

    const table = modal.querySelector(".modal_content")
    const edit_btn = table.querySelectorAll(".edit_col")
    const delete_btn = table.querySelectorAll(".delete_col")
    
    for(let e = 0; e < edit_btn.length; e++){
      edit_btn[e].addEventListener("click", () => {
        const rows = table.querySelectorAll(".register_rows")
        const cols = rows[e].querySelectorAll(".register_cols")
        for (let c = 1; c < cols.length; c++) {
          let input = document.createElement("input")
          
          if(i == 6 || i == 7){
            input = document.createElement("select")
          }
          
          input.value       = cols[c].innerHTML
          cols[c].innerHTML = ""
          cols[c].appendChild(input)
          edit_btn[e].innerHTML = "Guardar"
          delete_btn[e].innerHTML = "Cancelar"
        }
      })
    }
    
    for(let i = 0; i < delete_btn.length; i++){
      delete_btn[i].addEventListener("click", () => {
        const rows = table.querySelectorAll(".register_rows")
      })
    }

    
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

        console.log(new_table)
        
        old_table.parentNode.replaceChild(new_table, old_table)

        
      })
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