#calcular BF RUDIMENTAR
import PySimpleGUI as sg
import os
sg.theme('Dark Brown 1')

# Layout do programa

layout = [
    [sg.Text('Digite seu nome:')],
    [sg.Input()],
    [sg.Text('Digite sua altura em metros (Ex:1.75):')],
    [sg.Input()],
    [sg.Text('Digite seu peso:')],
    [sg.Input()],
    [sg.Text('Digite sua idade:')],
    [sg.Input()],
    [sg.Text('Sexo:')],
    [sg.Combo(['Masculino', 'Feminino'])],
    [sg.Text('Escolha o nivel de sua atividade física semanal.')],
    [sg.Combo(['Sedentário', '1 a 3 dias/semana', '3 a 5 dias/semana', '6 a 7 dias/semana', '2x ao dia(treinos pesados)'])],
    [sg.OK()]
]

window = sg.Window('Calculadora', layout)
def iniciar():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        sg.Popup(f' Seu nome é: {values[0]}\n Sua altura é: {values[1]} m\n Seu peso é: {values[2]} kg\n Você tem: {values[3]} anos\n Você é do sexo: {values[4]}')

    # A função a cima manda um popup identificando o usuario.

        if values[4] == 'Masculino':
            values[4] = 1
        elif values[4] == 'Feminino':
            values[4] = 0

    # A função a cima manda um popup na aba de sexo se o usuario não colocar uma opção válida e fecha o programa, alem disso aceita com iniciais maiusculas ou minusculas

        if values[5] == 'Sedentário':
            values[5] = 1.2
        elif values[5] == '1 a 3 dias/semana':
            values[5] = 1.375
        elif values[5] == '3 a 5 dias/semana':
            values[5] = 1.55
        elif values[5] == '6 a 7 dias/semana':
            values[5] = 1.725
        elif values[5] == '2x ao dia(treinos pesados)':
            values[5] = 1.9

    # Listas
        lista_altura = []
        lista_peso = []
        lista_idade = []
        lista_sexo = []
        lista_atividade = []
    # Adicionando elementos à lista
        lista_altura.append(values[1])
        lista_peso.append(values[2])
        lista_idade.append(values[3])
        lista_sexo.append(values[4])
        lista_atividade.append(values[5])
    # adicionei os valores a lista pra ficar mais facil de operar
        for i in lista_altura:
            altura= float(i)
        for i in lista_peso:
            peso = float(i)
        for i in lista_idade:
            idade = float(i)
        for i in lista_sexo:
            sexo = float(i)
        for i in lista_atividade:
            atividade = float(i)
    # Converti os elementos para float, para que seja possivel operar.
        imc = peso / (altura * altura)
        bf = (1.20 * imc) + (0.23 * idade) - (10.8 * sexo) - 5 * 4
        sg.popup(f' {values[0]}Seu BF é de: {bf:.2f}%\n Seu IMC está em:{imc:.2f}kg/m²')
        tmb_H = 66 + (13.7 * peso) + (5 * (altura * 100)) - (6.8 * idade)
        tmb_M = 655 + (9.6 * peso) + (1.8 * (altura * 100)) - (4.7 * idade)
    # Sexo masculino e suas atividades
        if sexo == 1 and atividade == 1.2:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_H}\n Sua NDC é de {tmb_H * 1.2:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.2) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.2) - 400.00:.2f} Kcal/dia')
        elif sexo == 1 and atividade == 1.375:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_H}\n Sua NDC é de {tmb_H * 1.375:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.375) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.375) - 400.00:.2f} Kcal/dia')
        elif sexo == 1 and atividade == 1.55:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_H}\n Sua NDC é de {tmb_H * 1.55:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.55) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.55) - 400.00:.2f} Kcal/dia')
        elif sexo == 1 and atividade == 1.725:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_H}\n Sua NDC é de {tmb_H * 1.725:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.725) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.725) - 400.00:.2f} Kcal/dia')
        elif sexo == 1 and atividade == 1.9:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_H}\n Sua NDC é de {tmb_H * 1.9:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.9) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.9) - 400.00:.2f} Kcal/dia')
    # Sexo feminino e suas respectivas atividades físicas
        if sexo == 0 and atividade == 1.2:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_M}\n Sua NDC é de {tmb_H * 1.2:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.2) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.2) - 400.00:.2f} Kcal/dia')
        elif sexo == 0 and atividade == 1.375:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_M}\n Sua NDC é de {tmb_H * 1.375:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.375) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.375) - 400.00:.2f} Kcal/dia')
        elif sexo == 0 and atividade == 1.55:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_M}\n Sua NDC é de {tmb_H * 1.55:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.55) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.55) - 400.00:.2f} Kcal/dia')
        elif sexo == 0 and atividade == 1.725:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_M}\n Sua NDC é de {tmb_H * 1.725:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.725) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.725) - 400.00:.2f} Kcal/dia')
        elif sexo == 0 and atividade == 1.9:
            sg.popup(f' {values[0]} sua Taxa de Metabolismo Basal é de: {tmb_M}\n Sua NDC é de {tmb_H * 1.9:.2f} Kcal/dia\n Para ganhar peso você precisará ingerir: {(tmb_H * 1.9) + 400:.2f} Kcal/dia\n Para perder peso você precisará ingerir:{(tmb_H * 1.9) - 400.00:.2f} Kcal/dia')

    # Variavel de IMC e risco de obesidade

        if imc < 18.5:
            sg.popup('Você está a baixo do peso ATENÇÃO!')
        elif imc >= 18.5 and imc < 24.9:
            sg.popup('Você está com o peso ideal!')
        elif imc >= 24.9 and imc <= 30:
            sg.popup('Você está a cima do peso!')
        elif imc > 30:
            sg.popup('Você pode estar em situação de obesidade ATENÇÃO!')
        sg.popup(f'Você possui {peso * (imc /100):.2f} kg de gordura em seu corpo, e {peso - peso * (imc /100 ):.2f} kg de massa magra.')

iniciar()
#Neste escopo estão todos os calculos.
window.close()
#TMB Mulher = 655 + (9,6 * P) + (1,8 * A) – (4,7 * I)
#TMB Homem = 66 + (13,7 * P) + (5 * A) – (6,8 * I)