# Socket

💬 Chat TCP com Python (Cliente/Servidor)

Este projeto implementa uma aplicação de **chat em rede** utilizando **sockets TCP** e **multithreading** em Python. Ele permite que múltiplos clientes se conectem a um servidor central e troquem mensagens em tempo real.

## 📁 Arquivos

- `servidor.py`: Código do servidor responsável por aceitar conexões e redirecionar mensagens entre os clientes.
- `cliente.py`: Código do cliente, responsável por se conectar ao servidor e enviar/receber mensagens.

---

## 🔧 Requisitos

- Python 3.x
- Ambiente de rede (mesma LAN ou IP público com redirecionamento de porta)
- Bibliotecas padrão:
  - `socket`
  - `threading`

### 📦 Como importar as bibliotecas no seu código

Para usá-las, basta importar assim:

```python
import socket
import threading
```


## Como gerar o arquivo `.exe`

Para gerar o executável dos scripts, siga os passos:

1. Instale o PyInstaller (caso ainda não tenha):

```bash
pip install pyinstaller
```

Se o comando acima não funcionar, tente:

```bash
python -m pip install pyinstaller
```

2. Para gerar o `.exe` do cliente:

```bash
pyinstaller --onefile cliente.py
```

3. Para gerar o `.exe` do servidor:

```bash
pyinstaller --onefile servidor.py
```

4. Os arquivos executáveis ficarão na pasta `dist`.

---

## Como usar

- Execute primeiro o servidor: `servidor.exe`
- Depois execute o cliente: `cliente.exe`

---

