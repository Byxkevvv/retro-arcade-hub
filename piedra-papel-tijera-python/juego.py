import tkinter as tk
import random

# -----------------------------
# CONFIGURACIÓN DEL JUEGO
# -----------------------------

puntos_jugador = 0
puntos_cpu = 0

opciones = ["Piedra", "Papel", "Tijera"]


# -----------------------------
# LÓGICA DEL JUEGO
# -----------------------------

def jugar(eleccion_jugador):
    global puntos_jugador, puntos_cpu

    eleccion_cpu = random.choice(opciones)

    texto_jugadas.config(
        text=f"Tú: {eleccion_jugador}   |   CPU: {eleccion_cpu}"
    )

    if eleccion_jugador == eleccion_cpu:
        mensaje.config(
            text="¡EMPATE!",
            fg="#FFD166"
        )

    elif (
        (eleccion_jugador == "Piedra" and eleccion_cpu == "Tijera")
        or
        (eleccion_jugador == "Papel" and eleccion_cpu == "Piedra")
        or
        (eleccion_jugador == "Tijera" and eleccion_cpu == "Papel")
    ):
        puntos_jugador += 1

        mensaje.config(
            text="¡GANASTE!",
            fg="#7CFF6B"
        )

    else:
        puntos_cpu += 1

        mensaje.config(
            text="¡GANA LA CPU!",
            fg="#FF6B6B"
        )

    actualizar_marcador()


def actualizar_marcador():
    marcador_jugador.config(text=str(puntos_jugador))
    marcador_cpu.config(text=str(puntos_cpu))


def reiniciar():
    global puntos_jugador, puntos_cpu

    puntos_jugador = 0
    puntos_cpu = 0

    actualizar_marcador()

    texto_jugadas.config(
        text="¡Selecciona una opción!"
    )

    mensaje.config(
        text="¿PREPARADO?",
        fg="#FFD166"
    )


# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------

ventana = tk.Tk()

ventana.title("Piedra, Papel o Tijera")
ventana.geometry("700x650")
ventana.resizable(False, False)

ventana.configure(bg="#10182B")


# -----------------------------
# TÍTULO
# -----------------------------

titulo = tk.Label(
    ventana,
    text="PIEDRA, PAPEL O TIJERA",
    font=("Arial", 26, "bold"),
    bg="#10182B",
    fg="#FFB703"
)

titulo.pack(pady=(35, 5))


subtitulo = tk.Label(
    ventana,
    text="Elige tu jugada",
    font=("Arial", 14),
    bg="#10182B",
    fg="#FFD166"
)

subtitulo.pack(pady=(0, 25))


# -----------------------------
# MARCADOR
# -----------------------------

marcadores = tk.Frame(
    ventana,
    bg="#10182B"
)

marcadores.pack(pady=10)


panel_jugador = tk.Frame(
    marcadores,
    bg="#17233D",
    padx=40,
    pady=15
)

panel_jugador.grid(
    row=0,
    column=0,
    padx=15
)


tk.Label(
    panel_jugador,
    text="JUGADOR",
    font=("Arial", 12, "bold"),
    bg="#17233D",
    fg="#FFD166"
).pack()


marcador_jugador = tk.Label(
    panel_jugador,
    text="0",
    font=("Arial", 30, "bold"),
    bg="#17233D",
    fg="white"
)

marcador_jugador.pack()


panel_cpu = tk.Frame(
    marcadores,
    bg="#17233D",
    padx=50,
    pady=15
)

panel_cpu.grid(
    row=0,
    column=1,
    padx=15
)


tk.Label(
    panel_cpu,
    text="CPU",
    font=("Arial", 12, "bold"),
    bg="#17233D",
    fg="#FFD166"
).pack()


marcador_cpu = tk.Label(
    panel_cpu,
    text="0",
    font=("Arial", 30, "bold"),
    bg="#17233D",
    fg="white"
)

marcador_cpu.pack()


# -----------------------------
# BOTONES
# -----------------------------

botones = tk.Frame(
    ventana,
    bg="#10182B"
)

botones.pack(pady=40)


boton_piedra = tk.Button(
    botones,
    text="PIEDRA",
    font=("Arial", 14, "bold"),
    width=12,
    height=4,
    bg="#274C77",
    fg="white",
    activebackground="#FFB703",
    cursor="hand2",
    command=lambda: jugar("Piedra")
)

boton_piedra.grid(
    row=0,
    column=0,
    padx=10
)


boton_papel = tk.Button(
    botones,
    text="PAPEL",
    font=("Arial", 14, "bold"),
    width=12,
    height=4,
    bg="#274C77",
    fg="white",
    activebackground="#FFB703",
    cursor="hand2",
    command=lambda: jugar("Papel")
)

boton_papel.grid(
    row=0,
    column=1,
    padx=10
)


boton_tijera = tk.Button(
    botones,
    text="TIJERA",
    font=("Arial", 14, "bold"),
    width=12,
    height=4,
    bg="#274C77",
    fg="white",
    activebackground="#FFB703",
    cursor="hand2",
    command=lambda: jugar("Tijera")
)

boton_tijera.grid(
    row=0,
    column=2,
    padx=10
)


# -----------------------------
# RESULTADO
# -----------------------------

texto_jugadas = tk.Label(
    ventana,
    text="¡Selecciona una opción!",
    font=("Arial", 13),
    bg="#17233D",
    fg="white",
    width=50,
    pady=12
)

texto_jugadas.pack()


mensaje = tk.Label(
    ventana,
    text="¿PREPARADO?",
    font=("Arial", 20, "bold"),
    bg="#10182B",
    fg="#FFD166"
)

mensaje.pack(pady=15)


# -----------------------------
# REINICIAR
# -----------------------------

boton_reiniciar = tk.Button(
    ventana,
    text="REINICIAR PARTIDA",
    font=("Arial", 12, "bold"),
    bg="#FFB703",
    fg="#10182B",
    padx=20,
    pady=10,
    cursor="hand2",
    command=reiniciar
)

boton_reiniciar.pack(pady=10)


# -----------------------------
# INICIAR PROGRAMA
# -----------------------------

ventana.mainloop()
