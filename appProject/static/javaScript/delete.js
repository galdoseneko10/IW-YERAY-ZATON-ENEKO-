var checks = document.getElementsByClassName("borrar_componete");

//Recorremos todos los checkbox que tengan class="check-finalizar" (uno por tarea, en principio)
    for (var i = 0; i < checks.length; i++) {
  //Añadimos un EventListener para poder saber cuando se clica el checkbox
  checks[i].addEventListener("click", function (event) {
    event.preventDefault()
    //Definimos el formulario para luego acceder a sus datos
    let form = event.target.parentNode;
    //Definimos la tarea para luego actualizarla en BBDD
    let tarea = new FormData(form);
    //Llamada AJAX para marcar como realizada la tarea
    if (confirm('Desea borrar el componente?')){

        fetch("../componentes/borrar/api", {
      method: "POST",
      body: tarea,
    })
      .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en la llamada Ajax";
        }
      })
      .then(function (texto) {
        //Definimos las fila que corresponde a la tarea para despues eliminarla
        let row = form.parentNode.parentNode;
        //La marcamos como done, lo que la hace moverse via CSS
        //Definimos el tiempo que se va a desplazar antes de eliminarla

          row.remove();

      })
      .catch(function (err) {
        alert("error inesperado");
      });

    }

  });
}
