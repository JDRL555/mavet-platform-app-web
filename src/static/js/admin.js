const btns            = document.querySelectorAll(".admin_option") // opciones del admin
const request_option  = document.querySelector(".request_option") // ver publicaciones solicitadas
const modal_bg        = document.querySelector(".modal_bg") // ventana para mostrar registros

request_option.addEventListener("click", () => window.location = "/post/request")

// se encarga de cubrir las opciones de editar los registros
function edit_operation(table, rows, edit_btn, delete_btn, from){
  for(let e = 0; e < edit_btn.length; e++){
    edit_btn[e].addEventListener("click", () => {
      const cols          = rows[e].querySelectorAll(".register_cols")
      const id            = cols[0].innerText
      const save_btn      = document.createElement("td")
      const cancel_btn    = document.createElement("td")
      const original_cols = []

      save_btn.setAttribute("class", "save_btn")
      cancel_btn.setAttribute("class", "cancel_btn")
      
      save_btn.innerText    = "Guardar"
      cancel_btn.innerText  = "Cancelar"
      
      for (let c = 0; c < cols.length; c++) {
        let input = document.createElement("input")
        input.setAttribute("class", "edit_input")
        
        if(parseInt(cols[0].innerHTML) && c <= 0) c++
        
        if(Date.parse(cols[c].innerHTML)){
          input.type = "date"
        }

        original_cols.push(cols[c].innerHTML)
        
        input.value = cols[c].innerHTML

        cols[c].innerHTML = ""
        cols[c].appendChild(input)
      }

      edit_btn[e].parentNode.replaceChild(save_btn, edit_btn[e])
      delete_btn[e].parentNode.replaceChild(cancel_btn, delete_btn[e])

      save_btn.addEventListener("click", async () => {
        const values    = table.querySelectorAll(".edit_input")
        const cols      = table.querySelectorAll("th")
        const edit_info = {}
        let index       = 0
        
        cols[0].innerHTML == "ID" && index++
        
        for (let g = index; g <= values.length; g++) {
          edit_info[cols[g].innerHTML] = values[g - 1].value
        }
        
        edit_info["id"] = id
        
        let route = ""
        if(from == "Usuarios")    route = "user"
        if(from == "Eventos")     route = "event"
        if(from == "Cursos")      route = "course"
        if(from == "Categorias")  route = "category"

        window.location.href = `/${route}/edit?info=${JSON.stringify(edit_info)}`
      })

      cancel_btn.addEventListener("click", () => { 
        edit_btn[e]    = document.createElement("td")
        delete_btn[e]  = document.createElement("td")

        edit_btn[e].setAttribute("class", "edit_col")
        delete_btn[e].setAttribute("class", "delete_col")
        
        edit_btn[e].innerText   = "Editar"
        delete_btn[e].innerText = "Eliminar"

        save_btn.parentNode.replaceChild(edit_btn[e], save_btn)
        cancel_btn.parentNode.replaceChild(delete_btn[e], cancel_btn)

        if(cols[0].innerText){
          original_cols.forEach((col, c) => {
             cols[c + 1].innerHTML = col
          })
        }else{
          original_cols.forEach((col, c) => {
            cols[c].innerHTML = col
         })
        }
      })
    })

  }
}

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

function create_operation(table, modal, create_btn, from){
  create_btn.addEventListener("click", () => {
    create_btn.style.display  = "none"
    const cols = []
    if(from == "Usuarios") {
      cols.push("Nombres")
      cols.push("Apellidos")
      cols.push("Fecha de Nacimiento")
      cols.push("Correo")
      cols.push("Nombre de usuario")
      cols.push("Telefono")
      cols.push("Especialidad del usuario")
      cols.push("Tipo de usuario")
      cols.push("Clave")
    }

    if(from == "Eventos") {
      cols.push("Nombre")
      cols.push("Descripcion")
      cols.push("Fecha de inicio")
      cols.push("Fecha de finalizacion")
      cols.push("Hora de inicio")
      cols.push("Hora de finalizacion")
      cols.push("Multimedia")
    }

    if(from == "Cursos") {
      cols.push("Nombre")
      cols.push("Descripcion")
      cols.push("Profesor")
      cols.push("Fecha de inicio")
      cols.push("Fecha de finalizacion")
      cols.push("Hora de inicio")
      cols.push("Hora de finalizacion")
      cols.push("Precio")
      cols.push("Multimedia")
    }

    if(from == "Categorias") {
      cols.push("Nombre")
    }
    const body = table?.querySelector("tbody")
    
    const new_row             = document.createElement("tr")
    const save_container      = document.createElement("td")
    const cancel_container    = document.createElement("td")
    const form                = document.createElement("form")
    const save_btn            = document.createElement("button")
    const cancel_btn          = document.createElement("button")
    const file_container      = document.createElement("div")
    const file_text           = document.createElement("p")
    const file_logo           = document.createElement("i")
    
    let route = ""

    if(from == "Usuarios")    route = "user"
    if(from == "Eventos")     route = "event"
    if(from == "Cursos")      route = "course"
    if(from == "Categorias")  route = "category"

    form.action = `/${route}/new`
    form.method = "POST"
    form.enctype = "multipart/form-data"

    save_btn.setAttribute("class", "save_btn")
    cancel_btn.setAttribute("class", "cancel_btn")

    save_btn.innerText    = "Guardar"
    cancel_btn.innerText  = "Cancelar"

    file_container.setAttribute("class", "file_container")
    file_logo.setAttribute("class", "fa-solid fa-upload")
    file_text.innerText = "Multimedia"
    
    file_text.appendChild(file_logo)
    file_container.appendChild(file_text)

    for (let c = -1; c < cols.length; c++) {
      const new_col = document.createElement("td")
      let input     = document.createElement("input")

      if(c == -1){
        new_row.appendChild(new_col)
      }else{
        input.setAttribute("class", "create_input")
        
        if(cols[c].includes("Fecha")){
          input.onclick = () => input.type = "date"
          input.onfocus = () => input.type = "date"
        }
  
        if(cols[c].includes("Hora")){
          input.onclick = () => input.type = "time"
          input.onfocus = () => input.type = "time"
        }

        if(cols[c].includes("Multimedia")){
          input.setAttribute("class", "create_input file")
          input.type    = "file"
          input.accept  = "image/*"
          input.addEventListener("change", () => {
            input.files.length
            ? file_container.style.backgroundColor = "#59c444"
            : file_container.style.backgroundColor = "#c92d2d"
          })
          file_container.appendChild(input)
        }
  
        if(cols[c].includes("Correo")){
          input.type = "email"
        }
  
        if(cols[c].includes("Telefono")){
          input.type = "number"
        }
        
        if(cols[c].includes("Clave")){
          input.type = "password"
        } 
  
        input.placeholder = cols[c]
        input.name        = cols[c]
        
        cols[c].includes("Multimedia") 
        ? new_col.appendChild(file_container)
        : new_col.appendChild(input)

        new_row.appendChild(new_col)
      }
    }

    save_container.appendChild(save_btn)
    cancel_container.appendChild(cancel_btn)

    new_row.appendChild(save_container)
    new_row.appendChild(cancel_container)

    console.log(modal)
    
    body.appendChild(new_row)
    table.appendChild(body)
    form.appendChild(table)
    modal.appendChild(form)

    // save_btn.addEventListener("click", async () => {
    //   const values = table?.querySelectorAll(".create_input") || modal.querySelectorAll(".create_input") 
    //   const save_info = {}

    //   for (let g = 0; g < values.length; g++) { 
    //     console.log(values[g].files[0])
    //     if(cols[g].includes("Multimedia")) {
    //       save_info[cols[g]] = values[g].files[0] 
    //     } 
    //     else save_info[cols[g]] = values[g].value
    //   }
      
    //   console.log(JSON.stringify(save_info))

    //   const response  = await fetch(`/${route}/new`, {
    //     method: "POST",
    //     body: JSON.stringify(save_info),
    //     mode: "cors",
    //     headers: {
    //       "Content-Type": "application/json",
    //     },
    //   })

    //   // window.location.href = `/${route}/new?info=${JSON.stringify(save_info)}`
    // })

    cancel_btn.addEventListener("click", () => {
      new_row.remove()
      create_btn.style.display  = ""
    })
  })
}

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

    console.log(modal)
    
    modal.style.width = "auto" 
    
    modal_bg.appendChild(modal)

    modal.style.transform       = "translateY(0px)"
    modal_bg.style.opacity      = 1
    modal_bg.style.visibility   = "visible"

    if(!modal.querySelector(".modal_content")){
      modal.querySelector(".modal_filters").remove()
      const empty       = document.createElement("h1")
      const create_btn  = document.createElement("button")

      create_btn.setAttribute("class", "create_col")
      create_btn.innerText = "Crear"

      empty.innerHTML = "No hay registros aun"
      empty.style.textAlign = "center"

      modal.appendChild(empty)
      modal.appendChild(create_btn)

      create_operation(null, modal, create_btn, from)
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