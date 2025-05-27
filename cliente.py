# Importa os módulos necessários para comunicação de rede (socket) e execução paralela (threading)
import socket
import threading

# Função responsável por receber mensagens do servidor
def receber(cliente):
    while True:
        try:
            # Tenta receber uma mensagem do servidor (até 1024 bytes)
            mensagem = cliente.recv(1024).decode('utf-8')
            # Exibe a mensagem recebida no terminal
            print(mensagem)
        except:
            # Em caso de erro (como o servidor desconectar), exibe mensagem e fecha a conexão
            print("Conexão encerrada.")
            cliente.close()
            break  # Sai do loop

# Função principal que inicia o cliente
def main():
    # Cria um socket TCP/IP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta ao servidor no IP e porta especificados
    cliente.connect(('111.111.11.11', 60045))  # Altere para o IP do servidor na sua rede

    # Solicita ao usuário seu nome, que será usado para identificar mensagens
    nome = input("Seu nome: ")
    print("Conectado ao servidor. Digite 'sair' para encerrar.")

    # Cria e inicia uma thread separada para ouvir as mensagens do servidor
    thread_receber = threading.Thread(target=receber, args=(cliente,))
    thread_receber.start()

    # Loop principal para enviar mensagens ao servidor
    while True:
        # Lê a entrada do usuário
        mensagem = input()
        # Se o usuário digitar 'sair', encerra a conexão e o programa
        if mensagem.lower() == 'sair':
            cliente.close()
            break  # Sai do loop
        # Envia a mensagem ao servidor com o nome do usuário
        cliente.send(f"{nome}: {mensagem}".encode('utf-8'))

# Executa a função principal ao iniciar o script
main()
