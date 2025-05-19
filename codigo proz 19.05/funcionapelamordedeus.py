usuarios = []

# Carrega os nomes salvos no CSV
try:
    with open("base_dados.csv", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith("seja bem vindo(a) "):
                nome = linha.replace("seja bem vindo(a) ", "").replace(".", "")
                if nome and nome not in usuarios:
                    usuarios.append(nome)
except FileNotFoundError:
    pass  # Se o arquivo não existir ainda, os trem continua

def responder_usuario(pergunta):
    pergunta = pergunta.lower()  # converte pergunta pra minusculo

    if "oi" in pergunta or "olá" in pergunta:
        return "oi! Gostaria de ver o menu?"
    elif "menu" in pergunta or "sim" in pergunta or "claro" in pergunta or "yes" in pergunta:
        return (
            "\n--- MENU ---\n"
            "1. Adicionar usuário\n"
            "2. Checar usuário\n"
            "3. Sair\n"
            "digite a opção desejada:"
        )
    elif pergunta == "1":
        nome = input("Digite o nome para adicionar: ").strip()
        if nome:
            if nome in usuarios:
                return f"{nome} já está na lista."
            else:
                usuarios.append(nome)
                # -------> !!!!!! Salva no arquivo CSV !!!!! <------ *importante*
                with open("base_dados.csv", "a") as arquivo:
                    arquivo.write(f"seja bem vindo(a) {nome}.\n")
                return f"{nome} adicionado com sucesso!"
        else:
            return "nome inválido."
    elif pergunta == "2":
        nome = input("Digite o nome pra verificar: ").strip()
        if nome in usuarios:
            return f"{nome} está cadastrado."
        else:
            return f"{nome} não está cadastrado."
    elif pergunta == "3" or "sair" in pergunta :
        return "sair"
    else:
        return "não entendi. Você deseja ver o menu?"

# Loop principal
while True:
    entrada = input("Você: ")
    resposta = responder_usuario(entrada)
    if resposta == "sair":
        print("chatbot: Até mais!")
        break
    print(f"chatbot: {resposta}")
