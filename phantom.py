import base64
import os

PURPLE = "\033[38;5;93m"
VIOLET = "\033[38;5;135m"
LAVENDER = "\033[38;5;183m"
RESET = "\033[0m"
def menu():
    print(
    PURPLE + r"""
    ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗     ████████
    ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║   ████████████
    ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║  ███  ███  ████
    ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║   ████████████
    ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║   ██ ██ ██ ██
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝    ██ ██ ██ ██
    """ + RESET
    + VIOLET + r"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """ + LAVENDER + r"""
                    PHANTOM.SCRIPT • V1.0
                        by M.MLabs.Dev
    """ + VIOLET + r"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """ + RESET
    )

def table():
    print(PURPLE + r"""
  ┌─[ MAIN MENU ]
  │
  ├── ∎ [01] Image -> B64
  ├── ∎ [02] B64 -> Image
  ├── ∎ [03] How use it?
  ├── ∎ [04] Reset
  ├── ∎ [05] Exit
  │
  └──[root@HAcker]─> _

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       SYSTEM STATUS: READY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """+ RESET)
def imagen_a_base64(ruta_imagen, ruta_salida_txt=None):
    with open(ruta_imagen, "rb") as f:
        datos_binarios = f.read()
    codificado = base64.b64encode(datos_binarios)
    texto_base64 = codificado.decode("utf-8")
    if ruta_salida_txt:
        with open(ruta_salida_txt, "w", encoding="utf-8") as f:
            return texto_base64

def base64_a_imagen(texto_base64, ruta_salida_imagen):
    datos_binarios = base64.b64decode(texto_base64)
    with open(ruta_salida_imagen, "wb") as f:
        f.write(datos_binarios)

# Ejemplo de uso
menu()
while True:
    table()
    user = int(input("Select Funtion > "))

    if user == 1:
        ruta_imagen = input("Image route > ").strip().strip('"')
        print("Do you wish a name for you .txt?")
        print("[YES] / [NO]")
        name = input("> ")
        if name.lower() == "yes":
            name = input("Chose a name for your .txt (is not necesary .txt)> ")
            b64 = imagen_a_base64(
                ruta_imagen,
                f"{name}.txt")
                    
            print(f"Image {name} encoded ",b64[:50], "...")
        else:
            b64 = imagen_a_base64(ruta_imagen, "foto.txt")
            print(f"Image encoded: {b64[:50]} ...")

    elif user == 2:
        ruta_txt = input("Base64 file route > ").strip().strip('"')

        with open(ruta_txt, "r", encoding="utf-8") as f:
            texto_leido = f.read()

        ruta_salida = input("Output image route > ").strip().strip('"')
        base64_a_imagen(texto_leido, ruta_salida)

        print("Image reconstructed successfully!")

    elif user == 3:
        print("Select Languaje [ES - EN]")
        idioma = input("> ")
        match idioma.lower():
            case "es":
                print("""
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    -                      Phantom.Script                           -
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        Para usar phatom, necesitas dos cosas; primero, la ruta de 
        tu imagen .png (la puedes conseguir arrastrando y soltando 
        la imagen aquí), y segundo, el nombre con el que desees que 
        se guarde tu archivo.txt (aunque no es necesario, te lo 
        recomiendo para evitar nombres repetidos).

        ‣ Para convertir imagenes a base64:
        Selecciona la opción 1, sube la ubicación de tu foto 
        (recuerda que debe ser .png o .jpg), selecciona un nombre 
        para tu archivo con el contenido .txt (opcional) y haz enter.
        Encontrarás el .txt en la misma carpeta en la que tengas 
        Phantom (por lo que te recomiendo tener una carpeta especial)

        ‣ Para convertir un base64 a imagen:
        Selecciona el archivo .txt del código base64 y sube su 
        ubicación a Phantom. Seleciona un nombre para tu imagen 
        reconstruida (opcional) y ecuentrala en la misma carpeta 
        en la que se encuentra Phantom.

        • ¡Suerte en tu misión!
        """)

            case "en":
                print("""
            ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
            -                      Phantom.Script                           -
            ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
            To use Phantom, you need two things; first, the path to your .png 
            image (you can get it by dragging and dropping the image here), 
            and second, the name you want your .txt file to be saved as 
            (although not necessary, I recommend it to avoid duplicate names).

            ‣ To convert images to base64:
            Select option 1, upload the location of your photo (remember it 
            must be .png or .jpg), choose a name for your file with the .txt 
            content (optional), and press enter. You will find the .txt in the 
            same folder where you have Phantom (so I recommend having a special 
            folder).

            ‣ To convert a base64 to an image:
            Select the .txt file with the base64 code and upload its location 
            to Phantom. Choose a name for your reconstructed image (optional) 
            and you will find it in the same folder where Phantom is located.

            • Good luck on your mission!""")

    elif user == 4:
        continue

    elif user == 5:
        break
