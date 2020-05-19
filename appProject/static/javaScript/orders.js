
var datajson;
function catalogo_pedidos(data) {
  let cad = "";

  for (let i = 0; i < data.length; i++) {
    cad += template_catalogo(data[i]);
  }
  return cad;
}

fetch("../pedidos/api")
  .then(function (response) {
    if (response.ok) {
      return response.text();
    } else {
      throw "Error en la llamada Ajax";
    }
  })
  .then(function (data) {
    datos = JSON.parse(data);
    console.log(datos)
    document.getElementById("lista_pedidos").innerHTML = catalogo_pedidos(datos.pedidos);

  })
  .catch(function (error) {
    console.log(error)
    alert("Error inesperado");
  });

function template_catalogo(ped) {
  retorno = `<li  class="span3 gallery-item" data-id="id-1" data-type="illustration">
        <ul class="element">
            <br>
            <li> CODIGO DE REFERENCIA: ${ ped.codigo_referencia }</li>
            <br>
            <li> FECHA: ${ ped.fecha } </li>
            <br>
            <li> CLIENTE: ${ ped.datos_cliente }</li>
            <br>
        </ul>

        <br>

        <a href="edit/${ ped.id }"><button class="separacionbottom">Editar</button></a>
        <a href="delete/${ ped.id }"
           onClick="return confirm('¿Seguro que quieres borrar los datos de: ${ped.codigo_referencia}?');">
            <button class="separacionbottom">Borrar</button>
        </a>
        <a href="/../appProject/pedido/${ ped.id }"><button class="separacionbottom">Ver</button></a>
    </li>`
  return retorno
}
