import PySimpleGUI as sg


layout = [[sg.Text('名前は？'), sg.Input()],
          [sg.Text('性別は？'), sg.Input()],
          [sg.Button('決定'), sg.Button('終了')]]

window = sg.Window('sample', layout)

event, values = window.read()

window.close()
print(f'eventは{event}')
print(f'valuesは{values}')