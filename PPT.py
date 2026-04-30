import customtkinter as kc
import random as rd

App = kc.CTk()
kc.set_appearance_mode("dark")


App.after(0, lambda: App.state("zoomed"))
App.grid_columnconfigure((0, 1), weight=1)
App.grid_rowconfigure(0, weight=1)

Lista_Cpu = ["Piedra", "Papel", "Tijeras"]

def Juego():
    global Lista_Cpu
    Eleccion_Cpu = rd.choice(Lista_Cpu)
    Eleccion_Jugador = str(Lista_Opciones_1.get())

    
    Label_Elecciones.configure(text=f"Jugador: {Eleccion_Jugador}\nCPU: {Eleccion_Cpu}")

  
    if Eleccion_Cpu == Eleccion_Jugador:
        Label_resultado.configure(text="Empate")
        
    elif (Eleccion_Cpu == "Papel" and Eleccion_Jugador == "Piedra") or \
         (Eleccion_Cpu == "Piedra" and Eleccion_Jugador == "Tijeras") or \
         (Eleccion_Cpu == "Tijeras" and Eleccion_Jugador == "Papel"):
        Label_resultado.configure(text="Ganador CPU")
        
    else:
        Label_resultado.configure(text="Ganador Jugador")


Frame_Jugador_1 = kc.CTkFrame(
    App, width=500, height=400, corner_radius=25, border_width=2, border_color="#1F6AA5"
)
Frame_Jugador_1.grid(row=0, column=0, padx=20, pady=20)
Frame_Jugador_1.grid_propagate(False)
Frame_Jugador_1.grid_columnconfigure(0, weight=1)
Frame_Jugador_1.grid_rowconfigure((0, 1), weight=1)

Label_J1 = kc.CTkLabel(
    Frame_Jugador_1, text="TU ELECCIÓN", font=("Comic Sans MS", 24, "bold")
)
Label_J1.grid(row=0, column=0, pady=(20, 0))

Lista_Opciones_1 = kc.CTkOptionMenu(
    Frame_Jugador_1,
    values=["Piedra", "Papel", "Tijeras"],
    width=250,
    height=45,
    font=("Comic Sans MS", 18),
    fg_color="#1F6AA5",
    button_color="#144870",
    button_hover_color="#0E324F",
    corner_radius=10,
)
Lista_Opciones_1.grid(row=1, column=0, pady=(0, 40))


Frame_Jugador_2 = kc.CTkFrame(
    App, width=500, height=400, corner_radius=25, border_width=2, border_color="#E74C3C"
)
Frame_Jugador_2.grid(row=0, column=1, padx=20, pady=20)
Frame_Jugador_2.grid_propagate(False)
Frame_Jugador_2.grid_columnconfigure(0, weight=1)
Frame_Jugador_2.grid_rowconfigure((0, 1), weight=1)

Label_CPU = kc.CTkLabel(
    Frame_Jugador_2,
    text="RIVAL (CPU)",
    font=("Comic Sans MS", 24, "bold"),
    text_color="#E74C3C",
)
Label_CPU.grid(row=0, column=0, pady=(20, 0))

Resultado_CPU = kc.CTkLabel(
    Frame_Jugador_2, text="¿?", font=("Comic Sans MS", 80, "bold"), text_color="#555555"
)
Resultado_CPU.grid(row=1, column=0, pady=(0, 40))

Boton_Juego = kc.CTkButton(
    App, text="Juego", command=Juego, font=("Comic Sans MS", 30, "bold")
)
Boton_Juego.grid(row=0, column=0, columnspan=2)

frame_resultado = kc.CTkFrame(App, width=400, height=200)
frame_resultado.grid(row=3, column=0, columnspan=2, pady=20)
frame_resultado.grid_propagate(False)
frame_resultado.grid_columnconfigure(0, weight=1)

Label_Elecciones = kc.CTkLabel(
    frame_resultado, text="2", font=("Comic Sans MS", 30, "bold")
)
Label_Elecciones.grid(row=0, column=0, pady=30)

Label_resultado = kc.CTkLabel(
    frame_resultado, text="2", font=("Comic Sans MS", 30, "bold")
)
Label_resultado.grid(row=1, column=0)

App.mainloop()
