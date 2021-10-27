function validar_formulario() {

    vNombre = document.getElementById("nombre").value;
    vEmail = document.getElementById("email").value;
    var expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

    vPassword = document.getElementById("password").value;
    vPassword = document.getElementById("confirmpassword").value;

    if (vNombre == "") {
        alert("El campo nombre no debe estar vacío.");
        return false
    } else if (vEmail == "") {
        alert("El campo del correo electrónico no debe estar vacío.");
        return false
    } else if (expReg.test(vEmail) == false) {
        alert("El campo del correo electrónico no válido.");
        return false
    }
    else if (vPassword == "") {
        alert("El campo Contraseña no debe estar vacío.");
        return false
    } else if (vPassword.length < 8) {
        alert("El campo Contraseña debe tener mínimo 8 caracteres.");
        return false
    }
    else if (vConfirmpassword == "") {
        alert("El campo Confirmar contraseña no debe estar vacío.");
        return false
    } else if (vConfirmpassword.length < 8) {
        alert("El campo Confirmar contraseña debe tener mínimo 8 caracteres.");
        return false
    }
}

function validar_formulario_login() {

    vEmail = document.getElementById("email").value;
    var expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

    vPassword = document.getElementById("password").value;

    if (vEmail == "") {
        alert("El campo del correo electrónico no debe estar vacío.");
        return false
    } else if (expReg.test(vEmail) == false) {
        alert("El campo del correo electrónico no válido.");
        return false
    }
    else if (vPassword == "") {
        alert("El campo Contraseña no debe estar vacío.");
        return false
    } else if (vPassword.length < 8) {
        alert("El campo Contraseña debe tener mínimo 8 caracteres.");
        return false
    }
}

function mostrarPassword(){
    var obj = document.getElementById("password");
    obj.type = "text";
}

function ocultarPassword(){
    var obj = document.getElementById("password");
    obj.type = "password";
}

function mostrarConfirmPassword(){
    var obj = document.getElementById("confirmpassword");
    obj.type = "text";
}

function ocultarConfirmPassword(){
    var obj = document.getElementById("confirmpassword");
    obj.type = "password";
}

function validar_formulario_agregar_vuelo() {

    vNumVuelo = document.getElementById("numvuelo").value;
    vCapVuelo = document.getElementById("capvuelo").value;
    vEstVuelo = document.getElementById("estvuelo").value;
    vPilotoAsig = document.getElementById("pilotoasig").value;
    vOrigen = document.getElementById("origen").value;
    vDestino = document.getElementById("destino").value;
    vAvionAsig = document.getElementById("avionasig").value;
    vFechaSalida = document.getElementById("fechasalida").value;


    if (vNumVuelo == "") {
        alert("El campo del numero del vuelo no debe estar vacío.");
        return false
    }
    else if (vCapVuelo == "") {
        alert("El campo Capacidad de vuelo no debe estar vacío.");
        return false
    } 
    else if (vEstVuelo == "") {
        alert("El campo Estado de vuelo no debe estar vacío.");
        return false
    } 
    else if (vPilotoAsig == "") {
        alert("El campo Piloto de vuelo no debe estar vacío.");
        return false
    } 
    else if (vOrigen == "") {
        alert("El campo Origen de vuelo no debe estar vacío.");
        return false
    } 
    else if (vDestino == "") {
        alert("El campo Destino de vuelo no debe estar vacío.");
        return false
    } 
    else if (vAvionAsig == "") {
        alert("El campo Avion asignado a vuelo no debe estar vacío.");
        return false
    } 
    else if (vCapVuelo == "") {
        alert("El campo Capacidad de vuelo no debe estar vacío.");
        return false
    } 
    else if (vFechaSalida == "") {
        alert("El campo Fecha de salida de vuelo no debe estar vacío.");
        return false
    } 
}

function informacion_vuelo (id,pasajero){
    // window.open("/reservas/"+id+""+"/"+pasajero+"","ventana3","width=500,height=700,scrollbars=NO")
    window.open("/reservas/"+id+""+"/"+pasajero+"",'_blank')
    // window.open(url, '_blank');
    
 }
 function informacion_vuelo_ida (id,pasajero){
    window.open("/reservas_ida/"+id+""+"/"+pasajero+"",'_blank')
 }


const btnDelete = document.querySelectorAll('.btn-delete')
if (btnDelete) {
    const btnArray=Array.from(btnDelete);
    btnArray.forEach((btn) =>{
        btn.addEventListener('click', (e) => {
            if(!confirm('Estas seguro de querer eliminar este usuario?')){
                e.preventDefault();
            }
        });
    });
    
    
}