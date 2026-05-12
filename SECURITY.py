from cryptography.fernet import Fernet
import customtkinter as kc
from PIL import Image

App = kc.CTk()
App.after(0, lambda: App.state("zoomed"))
App.grid_columnconfigure(0, weight=1)
App.grid_rowconfigure(0, weight=1)

def generar_llave():
    llave_nueva = Fernet.generate_key().decode()
    Historial.configure(state="normal")
    Entry_Contraseña.delete(0, "end")
    Entry_Contraseña.insert(0, llave_nueva)
    Historial.insert("end", f"> NUEVA LLAVE MAESTRA GENERADA: {llave_nueva}\n")
    Historial.configure(state="disabled")
    Historial.see("end")

def guardar_datos():
    global token
    Contraseña = Entry_Contraseña.get()
    Account = Entry_Site.get()
    Password_ci = Entry_Site_pass.get()
    if Contraseña.strip() == "" or Account.strip() == "" or Password_ci.strip() == "":
        return
    llave = Contraseña.encode()
    f = Fernet(llave)
    token = f.encrypt(Password_ci.encode())

def ver_datos():
    llave_maestra = str(Entry_Contraseña.get())
    if llave_maestra.strip() == "":
        actualizar_log("ERROR: INGRESA LA ACCESS KEY PARA DESCIFRAR")
        return
    try:
        llave_bytes = llave_maestra.encode()
        f = Fernet(llave_bytes)
        password_descifrada = f.decrypt(token).decode()
        actualizar_log(f"ACCESO CONCEDIDO. CONTRASEÑA: {password_descifrada}")
    except Exception:
        actualizar_log("ALERTA: LLAVE MAESTRA INCORRECTA O DATOS CORRUPTOS")

def actualizar_log(mensaje):
    Historial.configure(state="normal")
    Historial.insert("end", f"> {mensaje}\n")
    Historial.configure(state="disabled")
    Historial.see("end")
    
FONT_ENTRY = kc.CTkFont(family="Consolas", size=15)
FONT_TITULO = kc.CTkFont(family="Agency FB", size=50, weight="bold")

Frame_Neon = kc.CTkFrame(
    App,
    width=900,
    height=700,
    corner_radius=20,
    fg_color="#0A0000",
    border_width=4,
    border_color="#FF0000",
)
Frame_Neon.grid(row=0, column=0, padx=20, pady=20)
Frame_Neon.grid_propagate(False)
Frame_Neon.grid_columnconfigure(0, weight=1)

Titulo = kc.CTkLabel(Frame_Neon, text="Security Dashboard", font=FONT_TITULO)
Titulo.grid(row=0, column=0, pady=20)

frame_r = kc.CTkFrame(Frame_Neon, width=800, height=200, fg_color="transparent")
frame_r.grid(row=1, column=0)
frame_r.grid_propagate(False)
frame_r.grid_columnconfigure((0, 1, 2), weight=1)

Calavera = Image.open("demon.png")
Calavera_Img_Pil = kc.CTkImage(
    light_image=Calavera, dark_image=Calavera, size=(200, 200)
)

Frame_Image = kc.CTkFrame(frame_r, width=300, height=300, fg_color="transparent")
Frame_Image.grid(row=0, column=1)

label_image = kc.CTkLabel(
    Frame_Image, text="", image=Calavera_Img_Pil, compound="center"
)
label_image.grid(row=0, column=0)

frame_entry = kc.CTkFrame(frame_r, width=200, height=200, fg_color="transparent")
frame_entry.grid(row=0, column=0)
frame_entry.grid_rowconfigure((0, 1, 2), weight=1)

label_entry = kc.CTkLabel(frame_entry, text="ACCESS KEY", font=FONT_ENTRY)
label_entry.grid(row=0, column=0, pady=20)

Entry_Contraseña = kc.CTkEntry(
    frame_entry, placeholder_text="Ingresa key: ", font=FONT_ENTRY
)
Entry_Contraseña.grid(row=1, column=0)

Boton_Generar = kc.CTkButton(
    frame_entry,
    text="Generar",
    command=generar_llave,
    fg_color="#b40505",
    hover_color="#7b0303",
    font=FONT_ENTRY,
)
Boton_Generar.grid(row=2, column=0, pady=20)

frame_VAULT = kc.CTkFrame(frame_r, width=200, height=200, fg_color="transparent")
frame_VAULT.grid(row=0, column=2)
frame_VAULT.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

titulo_VAULT = kc.CTkLabel(
    frame_VAULT, text="VAULT ACTIONS", font=(FONT_TITULO, 20, "bold")
)
titulo_VAULT.grid(row=0, column=0)

Entry_Site = kc.CTkEntry(frame_VAULT, placeholder_text="Ingresa ACC: ", font=FONT_ENTRY)
Entry_Site.grid(row=1, column=0, pady=5)

Entry_Site_pass = kc.CTkEntry(
    frame_VAULT, placeholder_text="Ingresa PASS: ", font=FONT_ENTRY,show="*"
)
Entry_Site_pass.grid(row=2, column=0, pady=5)

Boton_Guardar = kc.CTkButton(
    frame_VAULT,
    text="Guardar",
    command=guardar_datos,
    fg_color="#b40505",
    hover_color="#7b0303",
    font=FONT_ENTRY,
)
Boton_Guardar.grid(row=3, column=0, pady=5)

Boton_ver = kc.CTkButton(
    frame_VAULT,
    text="ver",
    command=ver_datos,
    fg_color="#b40505",
    hover_color="#7b0303",
    font=FONT_ENTRY,
)
Boton_ver.grid(row=4, column=0, pady=5)

Frame_Historial = kc.CTkFrame(Frame_Neon, width=800, height=300, fg_color="transparent")
Frame_Historial.grid(row=2, column=0, pady=30)

label_Historail = kc.CTkLabel(Frame_Historial, text="SISTEMA DE LOGS", font=FONT_TITULO)
label_Historail.grid(row=0, column=0)

Historial = kc.CTkTextbox(
    Frame_Historial,
    width=800,
    height=250,
    corner_radius=10,
    border_width=2,
    border_color="#FF0000",
    fg_color="#0D0000",
    text_color="#FF0000",
    font=kc.CTkFont(family="Consolas", size=13),
    scrollbar_button_color="#8B0000",
    scrollbar_button_hover_color="#FF0000",
    state="disabled",
)
Historial.grid(row=1, column=0, pady=10, padx=20)

App.mainloop()