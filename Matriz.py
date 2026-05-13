import customtkinter as kc

Matriz_app = kc.CTk()
Matriz_app.after(0, lambda: Matriz_app.state("zoomed"))
Matriz_app.grid_columnconfigure(0, weight=1)
Matriz_app.grid_rowconfigure(0, weight=1)

FONT_ENTRY_MODERNA = kc.CTkFont(family="Consolas", size=14, weight="bold")


def GenerarMatriz():

    Columnas = int(Columnas_Entry.get())
    Filas = int(Filas_Entry.get())
    
    if Columnas > 11 or Filas > 11:
        return
    if Columnas == "" or Filas == "":
        return

    frame_entries_matriz = kc.CTkFrame(
        Frame_m, width=200, height=200, fg_color="transparent"
    )
    frame_entries_matriz.grid(row=0, column=0)

    for C in range(Columnas):
        for F in range(Filas):
            Matriz = kc.CTkEntry(
                frame_entries_matriz,
                width=10,
                height=10,
                placeholder_text="",
                font=FONT_ENTRY_MODERNA,
                border_width=1,
                corner_radius=2,
                fg_color="#04A404",
                border_color="#008F11",
                text_color="#00FF41",
                
                justify="center",
            )
            Matriz.grid(row=F, column=C, padx=1, pady=1)
            Matriz.insert("end",0)
    Columnas_Entry.delete(0,"end")
    Filas_Entry.delete(0,"end")
Main_Frame = kc.CTkFrame(
    Matriz_app,
    width=600,
    height=600,
    fg_color="#050505",
    border_width=2,
    border_color="#00FF41",
    corner_radius=15,
)
Main_Frame.grid(row=0, column=0)
Main_Frame.grid_propagate(False)
Main_Frame.grid_columnconfigure(0, weight=1)

Decoracion_Superior = kc.CTkFrame(
    Main_Frame, height=40, fg_color="#003311", corner_radius=0
)
Decoracion_Superior.grid(row=0, column=0, sticky="ew", padx=5, pady=(3, 0))

Titulo_Neon = kc.CTkLabel(
    Main_Frame,
    text="MATRIX_SUBSYSTEM_V2",
    text_color="#00FF41",
    font=("Consolas", 24, "bold"),
)
Titulo_Neon.grid(row=1, column=0, pady=20)

Borde_Interno = kc.CTkFrame(
    Main_Frame,
    width=540,
    height=450,
    fg_color="#0A0A0A",
    border_width=1,
    border_color="#008F11",
)
Borde_Interno.grid(row=2, column=0, pady=10)
Borde_Interno.grid_propagate(False)
Borde_Interno.grid_columnconfigure(1, weight=1)
Borde_Interno.grid_rowconfigure(0, weight=1)


Frame_Inputs = kc.CTkFrame(Borde_Interno, fg_color="transparent")
Frame_Inputs.grid(row=0, column=0, padx=20, pady=20)
Frame_Inputs.grid_columnconfigure(0, weight=1)

Filas_Entry = kc.CTkEntry(
    Frame_Inputs,
    placeholder_text="Ingresa #Filas",
    font=FONT_ENTRY_MODERNA,
    width=180,
    height=35,
    border_width=2,
    corner_radius=5,
    fg_color="#001100",
    border_color="#008F11",
    text_color="#00FF41",
    placeholder_text_color="#004411",
)
Filas_Entry.grid(row=0, column=0, pady=10)

Columnas_Entry = kc.CTkEntry(
    Frame_Inputs,
    placeholder_text="Ingresa #Columnas",
    font=FONT_ENTRY_MODERNA,
    width=180,
    height=35,
    border_width=2,
    corner_radius=5,
    fg_color="#001100",
    border_color="#008F11",
    text_color="#00FF41",
    placeholder_text_color="#004411",
)
Columnas_Entry.grid(row=1, column=0, pady=10)

Boton_Generar_Matriz = kc.CTkButton(
    Frame_Inputs,
    text="GENERAR MATRIZ",
    font=FONT_ENTRY_MODERNA,
    width=180,
    height=40,
    border_width=2,
    corner_radius=8,
    fg_color="#001100",
    border_color="#00FF41",
    text_color="#00FF41",
    hover_color="#003311",
    border_spacing=5,
    command=GenerarMatriz,
)
Boton_Generar_Matriz.grid(row=2, column=0, pady=20)

Frame_m = kc.CTkFrame(
    Borde_Interno,
    width=300,
    height=300,
    fg_color="#0D0D0D",
    border_width=1,
    border_color="#00FF41",
    corner_radius=10,
)
Frame_m.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
Frame_m.grid_propagate(False)
Frame_m.grid_rowconfigure(0, weight=1)
Frame_m.grid_columnconfigure(0, weight=1)


Matriz_app.mainloop()
