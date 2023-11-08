import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generating a list from 0 to 20 in steps of 0.02
new_list = np.arange(0, 20, 0.02).tolist()

print(len(new_list))



Ball_posX = []
Ball_posY = [] 
Vx_ball = []
Vy_ball = []

with open('Vx_bola.txt', 'r') as file:
        linhas = file.read().splitlines()

    #substituir "." por "."
for line in linhas[1:]:  
    t, vx_ball, = map(lambda val: float(val.replace(',', '.')), line.split())
    Vx_ball.append(vx_ball)

print(len(Vx_ball))

with open('Vy_bola.txt', 'r') as file:
        linhas = file.read().splitlines()

    #substituir "." por "."
for line in linhas[1:]:  
    t, vy_ball, = map(lambda val: float(val.replace(',', '.')), line.split())
    Vy_ball.append(vy_ball)

print(len(Vy_ball))
df = pd.DataFrame(data={'Tempo em segundos': new_list, 
                    'Velocidade da bola em Y': Vy_ball, 
                    'Velocidade da bola em X': Vx_ball})


fig, ax = plt.subplots(figsize=(20,10)) 

df.plot(x = 'Tempo em segundos', y = 'Velocidade da bola em Y', ax = ax) 
df.plot(x = 'Tempo em segundos', y = 'Velocidade da bola em X', ax = ax, secondary_y = True) 
plt.show()

