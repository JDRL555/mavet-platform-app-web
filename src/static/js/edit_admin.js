// se encarga de cubrir las opciones de editar los registros
function edit_operation(table, rows, edit_btn, delete_btn, from){
  for(let e = 0; e < edit_btn.length; e++){
    edit_btn[e].addEventListener("click", () => {
      const registers           = rows[e].querySelectorAll(".register_cols")
      const cols                = table.querySelectorAll("th")
      const id                  = cols[0].innerText
      let name                  = ""
      const save_btn            = document.createElement("td")
      const cancel_btn          = document.createElement("td")
      const original_registers  = []

      save_btn.setAttribute("class", "save_btn")
      cancel_btn.setAttribute("class", "cancel_btn")
      
      save_btn.innerText    = "Guardar"
      cancel_btn.innerText  = "Cancelar"
      
      for (let c = 0; c < registers.length; c++) {
        if(cols[c].innerHTML != "Fecha de creacion"){
          let input = document.createElement("input")
          input.setAttribute("class", "edit_input")
          
          if(parseInt(registers[0].innerHTML) && c <= 0) c++
          
          if(Date.parse(registers[c].innerHTML)){
            input.type = "date"
          }
  
          original_registers.push(registers[c].innerHTML)
          
          input.value = registers[c].innerHTML
  
          registers[c].innerHTML = ""
          registers[c].appendChild(input)
        }
      }

      edit_btn[e].parentNode.replaceChild(save_btn, edit_btn[e])
      delete_btn[e].parentNode.replaceChild(cancel_btn, delete_btn[e])

      save_btn.addEventListener("click", async () => {
        const values    = table.querySelectorAll(".edit_input")
        const edit_info = {}
        
        if(cols[0].innerHTML == "Nombre") {
          console.log("zi")
          edit_info["new_name"] = values[0].value
          name                  = original_registers[0]
          edit_info["old_name"] = name
        } else {
          for (let g = 1; g <= values.length; g++) {
            edit_info[cols[g].innerHTML] = values[g - 1].value
          }
          edit_info["id"] = id
        }

        console.log(edit_info)
        
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

        if(registers[0].innerText){
          original_registers.forEach((register, c) => {
             registers[c + 1].innerHTML = register
          })
        }else{
          original_registers.forEach((register, c) => {
            registers[c].innerHTML = register
         })
        }
      })
    })

  }
}