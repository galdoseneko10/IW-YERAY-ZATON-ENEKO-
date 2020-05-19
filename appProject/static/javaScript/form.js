var form= document.getElementById('formulario_alta') //tomar referncia del htm

form.addEventListener('submit',function(e){
    e.preventDefault() //no se envia el formulario predefinido sino como queremos nosotros
    let formulario = new FormData(form);//crear un objecto a partir del los datos del formulario

        fetch('../../formulario/api',{method:'POST',body:formulario})//manda los datos del formulario al servidor

        .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en la llamada Ajax";
        }
      })
      .then(function (texto) {

        alert('todo ok horse luis')

      })
      .catch(function (err) {
        alert("error inesperado");
      });

    })




