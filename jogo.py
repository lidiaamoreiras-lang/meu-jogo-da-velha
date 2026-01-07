from pyscript import Element

turno = "X"
tabuleiro = [""] * 9
jogo_ativo = True

def jogar(posicao):
    global turno, jogo_ativo
    
    # Se o quadrado já estiver ocupado ou o jogo acabou, não faz nada
    if tabuleiro[posicao] != "" or not jogo_ativo:
        return
    
    # Marca a jogada no tabuleiro e na tela
    tabuleiro[posicao] = turno
    botao = Element(str(posicao)).element
    botao.innerText = turno
    
    # Verifica se houve vencedor
    if verificar_vencedor():
        Element("status").element.innerText = f"🎉 Vitória do {turno}!"
        jogo_ativo = False
    elif "" not in tabuleiro:
        Element("status").element.innerText = "🤝 Empate!"
        jogo_ativo = False
    else:
        # Muda o turno
        turno = "O" if turno == "X" else "X"
        Element("status").element.innerText = f"Vez do: {turno}"

def verificar_vencedor():
    # Combinações para ganhar (linhas, colunas e diagonais)
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for v in vitorias:
        if tabuleiro[v[0]] == tabuleiro[v[1]] == tabuleiro[v[2]] != "":
            return True
    return False

def reiniciar():
    global turno, tabuleiro, jogo_ativo
    turno = "X"
    tabuleiro = [""] * 9
    jogo_ativo = True
    Element("status").element.innerText = "Vez do: X"
    for i in range(9):
        Element(str(i)).element.innerText = ""