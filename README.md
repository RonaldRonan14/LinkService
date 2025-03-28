# LinkService - Monitoramento de Conexão de Internet

![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)

## 📌 Descrição

O **LinkService** é um programa desenvolvido em **Python** para monitorar a latência e a disponibilidade da conexão com a internet. Ele permite acompanhar a estabilidade da rede em tempo real, fornecendo gráficos interativos e notificações quando a conexão cair.

## ✨ Funcionalidades

✅ Monitoramento contínuo da latência da internet.  
✅ Emissão automática de alertas quando o link estiver fora do ar.  
✅ Gráficos interativos para exibição da latência em tempo real.  
✅ Ícone na bandeja do sistema que indica o status da conexão.  

## 🛠 Estrutura do Projeto

```
LinkService/
│── app.py                     # Inicializa o monitoramento e exibe o gráfico
│
├── services/                   # Serviços do programa
│   ├── custom_toolbar.py        # Personaliza a barra de ferramentas do gráfico
│   ├── network_service.py       # Monitora a latência da rede
│   ├── notification_service.py  # Envia notificações ao usuário
│   ├── plot_service.py          # Exibe os gráficos da latência
│   ├── tray_service.py          # Gerencia o ícone da bandeja do sistema
│
├── README.md                    # Documentação do projeto
└── requirements.txt              # Dependências do projeto
```

## 🔄 Fluxo de Execução

1. O **`app.py`** inicia o monitoramento da rede em uma **thread separada**.
2. O **`plot_service.py`** exibe um gráfico atualizado em tempo real com a latência da conexão.
3. O **`network_service.py`** envia **pings periódicos** para medir a latência e atualiza o ícone da bandeja:
   - **Verde**: Conexão estável.
   - **Vermelho**: Conexão perdida.
4. Caso a conexão caia, o **`notification_service.py`** exibe um alerta ao usuário.
5. O ícone da bandeja pode ser usado para **restaurar a interface gráfica** ou **fechar o programa**.

## 🚀 Instalação

### 🔧 Requisitos

- Python **3.13+**
- Pip instalado

### 📥 Instalando as Dependências

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/LinkService.git
   cd LinkService
   ```
2. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

Para iniciar o **LinkService**, execute o seguinte comando:

```bash
python app.py
```

O monitoramento será iniciado em segundo plano, e o **ícone na bandeja do sistema** indicará o status da conexão.

## 🖥️ Tecnologias Utilizadas

- **Python** - Linguagem principal do projeto.
- **Matplotlib** - Utilizado para a geração dos gráficos.
- **ping3** - Biblioteca para monitoramento da latência da conexão.
- **win10toast** - Responsável pelas notificações no Windows.
- **pystray** - Gerenciamento do ícone na bandeja do sistema.
