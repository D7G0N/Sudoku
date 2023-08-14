import solve
import PySimpleGUI as sg

from fontTools.ttLib import TTFont
#font1 = TTFont('Anonymous.ttf')
#font1.save()

S = 15

font1 = ('Anonymous', 10)
sg.set_options(font=font1)

layout = [
    [sg.Button("Load New", key = '-LOAD-')],
    [sg.Multiline('', key = '-PROBLEM-', size = (S * 2, S)), sg.Multiline('', key = '-SOLUTION-', size = (S * 2, S))]
]

window = sg.Window('Sudoku', layout)

while True:

    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == '-LOAD-':
        solution = solve.create()
        window['-SOLUTION-'].update(solve.printSudoku(solution))

        problem = solve.simplify(solution)
        window['-PROBLEM-'].update(solve.printSudoku(problem))
    print(event, values)