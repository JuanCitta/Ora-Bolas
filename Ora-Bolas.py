import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import time
# A velocidade inicial do robô é zero
velocidade_atual_do_robô = 0
# A aceleração do robô (ajuste conforme necessário)
aceleracao_robô = 0.41208
velocidade_maxima = 3
# A posição final da bola (ponto fixo P2)
x_meta, y_meta = 6.56914176, 5.992032
print("Escolha o grafico que deve ser mostrado na telaz\n")
print("1 para o grafico da posicao da bola em X e Y")
print("2 para o grafico da velocidade da bola em X e Y")
print("3 para o grafico da aceleracao da bola em X e Y")
print("4 para o grafico da trajetoria da bola")
escolha = int(input("Digite a opcao desejada: "))

# Função para calcular a distância entre dois pontos
def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Função para calcular a posição do robô com aceleração até atingir a velocidade máxima
def calcular_posicao_robo(x_robô, y_robô, x_meta, y_meta, delta_t, velocidade, aceleracao, velocidade_maxima):
    distancia_ate_meta = calcular_distancia(x_robô, y_robô, x_meta, y_meta)
    nova_velocidade = velocidade + aceleracao * delta_t
    nova_velocidade = min(nova_velocidade, velocidade_maxima)

    # Distância percorrida com base na nova velocidade
    distancia_percorrida = (velocidade + nova_velocidade) / 2 * delta_t

    # Verificar se o robô chegou ou ultrapassou a meta
    if distancia_percorrida >= distancia_ate_meta:
        return x_meta, y_meta, nova_velocidade

    # Calcular o percentual do caminho percorrido
    percentual = distancia_percorrida / distancia_ate_meta

    # Calcular as novas coordenadas do robô
    x_novo = x_robô + percentual * (x_meta - x_robô)
    y_novo = y_robô + percentual * (y_meta - y_robô)

    return x_novo, y_novo, nova_velocidade

if escolha == 1:
    Ball_posX = []
    Ball_posY = [] 
    new_list = np.arange(0, 20.02, 0.02).tolist()

    with open('trajetoria_da_bola.txt', 'r') as file:
        linhas = file.read().splitlines()

        # The following loop should be inside the 'with open' block
        for line in linhas[1:]:  
            t, x_ball, y_ball = map(lambda val: float(val.replace(',', '.')), line.split())
            Ball_posX.append(x_ball)
            Ball_posY.append(y_ball)

    # Construct the DataFrame after reading the file and processing the data
    df = pd.DataFrame(data={'Tempo em segundos': new_list, 
                        'Posicao da bola em Y': Ball_posY, 
                        'Posicao da bola em X': Ball_posX})

    fig, ax = plt.subplots(figsize=(20, 10)) 

    df.plot(x='Tempo em segundos', y='Posicao da bola em Y', ax=ax) 
    df.plot(x='Tempo em segundos', y='Posicao da bola em X', ax=ax, secondary_y=True) 
    plt.show()
    
elif escolha == 2:
    Vx_ball = []
    Vy_ball = []
    new_list = np.arange(0, 20, 0.02).tolist()
    
    with open('Vx_bola.txt', 'r') as file:
            linhas = file.read().splitlines()

        #'limpando' os dados para poderem ser usados pelo Python
    for line in linhas[1:]:  
        t, vx_ball, = map(lambda val: float(val.replace(',', '.')), line.split())
        #Criacao da lista com as velocidades da bola em X
        Vx_ball.append(vx_ball)

    with open('Vy_bola.txt', 'r') as file:
            linhas = file.read().splitlines()

        #'limpando' os dados para poderem ser usados pelo Python
    for line in linhas[1:]:  
        t, vy_ball, = map(lambda val: float(val.replace(',', '.')), line.split())
        #Criacao da lista com as velocidades da bola em Y
        Vy_ball.append(vy_ball)

    df = pd.DataFrame(data={'Tempo em segundos': new_list, 
                        'Velocidade da bola em Y': Vy_ball, 
                        'Velocidade da bola em X': Vx_ball})


    fig, ax = plt.subplots(figsize=(20,10)) 

    df.plot(x = 'Tempo em segundos', y = 'Velocidade da bola em Y', ax = ax) 
    df.plot(x = 'Tempo em segundos', y = 'Velocidade da bola em X', ax = ax, secondary_y = True) 
    plt.show()
    
elif escolha == 3:
    Acelx_Ball = []
    Acely_Ball = []
    new_list = np.arange(0, 20, 0.02).tolist()
    with open('Ax_bola.txt','r') as file:
        linhas = file.read().splitlines()

    #'limpando' os dados para poderem ser usados pelo Python
    for line in linhas[1:]:  
        t, Ax_ball = map(lambda val: float(val.replace(',', '.')), line.split())
        Acelx_Ball.append(Ax_ball)
        
    with open('Ay_bola.txt','r') as file:
        linhas = file.read().splitlines()

    #'limpando' os dados para poderem ser usados pelo Python
    for line in linhas[1:]:  
        t, Ay_ball = map(lambda val: float(val.replace(',', '.')), line.split())
        Acely_Ball.append(Ay_ball)
    #Usando o Panda para desenhar o grafico de aceleracao da bola
    df = pd.DataFrame(data={'Tempo em segundos': new_list, 
                        'Aceleracao da bola em Y': Acely_Ball, 
                        'Aceleracao da bola em X': Acelx_Ball})


    fig, ax = plt.subplots(figsize=(20,10)) 

    df.plot(x = 'Tempo em segundos', y = 'Aceleracao da bola em Y', ax = ax) 
    df.plot(x = 'Tempo em segundos', y = 'Aceleracao da bola em X', ax = ax, secondary_y = True) 
    plt.show()
elif escolha == 4:
     # Choice 4 for the trajectory graph
    new_list = np.arange(0, 20, 0.02).tolist()
    Traj_BolaX = []
    Traj_BolaY = []

    # Read the ball trajectory file
    with open('trajetoria_da_bola.txt', 'r') as file:
        linhas = file.read().splitlines()

        # Process data in the file
        for line in linhas[1:]:  
            t, pos_bolax, pos_bolay = map(lambda val: float(val.replace(',', '.')), line.split())
            Traj_BolaX.append(pos_bolax)
            Traj_BolaY.append(pos_bolay)

    # Construct the DataFrame after reading the file and processing the data
    df = pd.DataFrame(data={'Trajetoria da bola em X': Traj_BolaX, 
                            'Trajetoria da bola em Y': Traj_BolaY})
    
    fig, ax = plt.subplots(figsize=(20, 10)) 
    df.plot(x='Trajetoria da bola em X', y='Trajetoria da bola em Y', ax=ax) 
    plt.show()
    
elif escolha == 6:
    x_robô = float(input("Digite a posicao X incial do robo: "))
    y_robô = float(input("Digite a posicao Y incial do robo: "))

    #Declaracao de variaveis
    L_X_Robo_RD = []
    T_RD = []
    L_Y_Robo_RD = []
    x_meta, y_meta = 6.56914176, 5.992032
# Lendo e processando as posições da bola
    arquivo = open("trajetoria_da_bola.txt", "r")

# Variáveis de controle de tempo
    tempo_inicial = time.time()
    ultimo_tempo_atualizacao = tempo_inicial

    # Loop de leitura das posições da bola
    for linha in arquivo.readlines()[1:]:
        colunas = linha.strip().replace(',', '.').split()
        tempo_bola = float(colunas[0])
        x_bola = float(colunas[1])
        y_bola = float(colunas[2])

        tempo_atual = time.time()
        delta_t = tempo_atual - ultimo_tempo_atualizacao
        ultimo_tempo_atualizacao = tempo_atual

        x_robô, y_robô, velocidade_atual_do_robô = calcular_posicao_robo(x_robô, y_robô, x_meta, y_meta, delta_t, velocidade_atual_do_robô, aceleracao_robô, velocidade_maxima)
        L_X_Robo_RD.append(x_robô)
        T_RD.append(delta_t)
        L_Y_Robo_RD.append(y_robô)
        if calcular_distancia(x_robô, y_robô, x_bola, y_bola) <= 0.2:
            break

    
        time.sleep(0.02)  # Dorme por 20ms
    arquivo.close()
     #Usando o Panda para desenhar o grafico de aceleracao da bola
    df = pd.DataFrame(data={'Tempo em segundos': T_RD, 
                        'Posicao do robo em Y': L_Y_Robo_RD, 
                        'Posicao do robo em X': L_X_Robo_RD})


    fig, ax = plt.subplots(figsize=(20,10)) 

    df.plot(x = 'Tempo em segundos', y = 'Posicao do robo em Y', ax = ax) 
    df.plot(x = 'Tempo em segundos', y = 'Posicao do robo em X', ax = ax, secondary_y = True) 
    plt.show()

elif escolha == 7:
    L_X_Robo = []
    T = []
    L_Y_Robo = []

# Lendo e processando as posições da bola
    arquivo = open("ball_positions.txt", "r")

# Variáveis de controle de tempo
    tempo_inicial = time.time()
    ultimo_tempo_atualizacao = tempo_inicial

    # Loop de leitura das posições da bola
    for linha in arquivo.readlines():
        colunas = linha.strip().replace(',', '.').split()
        tempo_bola = float(colunas[0])
        x_bola = float(colunas[1])
        y_bola = float(colunas[2])

        tempo_atual = time.time()
        delta_t = tempo_atual - ultimo_tempo_atualizacao
        ultimo_tempo_atualizacao = tempo_atual

        x_robô, y_robô, velocidade_atual_do_robô = calcular_posicao_robo(x_robô, y_robô, x_meta, y_meta, delta_t, velocidade_atual_do_robô, aceleracao_robô, velocidade_maxima)
        L_X_Robo.append(x_robô)
        T.append(delta_t)
        L_Y_Robo.append(y_robô)
        if calcular_distancia(x_robô, y_robô, x_bola, y_bola) <= 0.2:
            break

    
        time.sleep(0.02)  # Dorme por 20ms
    arquivo.close()
