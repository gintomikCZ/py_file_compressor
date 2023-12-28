import PySimpleGUI as sg
import zip_creator

label1 = sg.Text('Select files to compress:')
input1 = sg.Input(key='filesInput')
btn1 = sg.FilesBrowse('Choose', key="files")

label2 = sg.Text('Select destination folder:')
input2 = sg.Input(key="folderInput")
btn2 = sg.FolderBrowse('Choose', key="folder")

btn3 = sg.Button('Compress')
output = sg.Text('', key="output")

window = sg.Window('file compressor', layout=[
    [label1, input1, btn1],
    [label2, input2, btn2],
    [btn3, output ]
])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    zip_creator.make_archive(filepaths, folder)
    window['output'].update(value='compression completed')
    window['filesInput'].update(value='')
    window['folderInput'].update(value='')

window.close()