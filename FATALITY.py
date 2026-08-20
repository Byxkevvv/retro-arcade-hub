import tkinter as tk
from tkinter import messagebox
import json
import os


# =========================
# LEADERBOARD
# =========================

ARCHIVO_LEADERBOARD = "leaderboard.json"


def cargar_leaderboard():
    if not os.path.exists(ARCHIVO_LEADERBOARD):
        return []

    try:
        with open(ARCHIVO_LEADERBOARD, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_leaderboard(leaderboard):
    with open(ARCHIVO_LEADERBOARD, "w", encoding="utf-8") as archivo:
        json.dump(leaderboard, archivo, indent=4, ensure_ascii=False)


leaderboard = cargar_leaderboard()


# =========================
# VENTANA PRINCIPAL
# =========================

ventana = tk.Tk()
ventana.title("FATALITY ARCADE")
ventana.geometry("900x600")
ventana.configure(bg="#08011A")
ventana.resizable(False, False)


# =========================
# FUNCIONES DE LAS PANTALLAS
# =========================

def limpiar_pantalla():
    for widget in ventana.winfo_children():
        widget.destroy()


def mostrar_inicio():
    limpiar_pantalla()

    titulo = tk.Label(
        ventana,
        text="FATALITY",
        font=("Impact", 40, "bold"),
        fg="#08011A",
        bg="#00FFFF"
    )
    titulo.pack(pady=50)

    subtitulo = tk.Label(
        ventana,
        text="¡BIENVENIDO JUGADOR!",
        font=("Impact", 27, "bold"),
        fg="white",
        bg="#08011A"
    )
    subtitulo.pack(pady=10)

    tk.Button(
        ventana,
        text="JUGAR",
        font=("Impact", 16),
        width=25,
        command=mostrar_juegos
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="INSTRUCCIONES",
        font=("Impact", 16),
        width=25,
        command=mostrar_instrucciones
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="LEADERBOARD",
        font=("Impact", 16),
        width=25,
        command=mostrar_leaderboard
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="CRÉDITOS",
        font=("Impact", 16),
        width=25,
        command=mostrar_creditos
    ).pack(pady=10)


def mostrar_juegos():
    limpiar_pantalla()

    tk.Label(
        ventana,
        text="JUEGOS",
        font=("Impact", 27, "bold"),
        fg="#00ffcc",
        bg="#08011A"
    ).pack(pady=50)

    tk.Button(
        ventana,
        text=("Piedra, Papel o Tijera"),
        font=("Impact", 20),
        fg="#08011A",
        bg="#D7BFDE"
    ).pack(pady=20)

    tk.Button(
        ventana,
        text=("Buscaminas"),
        font=("Impact", 20),
        fg="#08011A",
        bg="#D7BFDE",
    ).pack(pady=25)

    boton_volver()

def mostrar_instrucciones():
    limpiar_pantalla()

    tk.Label(
        ventana,
        text="INSTRUCCIONES",
        font=("Impact", 27, "bold"),
        fg="#00ffcc",
        bg="#08011A"
    ).pack(pady=40)

    instrucciones = (
     " - Selecciona un juego desde el menú principal.\n\n"
     " - En Piedra, Papel o Tijera, elige una opción y compite contra tu oponente.\n\n"
     " - En Buscaminas, descubre las casillas evitando las minas.\n\n"
     " - Intenta conseguir la mayor puntuación posible.\n\n"
     " - Tus resultados se registrarán en el leaderboard.\n\n"
     " - Utiliza VOLVER para regresar al menú principal."
)

    tk.Label(
        ventana,
        text=instrucciones,
        font=("Impact", 16),
        fg="white",
        bg="#08011A",
        justify="left"
    ).pack(pady=20)

    boton_volver()


def mostrar_leaderboard():
    limpiar_pantalla()

    tk.Label(
        ventana,
        text="LEADERBOARD",
        font=("Impact", 27, "bold"),
        fg="#00ffcc",
        bg="#08011A"
    ).pack(pady=40)

    if not leaderboard:
        tk.Label(
            ventana,
            text="Todavía no hay récords.",
            font=("Impact", 18),
            fg="white",
            bg="#08011A"
        ).pack(pady=20)
    else:
        for posicion, jugador in enumerate(leaderboard, start=1):
            texto = f"{posicion}. {jugador['nombre']}  -  {jugador['puntuacion']} puntos"

            tk.Label(
                ventana,
                text=texto,
                font=("Arial", 16, "bold"),
                fg="white",
                bg="#111111"
            ).pack(pady=5)

    boton_volver()


def mostrar_creditos():
    limpiar_pantalla()

    tk.Label(
        ventana,
        text="CRÉDITOS",
        font=("Impact", 27, "bold"),
        fg="#00ffcc",
        bg="#08011A",
    ).pack(pady=30) 

    tk.Label(
        ventana,
        text="Detrás de cada pantalla, cada juego y cada detalle hay horas de dedicación.\n\n "
        "Cada integrante aportó sus habilidades, creatividad y dedicación para hacer posible este reto.\n\n "
        "¡Conoce a quienes hicieron posible FATALITY!",
        font=("Impact", 12),
        fg="#EDE5ED",
        bg="#08011A", 
        justify="center"
    ).pack(pady=(0,25))


    estudiantes = [
        ("Alison Herrera","Diseño y desarrollo de la interfaz principal"),
        ("Kevin González", "Desarrollo del juego Piedra, Papel o Tijera"),
        ("Adrián Reyes", "Desarrollo del juego Buscaminas"),
        ("Phillip de Leon", "Integración del proyecto y gestión en GitHub"),
     ]


    for nombre, trabajo in estudiantes:
        tk.Button(
            ventana,
            text=nombre,
            font=("Impact", 15),
            width=25,
            command=lambda n=nombre, t=trabajo: mostrar_estudiante(n, t)
        ).pack(pady=7)

    boton_volver()


def mostrar_estudiante(nombre, trabajo):
    limpiar_pantalla()

    tk.Label(
        ventana,
        text=f" {nombre}",
        font=("Impact", 28, "bold"),
        fg="#00ffcc",
        bg="#08011A",
    ).pack(pady=60)

    tk.Label(
        ventana,
        text="Se encargo de:",
        font=("Impact", 20),
        fg="white",
        bg="#08011A",
    ).pack(pady=10)

    tk.Label(
        ventana,
        text=trabajo,
        font=("Impact", 18),
        fg="white",
        bg="#08011A"
    ).pack(pady=20)

    boton_volver(mostrar_creditos)


def boton_volver(funcion=mostrar_inicio):
    tk.Button(
        ventana,
        text="◀ VOLVER",
        font=("Impact", 14, "bold"),
        width=15,
        command=funcion
    ).pack(pady=30)


# =========================
# INICIAR APLICACIÓN
# =========================

mostrar_inicio()

ventana.mainloop()


