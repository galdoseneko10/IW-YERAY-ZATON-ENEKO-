var form= document.getElementById('formulario_alta') //tomar referncia del html

form.addEventListener('submit',function(e){
    e.preventDefault() //no se envia el formulario predefinido sino como queremos nosotros
    let formulario = new FormData(form);//crear un objecto a partir del los datos del formulario

        fetch('../../formulario/api',{method:'POST',body:formulario})//manda los datos del formulario al servidor

        .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en Ajax";
        }
      })
      .then(function (texto) {

        alert('¡Registrado correctamente!')

      })
      .catch(function (err) {
        alert("Error");
      });

    })




