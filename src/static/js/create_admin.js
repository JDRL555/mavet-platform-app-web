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
    const body = table.querySelectorAll("tbody")
    
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
          form.enctype = "multipart/form-data"
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
    
    body[1].appendChild(new_row)
    table.appendChild(body[1])
    form.appendChild(table)
    modal.appendChild(form)
    

    cancel_btn.addEventListener("click", () => {
      new_row.remove()
      create_btn.style.display  = ""
      modal.appendChild(table)
      form.remove()
    })
  })
}