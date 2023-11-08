if escolha == 6:
#     def distancia(x1, y1, x2, y2):
#         return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# x_robo = 33
# y_robo = 9
# velocidade_robo = 2.8  # m/s
# aceleracao_robo = 2.8  # m/s^2
# raio_interceptacao = 0.09  # 9.43 em m 

# # lendo o trajetoria da bola
# with open('trajetoria_da_bola.txt', 'r') as file:
#     linhas = file.read().splitlines()

# for line in linhas[1:]:
#     t, x_ball, y_ball = map(lambda val: float(val.replace(',', '.')), line.split())

#     distance_to_ball = distancia(x_robo, y_robo, x_ball, y_ball)
#     tempo_robo_dist = math.sqrt((2 * distance_to_ball) / aceleracao_robo)

#     # Calculando a nova posicao com a velocidade do robo
#     new_x_robo = x_robo + (t / tempo_robo_dist) * velocidade_robo
#     new_y_robo = y_robo + (t / tempo_robo_dist) * velocidade_robo

#     X_Robo.append(new_x_robo)
#     Y_Robo.append(new_y_robo)
#     T.append(t)

# # Creating the DataFrame for robot positions
# df = pd.DataFrame(data={'Tempo em segundos': T, 
#                         'Posicao do robo em X': X_Robo, })

# # Plotting the data
# fig, ax = plt.subplots(figsize=(20, 10)) 
# df.plot(x='Tempo em segundos', y='Posicao do robo em X', ax=ax) 
# plt.show()

# df = pd.DataFrame(data={'Tempo em segundos': T, 
#                         'Posicao do robo em Y': Y_Robo, })

# # Plotting the data
# fig, ax = plt.subplots(figsize=(20, 10)) 
# df.plot(x='Tempo em segundos', y='Posicao do robo em Y', ax=ax) 
# plt.show()