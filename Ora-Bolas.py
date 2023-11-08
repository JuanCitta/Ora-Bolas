import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

print("Escolha o grafico que deve ser mostrado na telaz\n")
print("1 para o grafico da posicao da bola em X e Y")
print("2 para o grafico da velocidade da bola em X e Y")
print("3 para o grafico da aceleracao da bola em X e Y")
print("4 para o grafico da trajetoria da bola")
escolha = int(input("Digite a opcao desejada: "))


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
    
elif escolha == 5:
    X_Robo = []
Y_Robo = []
T = []

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x_robo = 33
y_robo = 9
velocidade_robo = 2.8  # m/s
aceleracao_robo = 2.8  # m/s^2
raio_interceptacao = 0.09  # 9.43 em m 

# lendo o trajetoria da bola
with open('trajetoria_da_bola.txt', 'r') as file:
    linhas = file.read().splitlines()

for line in linhas[1:]:
    t, x_ball, y_ball = map(lambda val: float(val.replace(',', '.')), line.split())

    distance_to_ball = distancia(x_robo, y_robo, x_ball, y_ball)
    tempo_robo_dist = math.sqrt((2 * distance_to_ball) / aceleracao_robo)

    # Calculando a nova posicao com a velocidade do robo
    new_x_robo = x_robo + (t / tempo_robo_dist) * velocidade_robo
    new_y_robo = y_robo + (t / tempo_robo_dist) * velocidade_robo

    X_Robo.append(new_x_robo)
    Y_Robo.append(new_y_robo)
    T.append(t)

# Creating the DataFrame for robot positions
df = pd.DataFrame(data={'Tempo em segundos': T, 
                        'Posicao do robo em X': X_Robo, })

# Plotting the data
fig, ax = plt.subplots(figsize=(20, 10)) 
df.plot(x='Tempo em segundos', y='Posicao do robo em X', ax=ax) 
plt.show()

df = pd.DataFrame(data={'Tempo em segundos': T, 
                        'Posicao do robo em Y': Y_Robo, })

# Plotting the data
fig, ax = plt.subplots(figsize=(20, 10)) 
df.plot(x='Tempo em segundos', y='Posicao do robo em Y', ax=ax) 
plt.show()


    