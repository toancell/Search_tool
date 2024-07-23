import PySimpleGUI as sg 
import os 
import shutil 
results =[]
layout = [
    [sg.Text("Search Term",size=(11,1)),sg.Input(size=(40,1),key="-TERM-"),sg.Radio("Contains", group_id ="search_type",key="-CONTAINS-")],
    [sg.Text("Search Path",size=(11,1)),sg.Input("/..",size=(40,1),key="-PATH-"),sg.FolderBrowse(),sg.Button("Search")],
    [sg.Text("Follow ig: toancell09.07 to book schedule a photo shoot or tiktok: Ngọc Toàn Tụp Ảnh",size=(80,1))],
    [sg.Listbox( values=results,size=(100,28),enable_events=True, key="-RESULTS-")]

]
window= sg.Window("File Search Engine", layout=layout, finalize= True, return_keyboard_events = True)
while True:
    event,values = window.read()
    if event is None: 
        break
    if event == "Search":
        term = values["-TERM-"].lower()
        folder_path = values["-PATH-"]
        results.clear()

        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root,file).replace("\\", "/")
                if term in file.lower():
                    results.append(file_path)
        
        window["-RESULTS-"].update(values =results)
    if event == "-RESULTS-" and values["-RESULTS-"] :
        full_name = values["-RESULTS-"][0]
        os.startfile(full_name)

        image_select_folder = os.path.join(folder_path, "Image_select")
        if not os.path.exists(image_select_folder):
            os.makedirs(image_select_folder)

        shutil.copy(full_name, image_select_folder)
window.close()
