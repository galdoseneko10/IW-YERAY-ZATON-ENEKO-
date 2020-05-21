var checks = document.getElementsByClassName("borrar_componete");
    for (var i = 0; i < checks.length; i++) {
  checks[i].addEventListener("click", function (event) {
    event.preventDefault()
    let form = event.target.parentNode;
    let tarea = new FormData(form);
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
        let row = form.parentNode.parentNode;
          row.remove();

      })
      .catch(function (err) {
        alert("error inesperado");
      });

    }

  });
}
