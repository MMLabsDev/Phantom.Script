import base64
import binascii
import os

os.system("")  # Activa los colores ANSI en la consola de Windows

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
    """ + RESET)


def imagen_a_base64(ruta_imagen, ruta_salida_txt=None):
    """Convierte una imagen a Base64. Si se da ruta_salida_txt, guarda el texto ahí."""
    with open(ruta_imagen, "rb") as f:
        datos_binarios = f.read()
    texto_base64 = base64.b64encode(datos_binarios).decode("utf-8")
    if ruta_salida_txt:
        with open(ruta_salida_txt, "w", encoding="utf-8") as f:
            f.write(texto_base64)
    return texto_base64


def base64_a_imagen(texto_base64, ruta_salida_imagen):
    """Reconstruye una imagen a partir de texto Base64."""
    datos_binarios = base64.b64decode(texto_base64)
    with open(ruta_salida_imagen, "wb") as f:
        f.write(datos_binarios)


def opcion_imagen_a_b64():
    ruta_imagen = input("Image route > ").strip().strip('"')
    print("Do you wish a name for your .txt? [YES] / [NO]")
    resp = input("> ").strip().lower()

    if resp in ("yes", "y"):
        name = input("Choose a name for your .txt > ").strip() or "foto"
    else:
        name = "foto"
    if not name.lower().endswith(".txt"):
        name += ".txt"

    try:
        b64 = imagen_a_base64(ruta_imagen, name)
        print(f"Image encoded -> {name}\n{b64[:50]} ...")
    except FileNotFoundError:
        print("File not found. Check the route.")
    except OSError as e:
        print(f"Could not read/write the file: {e}")


def opcion_b64_a_imagen():
    ruta_txt = input("Base64 file route > ").strip().strip('"')
    try:
        with open(ruta_txt, "r", encoding="utf-8") as f:
            texto_leido = f.read().strip()
    except FileNotFoundError:
        print("File not found. Check the route.")
        return
    except OSError as e:
        print(f"Could not read the file: {e}")
        return

    ruta_salida = input("Output image route (e.g. result.png) > ").strip().strip('"')
    if not ruta_salida:
        ruta_salida = "reconstruida.png"

    try:
        base64_a_imagen(texto_leido, ruta_salida)
        print(f"Image reconstructed successfully -> {ruta_salida}")
    except (binascii.Error, ValueError):
        print("The file does not contain valid Base64.")
    except OSError as e:
        print(f"Could not write the image: {e}")


def ayuda():
    print("Select Language [ES - EN]")
    idioma = input("> ").strip().lower()
    match idioma:
        case "es":
            print("""
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    -                      Phantom.Script                           -
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        Para usar Phantom, necesitas dos cosas; primero, la ruta de
        tu imagen .png (la puedes conseguir arrastrando y soltando
        la imagen aquí), y segundo, el nombre con el que desees que
        se guarde tu archivo .txt (aunque no es necesario, te lo
        recomiendo para evitar nombres repetidos).

        ‣ Para convertir imágenes a base64:
        Selecciona la opción 1, sube la ubicación de tu foto
        (recuerda que debe ser .png o .jpg), selecciona un nombre
        para tu archivo .txt (opcional) y haz enter.
        Encontrarás el .txt en la misma carpeta en la que tengas
        Phantom (por lo que te recomiendo tener una carpeta especial).

        ‣ Para convertir un base64 a imagen:
        Selecciona el archivo .txt del código base64 y sube su
        ubicación a Phantom. Selecciona un nombre para tu imagen
        reconstruida y encuéntrala en la misma carpeta
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
        must be .png or .jpg), choose a name for your .txt file
        (optional), and press enter. You will find the .txt in the
        same folder where you have Phantom (so I recommend having a special
        folder).

        ‣ To convert a base64 to an image:
        Select the .txt file with the base64 code and upload its location
        to Phantom. Choose a name for your reconstructed image
        and you will find it in the same folder where Phantom is located.

        • Good luck on your mission!
        """)
        case _:
            print("Invalid language. Use ES or EN.")


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    menu()
    while True:
        table()
        try:
            user = int(input("Select Function > "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if user == 1:
            opcion_imagen_a_b64()
        elif user == 2:
            opcion_b64_a_imagen()
        elif user == 3:
            ayuda()
        elif user == 4:
            limpiar_pantalla()
            menu()
        elif user == 5:
            print("Bye!")
            break
        else:
            print("Invalid option. Choose between 1 and 5.")


if __name__ == "__main__":
    main()
