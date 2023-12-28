import PySimpleGUI as sg

label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
btn1 = sg.FilesBrowse('Choose')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
btn2 = sg.FolderBrowse('Choose')

btn3 = sg.Button('Compress')

window = sg.Window('file compressor', layout=[
    [label1, input1, btn1],
    [label2, input2, btn2],
    [btn3]
])

window.read()
window.close()