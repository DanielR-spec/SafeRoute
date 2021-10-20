function sendMail(params) {
  var tempParams = {

    nombre: document.getElementById('nombre').value,
    correo: document.getElementById('correo').value,
    telefono: document.getElementById('telefono').value,
    servicio: document.getElementById('inputGroupSelect01').value,
    solicitud:document.getElementById('solicitud').value,
    nper:document.getElementById('nper').value,
    fecha:document.getElementById('fecha').value,
    hora:document.getElementById('hora').value,

  };


  
    emailjs.send('service_sv1w0q4','template_ycz08nm',tempParams)
    .then(function (res) {
      alert("reserva realizada");
            localStorage.clear();
            window.location.replace("../index.html");
            
    
    })
}