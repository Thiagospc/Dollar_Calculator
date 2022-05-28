import PySimpleGUI as sg
sg.theme("DarkBlue9")
from consome import v

lista = []

class DolarCalculator():
    
    def layout_layout():
        global layout
        layout = [
            [sg.Input(key="input_principal", size=(35,38))],
            [sg.Button('Calcular', size=(14, 2)), sg.Text(" "*25)],
            [sg.Button("US$"), sg.Text(" "), sg.Button("R$")],
            [sg.Output(size=(33,15))],
            [sg.Button('Exit')]
        ]

    
    layout_layout()

    def executa():
        window = sg.Window("Dollar Calculator", layout=layout, return_keyboard_events=True, margins=(0, 0), resizable=True, finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                arquivo = open("Valores.txt", "w+")
                for i in lista:
                    arquivo.write(i)
                sg.Popup("Suas pesquisas from salvas --> Valores.txt")
                break
            
            def updater():
                try:
                    if event == 'US$':
                        window['input_principal'].update("R$")
                    if event == 'R$':
                        window['input_principal'].update("US$")
                except TypeError:
                    print("TypeErro")


            updater()

            if event == "Calcular":
                
                def calculando():
                    try:
                        valor_input = values['input_principal']
                        #valor_input = str(valor_input)

                        if 'R$' in valor_input:
                            def dolar():
                                try:
                                    x = 0
                                    real = valor_input
                                    real = str(real)
                                    real = real.replace('R$', '')
                                    real = real.replace('.', '')
                                    real = real.replace(',', '.')
                                    
                                    try:
                                        real = float(real)
                                        x = real/v
                                        print(f"R${real} = US${x}\n")
                                        lista.append(f"R${real} = US${x}\n")
                                    except ValueError:
                                        print("Selecione um valor real")

                                except UnboundLocalError:
                                    print("Erro de variável (UnboundLocalError)")


                            dolar()
                        elif 'US$' in valor_input:

                            def reais():                    
                                try:
                                    dolar = valor_input
                                    dolar = str(dolar)
                                    dolar = dolar.replace('US$', '')
                                    dolar = dolar.replace('.', '')
                                    dolar = dolar.replace(',', '.')
                                    
                                    try:
                                        x = 0
                                        dolar = float(dolar)
                                        x = v*dolar
                                        print(f"US${dolar} = R${x}\n")
                                        lista.append(f"US${dolar} = R${x}\n")
                                    except ValueError:
                                        print("Selecione um valor real")

                                except UnboundLocalError:
                                    print("Erro de variável (UnboundLocalError)")
                            

                            reais()
                        
                        else:
                            print("Erro, Selecione 'US$' ou 'R$'")
                    
                    except KeyError:
                        print("erro KeyError")


                calculando()
        window.close()
    executa()
DolarCalculator()