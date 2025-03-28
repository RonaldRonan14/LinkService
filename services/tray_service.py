# services/tray_service.py
import os
import pystray
from PIL import Image, ImageDraw
import queue

# Fila para sinalizar a restauração da janela
restore_queue = queue.Queue()

# Variável global para manter referência ao ícone em execução
tray_icon = None

def create_tray_icon_image(connection_ok=True):
    """
    Cria uma imagem para o ícone da bandeja.
    Usa 'lightgreen' se a conexão estiver OK e 'red' se estiver sem internet.
    """
    width, height = 64, 64
    color = "lightgreen" if connection_ok else "red"
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    square_size = 20
    left = (width - square_size) // 2
    top = (height - square_size) // 2
    right = left + square_size
    bottom = top + square_size
    draw.rectangle((left, top, right, bottom), fill="white")
    return image

def on_tray_icon_clicked(icon, item):
    """
    Coloca um sinal na fila para restaurar a janela e encerra o ícone.
    """
    restore_queue.put("restore")
    icon.stop()

def exit_program(icon, item):
    """
    Encerra o ícone da bandeja e finaliza o programa.
    """
    icon.stop()
    os._exit(0)  # Força a finalização do processo

def start_tray_icon(connection_ok=True):
    """
    Inicia o ícone da bandeja com o ícone configurado de acordo com o status da conexão.
    """
    global tray_icon
    image = create_tray_icon_image(connection_ok)
    menu = pystray.Menu(
        pystray.MenuItem("Restaurar", on_tray_icon_clicked),
        pystray.MenuItem("Sair", exit_program)
    )
    tray_icon = pystray.Icon("latency_monitor", image, "LinkService", menu)
    tray_icon.run()

def update_tray_icon(connection_ok):
    """
    Se o tray_icon estiver em execução, atualiza o ícone com a nova cor.
    """
    global tray_icon
    if tray_icon is not None:
        tray_icon.icon = create_tray_icon_image(connection_ok)