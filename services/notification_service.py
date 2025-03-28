from win10toast import ToastNotifier

# Cria uma instância global do ToastNotifier
notifier = ToastNotifier()

def notify_connection_lost(duration=15):
    """
    Exibe uma notificação do Windows informando que a conexão foi perdida.
    """
    notifier.show_toast("Alerta", "A conexão com a internet foi perdida", duration=duration, threaded=True)