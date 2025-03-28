from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class CustomToolbar(NavigationToolbar2Tk):
    # Apenas o botão "Save" será exibido
    toolitems = (
        ('Save', 'Salvar o gráfico', 'filesave', 'save_figure'),
    )