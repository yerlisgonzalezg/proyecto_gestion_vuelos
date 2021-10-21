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