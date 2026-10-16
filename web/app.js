import { PoseLandmarker, FilesetResolver, DrawingUtils } from
  "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.14/+esm";

const MODEL = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task";
const video = document.getElementById("video");
const boton = document.getElementById("start");
const estado = document.getElementById("status");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const PY_FILES = ["__init__.py", "geometry.py", "smoothing.py", "exercises.py", "api.py"];

async function crearDetector() {
    const fileset = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.14/wasm");
    return PoseLandmarker.createFromOptions(fileset, {
        baseOptions: { modelAssetPath: MODEL },
        runningMode: "VIDEO",
        numPoses: 1,
    });
}

async function iniciarPython() {
    const py = await loadPyodide();
    py.FS.mkdirTree("/home/pyodide/core");
    for (const f of PY_FILES) {
    const res = await fetch(`../core/${f}`);
    const texto = await res.text();
    const ruta = `/home/pyodide/core/${f}`;
    py.FS.writeFile(ruta, texto);
    }
    py.runPython(`import sys\nsys.path.insert(0, "/home/pyodide")`);
    return py.pyimport("core.api");
}
boton.onclick = async () => {
  try {
    estado.textContent = "Pidiendo cámara…";
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = stream;
    await video.play();
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const draw = new DrawingUtils(ctx);
    estado.textContent = "Cargando modelo de pose…";
    const detector = await crearDetector();
    estado.textContent = "";
    estado.textContent = "Cargando Python..."
    const api = await iniciarPython();
    estado.textContent = ""
    const bucle = () => {
        const res = detector.detectForVideo(video, performance.now());
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (res.landmarks.length > 0) {
            const lm = res.landmarks[0];
            draw.drawConnectors(lm, PoseLandmarker.POSE_CONNECTIONS);
            draw.drawLandmarks(lm);
        }
        requestAnimationFrame(bucle);
    };
    bucle();
  } catch (e) {
    estado.textContent = "Error: " + e.message;
  }
};