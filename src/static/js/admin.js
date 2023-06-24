const btns            = document.querySelectorAll(".admin_option")
const request_option  = document.querySelector(".request_option")
const options         = document.querySelectorAll(".options")
const actions         = document.querySelectorAll("p")
const modal_bg        = document.querySelector(".modal_bg")

request_option.addEventListener("click", () => window.location = "/post/request")

for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", () => {
    if(options[i].style.opacity == 0){
      i == 2 || i == 3 ? options[i].style.top = "-40%" : options[i].style.top = "40%"
      options[i].style.opacity      = 1
      options[i].style.visibility   = "visible"
    }else{
      options[i].style.top          = 0
      options[i].style.opacity      = 0
      setTimeout(() => options[i].style.visibility  = "hidden", 1)
    }
  })
}

for (let i = 1; i < actions.length; i++) {
  actions[i].addEventListener("click", async () => {
    for (let j = 0; j < btns.length; j++) {
      options[j].style.top          = 0
      options[j].style.opacity      = 0
      setTimeout(() => options[j].style.visibility  = "hidden", 1)
    }
    let from = ""
    if(i >= 1  && i <= 4 ) from = "Usuarios" 
    if(i >= 5  && i <= 8 ) from = "Eventos" 
    if(i >= 9  && i <= 12) from = "Cursos" 
    if(i >= 13 && i <= 16) from = "Categorias" 
    const data      = { from, option: actions[i].innerHTML }
    const response  = await fetch("/modal", {
      method: "POST",
      body: JSON.stringify(data),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
    let modal     = await response.text()
    const parser  = new DOMParser()
    modal         = parser.parseFromString(modal, "text/html")
    modal         = modal.body.querySelector(".modal")
    
    if(modal.querySelector(".modal_content")) modal.style.width = "auto" 
    if(modal.querySelector(".modal_form")) modal.style.height = "80vh" 
    
    modal_bg.appendChild(modal)

    modal.style.transform       = "translateY(0px)"
    modal_bg.style.opacity      = 1
    modal_bg.style.visibility   = "visible"
    
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
        if(response.status == "200"){
          let new_table   = await response.text()
          const parser    = new DOMParser()
          const old_table = modal.querySelector(".modal_content") 
          new_table       = parser.parseFromString(new_table, "text/html")
          new_table       = new_table.body.querySelector(".modal_content")
          
          old_table.parentNode.replaceChild(new_table, old_table)
        }
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
