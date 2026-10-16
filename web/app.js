import { PoseLandmarker, FilesetResolver } from
  "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.14/+esm";

const MODEL = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task";
const video = document.getElementById("video");
const boton = document.getElementById("start");
const estado = document.getElementById("status");

async function crearDetector() {
  const fileset = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.14/wasm");
  return PoseLandmarker.createFromOptions(fileset, {
    baseOptions: { modelAssetPath: MODEL },
    runningMode: "VIDEO",
    numPoses: 1,
  });
}

boton.onclick = async () => {
  try {
    estado.textContent = "Pidiendo cámara…";
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = stream;
    await video.play();

    estado.textContent = "Cargando modelo de pose…";
    const detector = await crearDetector();
    estado.textContent = "";

    const bucle = () => {
      const res = detector.detectForVideo(video, performance.now());
      console.log(res.landmarks[0]?.[25]);   // rodilla izquierda
      requestAnimationFrame(bucle);
    };
    bucle();
  } catch (e) {
    estado.textContent = "Error: " + e.message;
  }
};