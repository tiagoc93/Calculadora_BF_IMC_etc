

import PySimpleGUI as sg
from Saude import bf_homem, bf_mulher, bf_dobra_mulher, bf_dobra_homem, tmb, imc



if __name__ == '__main__':
    sg.theme('BlueMono')
    # Nomes das Tabs internas e suas Funções

    tab1_layout = [
        [sg.T('Calculadora de "IMC".')],
        [sg.T('Altura:')], [sg.Input(key='Altura1')],
        [sg.T('Peso:')], [sg.Input(key='Peso1')],
        [sg.Button('Calcular', key='CalcularIMC'), sg.Button('Limpar', key='Clear1')],
    ]

    tab2_layout = [
        [sg.T('Calculadora de "BF" com Fita Métrica.')],
        [sg.T('Altura:')], [sg.Input(key='Altura2')],
        [sg.T('Cintura:')], [sg.Input(key='Cintura')],
        [sg.T('Pescoço:')], [sg.Input(key='Pescoço')],
        [sg.T('Quadril, (mulher):')], [sg.Input(key='Quadril')],
        [sg.Button('Calcular', key='CalcularBF'), sg.Button('Limpar', key='Clear2')],
    ]

    tab3_layout = [
        [sg.T('Calculadora de "BF" com Adipômetro (Pollock).')],
        [sg.T('Peito:')], [sg.Input(key='Peito')],
        [sg.T('Axilar:')], [sg.Input(key='Axilar')],
        [sg.T('Triceps:')], [sg.Input(key='Triceps')],
        [sg.T('Subescapular:')], [sg.Input(key='Subescapular')],
        [sg.T('Abdominal:')], [sg.Input(key='Abdominal')],
        [sg.T('Suprailiaca:')], [sg.Input(key='Suprailiaca')],
        [sg.T('Coxa:')], [sg.Input(key='Coxa')],
        [sg.T('Idade:')], [sg.Input(key='Idade1')],
        [sg.Button('Calcular', key='CalcularPollock'), sg.Button('Limpar', key='Clear3')]
    ]

    tab4_layout = [
        [sg.T('Calculadora de "TMB", (Taxa Metabólica Basal).')],
        [sg.T('Atividade:')], [sg.Combo(['Sedentário', 'Levemente Ativo', 'Moderadamente Ativo', 'Altamente Ativo', 'Extremamente Ativo'], key='Atividade')],
        [sg.T('Peso em kg:')], [sg.Input(key='Peso3')],
        [sg.T('Altura em M:')], [sg.Input(key='Altura3')],
        [sg.T('Idade:')], [sg.Input(key='Idade2')],
        [sg.Button('Calcular', key='CalcularTMB'), sg.Button('Limpar', key='Clear4')],
    ]

    # Layout Principal do Programa
    layout = [
        [sg.T('Bem vindo(a) ao Nutriam!')],
        [sg.Text('Nome do Paciente:')],
        [sg.Input(key='Nome')],
        [sg.Text('Sexo:')],
        [sg.Combo(['Homem', 'Mulher'], key='Sexo')],
        [sg.TabGroup([[sg.Tab('IMC', tab1_layout), sg.Tab('BF', tab2_layout), sg.Tab('Pollock', tab3_layout), sg.Tab('TMB', tab4_layout) ]])],
        [sg.Output(key='-DISPLAY-',size=(45, 5))]
    ]
    # Janela
    janela = sg.Window('Nutriam', layout)
    janela.read()
    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED:
            break
        sexo = (values['Sexo'])

        if event == 'CalcularBF' and sexo == 'Homem': # Fixed
            janela['-DISPLAY-'].update(' ')
            altura = float(values['Altura2'])
            cintura = float(values['Cintura'])
            pescoco = float(values['Pescoço'])
            try:
                bf_homem(altura,cintura,pescoco)
                print(bf_homem(altura,cintura,pescoco))
            except TypeError:
                print('Atenção, se o sexo for masculino, não pode ser preenchido o valor Quadril.')

        elif event == 'CalcularBF' and sexo == 'Mulher': # Fixed
            janela['-DISPLAY-'].update(' ')
            altura = float(values['Altura2'])
            cintura = float(values['Cintura'])
            pescoco = float(values['Pescoço'])
            quadril = float(values['Quadril'])
            try:
                bf_mulher(altura,cintura,pescoco,quadril)
                print(bf_mulher(altura,cintura,pescoco,quadril))
            except TypeError:
                print('Atenção se o sexo for feminino, é preciso preencher o valor Quadril.')

        elif event == 'CalcularIMC':      # Fixed
            janela['-DISPLAY-'].update(' ')
            altura = float(values['Altura1'])
            peso = float(values['Peso1'])
            imc(peso, altura)
            print(imc(peso,altura))


        elif event == 'CalcularPollock' and sexo == 'Homem': # Funcional
            janela['-DISPLAY-'].update(' ')
            peito = float(values['Peito'])
            axilar = float(values['Axilar'])
            triceps = float(values['Triceps'])
            subescapular = float(values['Subescapular'])
            abdominal = float(values['Abdominal'])
            suprailiaca = float(values['Suprailiaca'])
            coxa = float(values['Coxa'])
            idade = int(values['Idade1'])
            bf_dobra_homem(peito, axilar, triceps, subescapular, abdominal, suprailiaca, coxa, idade)
            print(bf_dobra_homem(peito, axilar, triceps, subescapular, abdominal, suprailiaca, coxa, idade))

        elif event == 'CalcularPollock' and sexo == 'Mulher': # Funcional
            janela['-DISPLAY-'].update(' ')
            peito = float(values['Peito'])
            axilar = float(values['Axilar'])
            triceps = float(values['Triceps'])
            subescapular = float(values['Subescapular'])
            abdominal = float(values['Abdominal'])
            suprailiaca = float(values['Suprailiaca'])
            coxa = float(values['Coxa'])
            idade = int(values['Idade1'])
            bf_dobra_mulher(peito, axilar, triceps, subescapular, abdominal, suprailiaca, coxa, idade)
            print(bf_dobra_mulher(peito, axilar, triceps, subescapular, abdominal, suprailiaca, coxa, idade))

        elif event == 'CalcularTMB': # Fixed
            janela['-DISPLAY-'].update(' ')
            atividade = (values['Atividade'])
            idade = int(values['Idade2'])
            altura = float(values['Altura3'])
            peso = float(values['Peso3'])
            tmb(atividade, peso, altura, idade, sexo)
            print(tmb(atividade,peso,altura, idade, sexo))

        elif event == 'Clear1' or event == 'Clear2' or event == 'Clear3' or event == 'Clear4':
            janela['-DISPLAY-'].update(' ')

















