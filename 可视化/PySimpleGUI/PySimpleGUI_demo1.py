import PySimpleGUI as sg      

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText(), sg.FileBrowse()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title').Layout(layout)    

event, values = window.Read()    
#window.Close()
window._Close()
source_filename = values[0]
print(source_filename)
print(event)
