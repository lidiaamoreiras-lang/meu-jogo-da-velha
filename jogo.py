import random
from pyscript import Element

tabuleiro = [""] * 9
jogo_ativo = True

def jogar(posicao):
    global jogo_ativo
    
    # Se o lugar estiver ocupado ou o jogo acabou, não faz nada
    if tabuleiro[posicao] != "" or not jogo_ativo:
        return
    
    # Sua jogada (X)
    marcar_jogada(posicao, "X")
    
    if verificar_fim_de_jogo():
        return

    # Jogada do Robô (O) imediata
    jogada_do_robo()
    verificar_fim_de_jogo()

def marcar_jogada(posicao, player):
    tabuleiro[posicao] = player
    Element(f"q{posicao}").element.innerText = player

def jogada_do_robo():
    vazios = [i for i, x in enumerate(tabuleiro) if x == ""]
    if vazios and jogo_ativo:
        escolha = random.choice(vazios)
        marcar_jogada(escolha, "O")

def verificar_vencedor():
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for v in vitorias:
        if tabuleiro[v[0]] == tabuleiro[v[1]] == tabuleiro[v[2]] != "":
            return tabuleiro[v[0]]
    return None

def verificar_fim_de_jogo():
    global jogo_ativo
    vencedor = verificar_vencedor()
    status = Element("status").element
    
    if vencedor:
        status.innerText = f"🎉 Vitória do {vencedor}!"
        jogo_ativo = False
        return True
    elif "" not in tabuleiro:
        status.innerText = "🤝 Empate!"
        jogo_ativo = False
        return True
    return False

def reiniciar():
    global tabuleiro, jogo_ativo
    tabuleiro = [""] * 9
    jogo_ativo = True
    Element("status").element.innerText = "Sua vez (X)"
    for i in range(9):
        Element(f"q{i}").element.innerText = ""