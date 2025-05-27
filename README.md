# Socket

Projeto com scripts `cliente.py` e `servidor.py` para comunicação via sockets.

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

