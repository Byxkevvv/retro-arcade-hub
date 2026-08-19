const botones = document.querySelectorAll(".opcion");
const mensaje = document.getElementById("mensaje");
const jugadas = document.getElementById("jugadas");
const puntosJugadorTexto = document.getElementById("puntosJugador");
const puntosCPUTexto = document.getElementById("puntosCPU");
const botonReiniciar = document.getElementById("reiniciar");

let puntosJugador = 0;
let puntosCPU = 0;

const opciones = ["piedra", "papel", "tijera"];

const simbolos = {
    piedra: "✊",
    papel: "📄",
    tijera: "✂️"
};

botones.forEach(boton => {

    boton.addEventListener("click", () => {

        const jugador = boton.dataset.eleccion;

        const numeroAleatorio = Math.floor(Math.random() * 3);
        const cpu = opciones[numeroAleatorio];

        jugar(jugador, cpu);

    });

});

function jugar(jugador, cpu) {

    jugadas.textContent =
        "Tú: " + simbolos[jugador] + " " + jugador +
        " | CPU: " + simbolos[cpu] + " " + cpu;

    if (jugador === cpu) {

        mensaje.textContent = "🤝 ¡EMPATE!";
        return;

    }

    if (
        (jugador === "piedra" && cpu === "tijera") ||
        (jugador === "papel" && cpu === "piedra") ||
        (jugador === "tijera" && cpu === "papel")
    ) {

        puntosJugador++;

        mensaje.textContent = "🎉 ¡GANASTE!";

    } else {

        puntosCPU++;

        mensaje.textContent = "🤖 ¡GANA LA CPU!";

    }

    actualizarMarcador();
}

function actualizarMarcador() {

    puntosJugadorTexto.textContent = puntosJugador;
    puntosCPUTexto.textContent = puntosCPU;

}

botonReiniciar.addEventListener("click", () => {

    puntosJugador = 0;
    puntosCPU = 0;

    actualizarMarcador();

    jugadas.textContent = "¡Selecciona una opción!";
    mensaje.textContent = "¿Preparado?";

});