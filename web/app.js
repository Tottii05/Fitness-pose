const video = document.getElementById("video");
const boton = document.getElementById("start");
const estado = document.getElementById("status");

boton.onclick = async () => {
  try {
    estado.textContent = "Pidiendo cámara…";
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = stream;
    await video.play();
    estado.textContent = "";
  } catch (e) {
    estado.textContent = "Error: " + e.message;
  }
};