import random
import time
import tkinter as tk
from tkinter import messagebox


class BuscaminasFrame(tk.Frame):

  def __init__(
      self,
      parent,
      filas=8,
      columnas=8,
      minas=10,
      on_game_over_callback=None,
  ):
    super().__init__(parent)
    self.parent = parent
    self.filas = filas
    self.columnas = columnas
    self.total_minas = minas
    self.on_game_over_callback = on_game_over_callback

    self.tablero = []
    self.botones = {}
    self.minas_pos = set()
    self.reveladas = 0
    self.tiempo_inicio = None
    self.juego_terminado = False

    self.crear_interfaz()
    self.iniciar_juego()

  def crear_interfaz(self):
    # Panel superior (Contadores)
    self.panel_superior = tk.Frame(self, bg="#2c3e50", pady=5)
    self.panel_superior.pack(side=tk.TOP, fill=tk.X)

    self.lbl_info = tk.Label(
        self.panel_superior,
        text=f"Minas: {self.total_minas}",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#2c3e50",
    )
    self.lbl_info.pack(side=tk.LEFT, padx=10)

    self.btn_reiniciar = tk.Button(
        self.panel_superior,
        text="🔄 Reiniciar",
        command=self.iniciar_juego,
        font=("Arial", 10, "bold"),
    )
    self.btn_reiniciar.pack(side=tk.RIGHT, padx=10)

    # Tablero de juego
    self.grid_frame = tk.Frame(self, bg="#bdc3c7")
    self.grid_frame.pack(side=tk.TOP, pady=10)

  def iniciar_juego(self):
    self.juego_terminado = False
    self.reveladas = 0
    self.tiempo_inicio = time.time()

    for btn in self.botones.values():
      btn.destroy()
    self.botones.clear()
    self.minas_pos.clear()

    todas_pos = [(r, c) for r in range(self.filas) for c in range(self.columnas)]
    self.minas_pos = set(random.sample(todas_pos, self.total_minas))

    for r in range(self.filas):
      for c in range(self.columnas):
        btn = tk.Button(
            self.grid_frame,
            width=3,
            height=1,
            font=("Arial", 11, "bold"),
            bg="#ecf0f1",
        )
        btn.bind(
            "<Button-1>",
            lambda e, fila=r, col=c: self.revelar_casilla(fila, col),
        )
        btn.bind(
            "<Button-3>", lambda e, fila=r, col=c: self.marcar_bandera(fila, col)
        )

        btn.grid(row=r, column=c, padx=1, pady=1)
        self.botones[(r, c)] = btn

  def contar_minas_adyacentes(self, r, c):
    cant = 0
    for dr in [-1, 0, 1]:
      for dc in [-1, 0, 1]:
        if dr == 0 and dc == 0:
          continue
        nr, nc = r + dr, c + dc
        if (nr, nc) in self.minas_pos:
          cant += 1
    return cant

  def revelar_casilla(self, r, c):
    if self.juego_terminado or self.botones[(r, c)]["state"] == "disabled":
      return

    if (r, c) in self.minas_pos:
      self.botones[(r, c)].config(text="💣", bg="#e74c3c")
      self.terminar_juego(ganado=False)
      return

    self.revelar_recursivo(r, c)

    casillas_objetivo = (self.filas * self.columnas) - self.total_minas
    if self.reveladas == casillas_objetivo:
      self.terminar_juego(ganado=True)

  def revelar_recursivo(self, r, c):
    if (r, c) not in self.botones or self.botones[(r, c)]["state"] == "disabled":
      return

    btn = self.botones[(r, c)]
    if btn["text"] == "🚩":
      return

    minas_alrededor = self.contar_minas_adyacentes(r, c)
    btn.config(state="disabled", relief=tk.SUNKEN, bg="#ffffff")
    self.reveladas += 1

    if minas_alrededor > 0:
      colores = {1: "blue", 2: "green", 3: "red", 4: "purple", 5: "maroon"}
      color = colores.get(minas_alrededor, "black")
      btn.config(text=str(minas_alrededor), fg=color)
    else:
      btn.config(text="")
      for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
          if dr == 0 and dc == 0:
            continue
          nr, nc = r + dr, c + dc
          if 0 <= nr < self.filas and 0 <= nc < self.columnas:
            self.revelar_recursivo(nr, nc)

  def marcar_bandera(self, r, c):
    if self.juego_terminado or self.botones[(r, c)]["state"] == "disabled":
      return

    btn = self.botones[(r, c)]
    if btn["text"] == "🚩":
      btn.config(text="", fg="black")
    elif btn["text"] == "":
      btn.config(text="🚩", fg="#e67e22")

  def terminar_juego(self, ganado):
    self.juego_terminado = True
    tiempo_total = int(time.time() - self.tiempo_inicio)

    for r, c in self.minas_pos:
      if ganado:
        self.botones[(r, c)].config(text="🚩", bg="#2ecc71")
      else:
        self.botones[(r, c)].config(text="💣", bg="#e74c3c")

    if ganado:
      score = max(1000 - (tiempo_total * 10), 100)
      messagebox.showinfo(
          "¡Victoria!",
          f"¡Felicidades! Ganaste en {tiempo_total} segundos.\nPuntaje:"
          f" {score}",
      )
      if self.on_game_over_callback:
        self.on_game_over_callback("Buscaminas", score)
    else:
      messagebox.showerror("Game Over", "¡Has tocado una mina!")


if __name__ == "__main__":
  root = tk.Tk()
  root.title("Buscaminas - Retro Arcade")
  juego = BuscaminasFrame(root, filas=8, columnas=8, minas=10)
  juego.pack(expand=True, fill="both")
  root.mainloop()