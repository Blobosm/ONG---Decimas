$(document).ready(function () {


        $("#btnbuscagif").click(function(e){
            $.get("https://g.tenor.com/v1/search?q="+$("#txtgif").val()+"&key=LIVDSRZULELA&limit=100", function(data){
                
                console.log(data);
                $("#resultado").html(null);
                 $.each(data.results, function(i,item){
                    //console.log(item.media[0]["gif"]["preview"]);
                 
                    $("#resultado").append("<img style='width:300px;' src='"+item.media[0]["gif"]["preview"]+"'/>")
                });
            });
        });



        $("#btnbuscarProductos").click(function(e){

            $.get("https://www.themealdb.com/api/json/v1/1/categories.php", function(data){

                $.each(data.categories, function(i,item){
                    $("#categoria").append("<tr><td>"+item.idCategory+"</td>"+
                                            "<td>"+item.strCategory+"</td>"+
                                            "<td> <img src='"+item.strCategoryThumb+"' /></td>"+
                                            "<td>"+item.strCategoryDescription+"</td></tr>"
                    );
                });

            });

        });



    /*  $("#txtnombre").focus(function (e) {


          if ($("#txtnombre").val() == "") {
              $("#r_txtnombre").html("Debe completar el campo");
          } else {
              $("#r_txtnombre").html(null);
          }




      });
      $("#txtnombre").change(function (e) {


          if ($("#txtnombre").val() == "") {
              $("#r_txtnombre").html("Debe completar el campo");
          } else {
              $("#r_txtnombre").html(null);
          }




      });*/

    $("#btnenviar").click(function (e) {


        if (validaFormulario() != "") {
            swal("Error en Formulario", validaFormulario(), "error");
        } else {
            swal("Envio Correcto", "En la brevedad nos pondremos en Contacto con usted", "success");
            $('#btnreset').trigger('click');

        }


        e.preventDefault();
    });
});

function validaFormulario() {

    var html = "";

    if ($("#txtnombre").val() == "") {
        html += "- El campo nombre no puede ser nulo \n";
    }
    if ($("#txtemail").val() == "") {
        html += "- El Email nombre no puede ser nulo \n";
    }
    if (($("#rbtnRUT")).is(":not(:checked)") && ($("#rbtnPasaporte")).is(":not(:checked)")) {
        html += "- Debe selecionar Tipo de Identificacion \n";
    } else {
        if ($("#txtidentificador").val() == "") {
            html += "- Debe Ingresar datos en Rut/Pasaporte \n";
        } else {
            if (($("#rbtnRUT")).is(":checked")) {
                if (validarRut($("#txtidentificador").val()) == false) {
                    html += "- Debe Ingresar un Rut Válido \n";
                }
            }
        }
    }
    if ($("#cbxCiudad").val() == "0") {
        html += "- El Seleccionar una Ciudad \n";
    }
    if ($("#txtaComentario").val().trim().length < 50) {
        html += "- El Comentario debe contener a lo menos 50 caracteres \n";
    }
    return html;
}

function insertanombre() {



    /*  if (($("#rbtnRUT")).is(":checked")) {
          alert("esta check el rut");
      } else {
          alert("esta check el pasaporte");
      }*/

    /* if (validarRut($("#txtidentificador").val()) == true) {
         alert("Es Valido");
     } else {
         alert("No Valido");
     }*/

    /* alert($("#cbxCiudad").val());*/


    /*textoAreaDividido = $("#txtaComentario").val().trim();
    alert(textoAreaDividido);
    alert(textoAreaDividido.length);*/

    preventDefault();
}

function validarRut(rutCompleto) {
    // Primero eliminamos cualquier caracter que no sea número o k/K
    rutCompleto = rutCompleto.replace("‐", "-");

    // Luego validamos que el formato del RUT sea válido
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
        return false;

    // Separamos el número del dígito verificador    
    var tmp = rutCompleto.split('-');
    // Calculamos el dígito verificador esperado
    var digv = tmp[1];
    var rut = tmp[0];
    if (digv == 'K') digv = 'k';
    // Comparamos el dígito verificador ingresado con el esperado
    return (dv(rut) == digv);
}

function dv(T) {
    var M = 0,
        S = 1;
    for (; T; T = Math.floor(T / 10))
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
}


function valrut(objeto) {
    var i, s, f, bueno;
    f = "32765432";
    r = objeto.value;
    largo = r.length - 2;
    bueno = false;
    s = 0;
    for (i = 0; i < largo; i++) {
        s = s + (parseInt(r.charAt(i)) * parseInt(f.charAt(i)));
    }
    dv = 11 - (s % 11);
    if (dv == 10 && (r.charAt(9) == 'K' || r.charAt(9) == 'k')) {
        bueno = true;
    } else {
        if (dv == 11 && r.charAt(9) == '0') {
            bueno = true;
        } else {
            if (dv == parseInt(r.charAt(9))) {
                bueno = true;
            } else {
                alert("RUT Incorrecto...");
                objeto.focus();
                bueno = false;
            }
        }
    }
    return bueno;
}


function soloNumeros(string) {
    var out = '';
    var filtro = '1234567890'; //Caracteres validos
    //Recorrer el texto y verificar si el caracter se encuentra en la lista de validos 
    for (var i = 0; i < string.length; i++)
        if (filtro.indexOf(string.charAt(i)) != -1)
            //Se añaden a la salida los caracteres validos
            out += string.charAt(i);
    //Retornar valor filtrado
    return out;
}