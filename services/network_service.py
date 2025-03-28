import time
import datetime
from ping3 import ping
from services.notification_service import notify_connection_lost
from services.tray_service import update_tray_icon

# Variáveis globais para armazenar dados e o status de conexão
connection_lost = False
latency_values = []
timestamps = []

def monitor_network(host="8.8.8.8", interval=5):
    """
    Executa o ping a cada 5 segundos, atualiza as listas de latência e timestamps,
    dispara a notificação se a conexão for perdida e atualiza o ícone da bandeja.
    """
    global connection_lost
    while True:
        try:
            result = ping(host, unit="ms", timeout=2)
        except Exception as e:
            result = None

        now = datetime.datetime.now()
        timestamps.append(now)
        if result is None:
            latency_values.append(0)
            if not connection_lost:
                notify_connection_lost()  # Notifica a perda de conexão
            connection_lost = True
        else:
            latency_values.append(result)
            connection_lost = False

        # Atualiza o ícone da bandeja:
        # Se connection_lost for False, connection_ok será True (ícone verde);
        # se for True, o ícone ficará vermelho.
        update_tray_icon(not connection_lost)

        time.sleep(interval)