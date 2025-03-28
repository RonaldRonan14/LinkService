import os
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from services.custom_toolbar import CustomToolbar
from services.tray_service import restore_queue

def on_close():
    # Fecha todas as janelas do Matplotlib e encerra o programa
    plt.close('all')
    os._exit(0)

def update_plot(fig, ax, line, timestamps, latency_values):
    # Define o limite: 2 minutos
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(minutes=2)

    # Filtra os dados para manter apenas os últimos 2 minutos
    filtered_timestamps = [t for t in timestamps if t >= cutoff]
    indices = [i for i, t in enumerate(timestamps) if t >= cutoff]
    filtered_latency = [latency_values[i] for i in indices]

    # Remove anotações anteriores
    for txt in ax.texts:
        txt.remove()
    
    # Atualiza os dados do gráfico com os dados filtrados
    line.set_data(filtered_timestamps, filtered_latency)
    for x, y in zip(filtered_timestamps, filtered_latency):
        ax.text(x, y, f"{y:.2f}", fontsize=8, ha='center', va='bottom')

    if filtered_latency:
        last_latency = filtered_latency[-1]
        if last_latency > 0 and last_latency < 100:
            line_color = 'green'
        elif last_latency > 0 and last_latency < 300:
            line_color = 'yellow'
        else:
            line_color = 'red'
        line.set_color(line_color)

    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

def on_minimize(event, fig):
    """
    Ao minimizar, oculta a janela e inicia o ícone da bandeja em uma nova thread.
    """
    window = plt.get_current_fig_manager().window
    if window.state() == 'iconic':
        window.withdraw()
        from services.tray_service import start_tray_icon
        from services.network_service import connection_lost
        import threading
        threading.Thread(target=start_tray_icon, args=(not connection_lost,), daemon=True).start()

def plot_latency(timestamps, latency_values, title="Monitor de Latência"):
    plt.ion()  # Modo interativo
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title("LinkService")
    fig.canvas.manager.window.state('zoomed')
    
    # Define o protocolo para fechar a janela
    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.protocol("WM_DELETE_WINDOW", on_close)

    ax.set_title(title)
    line, = ax.plot(timestamps, latency_values, marker='o', label="Latência (ms)")
    ax.set_xlabel("Hora")
    ax.set_ylabel("Latência (ms)")
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    fig.autofmt_xdate()

    # Substitua a toolbar padrão pela sua customizada
    manager = plt.get_current_fig_manager()
    if hasattr(manager, 'toolbar'):
        manager.toolbar.destroy()
    manager.toolbar = CustomToolbar(manager.canvas, manager.window)
    manager.toolbar.update()

    try:
        fig_manager.window.bind("<Unmap>", lambda event: on_minimize(event, fig))
    except Exception as e:
        print("Erro ao configurar evento de minimizar:", e)

    while True:
        update_plot(fig, ax, line, timestamps, latency_values)
        try:
            while True:
                task = restore_queue.get_nowait()
                if task == "restore":
                    fig_manager.window.deiconify()
        except Exception:
            pass
        time.sleep(1)