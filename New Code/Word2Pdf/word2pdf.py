from main import *
import os
import PySimpleGUI as sg
### Imports ####

def main():
    Layout = [ [sg.Text('Hello From PDF converter, Please Provide the .docx to convert to .PDF')] ,
            [sg.Input(key='file_path'), sg.FileBrowse()],
            [sg.Checkbox('Open the converted file in the default PDF viewer', key='open', default=False)],
            [sg.OK(), sg.Cancel()]]

    window = sg.Window('PDF Converter', layout=Layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel', sg.WINDOW_CLOSED):
            break
        elif event in ('OK'):
            file_path = os.path.normpath(values['file_path'])
            make_pdf_(file_path, open_=values['open'])
            sg.popup('pdf made !')
            break
        else:
            sg.popup('An Error Occoured')
            break

if __name__ == "__main__":
    main()