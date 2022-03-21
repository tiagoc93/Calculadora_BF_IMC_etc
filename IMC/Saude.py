"""
Calculos Úteis de Saúde
"""
"""
# ----------INDICE DE MASSA CORPORAL (IMC)---------- #
"""
if __name__ != '__main__':
    def imc(peso,altura):
        try:
            resultado_imc = peso / altura ** 2
        except ZeroDivisionError:
            return 'Atenção, Valores peso e altura não podem ser iguais a 0\nFechando Programa...'
        except TypeError:
            return 'Não utilize Palavras, somente números \nFechando Programa...'
        else:
            if resultado_imc <= 18.5:
                return f'Seu IMC é {resultado_imc:.2f} kg/m²\nSituação: Magreza\nGrau de Obesidade: 0'
            elif resultado_imc > 18.5 and resultado_imc <= 24.9:
                return f'Seu IMC é {resultado_imc:.2f} kg/m²\nSituação: Normal\nGrau de Obesidade: 0'
            elif resultado_imc > 24.9 and resultado_imc <= 29.9:
                return f'Seu IMC é {resultado_imc:.2f} kg/m²\nSituação: Sobrepeso\nGrau de Obesidade: 1'
            elif resultado_imc > 29.9 and resultado_imc <= 39.9:
                return f'Seu IMC é {resultado_imc:.2f} kg/m²\nSituação: Obesidade\nGrau de Obesidade: 2'
            else:
                return f'Seu IMC é {resultado_imc:.2f} kg/m²\nSituação: Obesidade Grave\nGrau de Obesidade: 3'

    #print(imc(83, 1.68))
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    """
    # ----------TAXA METABÓLICA BASAL---------- #
    """
    def tmb(atividade,peso,altura, idade, sexo):
        altura = altura * 100
        if atividade == 'Sedentário':
            atividade = 1.2
        elif atividade == 'Levemente Ativo':
            atividade = 1.375
        elif atividade == 'Moderadamente Ativo':
            atividade = 1.55
        elif atividade == 'Altamente Ativo':
            atividade = 1.725
        elif atividade == 'Extremamente Ativo':
            atividade = 1.9
        else:
            return 'Digite Atividade Válida'
        if sexo == 'Homem':
            try:
                resultado_tmb_h = atividade * (66 + (13.7 * peso) + (5 * altura) - (6.8 * idade))
            except TypeError:
                return 'Por favor, Digite somente numeros neste campo.'
            return f'Sua Taxa Metabólica Basal é de: {round(resultado_tmb_h)} Kcal'
        elif sexo == 'Mulher':
            resultado_tmb_m = atividade * (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade))
            return f'Sua Taxa Metabólica Basal é de: {round(resultado_tmb_m)} Kcal'
        else:
            return 'Digite um Sexo Válido.'

    #print(tmb('Moderadamente Ativo', 83, 1.68, 28, 'Homem'))

    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    """
    # ----------BODY FAT ATRAVÉS DE ADIPÔMETRO (Pollock)---------- #
    """
    def bf_dobra_homem(peito, axilar, triceps, subescapular, abdominal, suprailiaca, coxa, idade):
        soma_dobra = peito + axilar + triceps + subescapular + abdominal + suprailiaca + coxa
        dc = 1.112 - (0.00043499 * soma_dobra) + (0.00000055 * soma_dobra ** 2) - (0.00028826 * idade) #Densidade Corporal
        bf_pollock = (495 / dc) - 450
        return f'Seu BF é {bf_pollock:.2f} %'

    #print(bf_dobra_homem(5, 5, 5, 5, 5, 5, 5, 28))

    def bf_dobra_mulher(peito, axilar, triceps, subescapular, abdominal, suprailiaca, coxa, idade):
        soma_dobraM = peito + axilar + triceps + subescapular + abdominal + suprailiaca + coxa
        dcM = 1.097 - (0.00046971 * soma_dobraM) + (0.00000056 * soma_dobraM ** 2) - (0.00012828 * idade) #Densidade Corporal
        bf_pollockM = (495 / dcM) - 450
        return f'Seu BF é {bf_pollockM:.2f} %'
    #print(bf_dobra_mulher(5, 5, 5, 5, 5, 5, 5, 28))


    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    """
    # ----------BODY FAT ATRAVÉS DE FITA MÉTRICA---------- #
    """
    from math import log
    from math import log10

    def bf_homem(altura,cintura,pescoco):
        try:
            resultado_bf_h = (86.010 * log10(cintura - pescoco) - 70.041 * log10(altura)) / 10
            return f'Seu BF é: {resultado_bf_h:.1f} %'
        except TypeError:
            return 'Somente numeros nesta função.\nFechando Programa...'
    def bf_mulher(altura,cintura,pescoco,quadril):
        try:
            altura = altura * 100
            resultado_bf_m = (495 / (1.296 - 0.350 * log10(quadril + cintura - pescoco) + 0.221 * log10(altura))) - 450
            return f'Seu BF é: {resultado_bf_m:.1f}%'
        except TypeError:
            return 'Somente numeros nesta função.\nFechando o Programa...'

    #print(bf_homem(1.65, 75, 38))
    #print(bf_mulher(1.65, 75, 38, 90))

    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
