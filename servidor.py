import socket  # Importa biblioteca para sockets TCP/IP
import threading  # Importa biblioteca para rodar múltiplas threads simultâneas

# Lista para armazenar os clientes conectados
clientes = []

# Variável global para o socket do servidor (para poder fechar depois)
servidor = None

# Flag para controlar o loop principal do servidor
servidor_ativo = True

# Função para enviar a mensagem recebida para todos os outros clientes
def broadcast(mensagem, remetente):
    for cliente in clientes:
        if cliente != remetente:
            try:
                cliente.send(mensagem)  # Tenta enviar mensagem para o cliente
            except:
                # Caso falhe, fecha a conexão e remove da lista
                cliente.close()
                clientes.remove(cliente)

# Função para lidar com a comunicação de um único cliente
def lidar_com_cliente(cliente):
    while True:
        try:
            # Recebe mensagem do cliente
            mensagem = cliente.recv(1024)
            if not mensagem:  # Se não recebeu mensagem, cliente desconectou
                break
            # Mostra a mensagem no servidor (decodifica bytes para string)
            print(f"Mensagem recebida: {mensagem.decode('utf-8')}")
            # Envia a mensagem para os outros clientes
            broadcast(mensagem, cliente)
        except:
            # Remove cliente da lista em caso de erro
            if cliente in clientes:
                clientes.remove(cliente)
            cliente.close()
            break

# Função que fica escutando no terminal do servidor para comando de encerramento
def escutar_comandos():
    global servidor_ativo, servidor
    while True:
        comando = input()
        if comando.lower() == "sair":
            print("Comando de encerramento recebido.")
            servidor_ativo = False  # Altera flag para sair do loop principal
            # Fecha todas as conexões dos clientes
            for cliente in clientes:
                cliente.close()
            # Fecha o socket do servidor para liberar a porta
            servidor.close()
            break

# Função principal para iniciar o servidor
def iniciar_servidor():
    global servidor, servidor_ativo
    # Cria o socket do servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa o socket a um IP e porta (use IP válido para sua rede)
    servidor.bind(('111.111.11.11', 60045)) # Altere para o IP que deseja ser o servidor na sua rede
    servidor.listen()
    print("Servidor iniciado. Aguardando conexões...")
    print("Digite 'sair' para encerrar o servidor.")

    # Inicia uma thread separada para escutar comandos do terminal (como 'sair')
    thread_comandos = threading.Thread(target=escutar_comandos)
    thread_comandos.daemon = True  # Para a thread fechar junto com o programa
    thread_comandos.start()

    # Loop principal que aceita novos clientes enquanto servidor_ativo for True
    while servidor_ativo:
        try:
            cliente, endereco = servidor.accept()
            print(f"Cliente conectado: {endereco}")
            clientes.append(cliente)  # Adiciona cliente à lista
            # Cria uma thread para lidar com o cliente conectado
            thread = threading.Thread(target=lidar_com_cliente, args=(cliente,))
            thread.start()
        except OSError:
            # Essa exceção acontece quando o socket é fechado pelo escutar_comandos
            break

    print("Servidor encerrado.")

# Inicia o servidor
iniciar_servidor()
