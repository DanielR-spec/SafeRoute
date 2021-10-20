function sendMail(params) {
  var tempParams = {

    nombre: document.getElementById('nombre').value,
    correo: document.getElementById('correo').value,

  };


  
    emailjs.send('service_sv1w0q4','template_ycz08nm',tempParams)
    .then(function (res) {
      alert("reserva realizada");
            localStorage.clear();
            window.location.replace("index.html");
            
    
    })
}