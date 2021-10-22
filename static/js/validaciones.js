"use strict";


var paisorigen=document.getElementById("paisorigen");
var paisdestino=document.getElementById("paisdestino");
var mensaje=document.getElementById("mensaje");
paisdestino.addEventListener("change", function(){
    console.log("entrar");
    if (paisorigen.value==paisdestino.value){
        paisdestino.value=null;
        mensaje.innerHTML="<p>Pais de origen no puede ser igual al pais destino</p>";
        mensaje.style.color="red";
    }
});
var fecharegresoL=document.getElementById("tipo2");
var tipo2=document.getElementById("tipo2");
    tipo2.addEventListener("click", function(){
        fecharegresoS.style.display="none";
});

var tipo1=document.getElementById("tipo1");
var fecharegreso=document.getElementById("fecharegresoL");
    tipo1.addEventListener("click", function(){
        fecharegresoS.style.display="block";
        fecharegreso.required = true;
});