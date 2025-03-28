import threading
from services.network_service import monitor_network, latency_values, timestamps
from services.plot_service import plot_latency

if __name__ == "__main__":
    # Inicia o monitoramento da rede em uma thread separada
    monitor_thread = threading.Thread(target=monitor_network, daemon=True)
    monitor_thread.start()
    
    # Inicia a exibição do gráfico na thread principal
    plot_latency(timestamps, latency_values)