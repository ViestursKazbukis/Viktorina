import PySimpleGUI as sg
from gtts import gTTS
import os

rez=0
datne='pd.txt'
dalas=[
    [sg.Text("Ievadi savu vārdu:"),sg.InputText(key="--vaards--")],
    [sg.T("Kas ir Latvijas valsts prezidents")],[sg.Button("Klausīties uzdevumu", size=(6,4))],
    [sg.Radio("Raimonds Vējonis",'Radio1', default=False, key="Vejonis"),sg.Radio("Edgars Rinkēvičs",'Radio2', default=False, key="Rinkevics")],
    [sg.Button('Iziet'), sg.Button('Turpināt viktorīnu')],
    [sg.Text(f"Jūsu rezultāts ir {rez}")],
]
logs = sg.Window("Viktorīna",dalas, size=(300, 200))
tts = gTTS(text="Kas ir Latvijas valsts prezidents", lang='lv')
tts.save("teksts.mp3")
while True: 
    event, values =logs.read()
    if event =="Klausīties uzdevumu":
         os.system("start teksts.mp3")
    if event == sg.WINDOW_CLOSED or event =='Iziet':
        break
    
         
    elif event == "Turpināt viktorīnu":
        vards=values["--vaards--"]
        if values ["Rinkevics"] == True:
            rez=rez+1
        dalas=[
            [sg.T("Vai koks ir atjaunojams dabas resurss?")],
            [sg.Radio("Jā",'Radio1',default=False,key="ja")],[sg.Radio("Nē",'Radio2',default=False,key="ne")],
            [sg.Button('Iziet'), sg.Button('Turpinām viktorīnu')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event == 'Turpinām viktorīnu':
        if values ["ja"] ==True:
            rez=rez+1
        dalas=[
            [sg.T("Ievadi 2+2 vērtību:"),sg.InputText(key="cetri")],
            [sg.Button('Iziet'), sg.Button('Turpinām?')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event == "Turpinām?":
        if values ["cetri"]=="4":
              rez=rez+1
        dalas=[
            [sg.T("Cik Viesturam ir gadi?")],
            [sg.Combo(['14','15','16','17'],key='sespadsmit' )],
            [sg.Button('Iziet'), sg.Button('Turpinām!')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event == "Turpinām!":
        if values ['sespadsmit']=='16':
              rez=rez+1
        dalas=[
            [sg.T("Vai Viesturs ir vīrietis vai sieviete")],
            [sg.Radio("Vīrietis",'Radio1',default=False,key="vir")],[sg.Radio("Sieviete",'Radio2',default=False,key="siev")],
            [sg.Button('Iziet'), sg.Button('Paturpināsim')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event == 'Paturpināsim':
        if values ["vir"]==True:
              rez=rez+1
        dalas=[
            [sg.T("Līdz kurai klasei ir vidusskola?")], 
            [sg.Combo(["9","12","15"], key="twelve")],
            [sg.Button('Iziet'), sg.Button('Uz priekšu!')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event == 'Uz priekšu!':
        if values ["twelve"]=="12":
              rez=rez+1
        dalas=[
            [sg.T("Cik ir 10 - 3 ?")], 
            [sg.InputText(key="seven")],
            [sg.Button('Iziet'), sg.Button('Vēlies turpināt?')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event == 'Vēlies turpināt?':
        if values ["seven"]=="7":
              rez=rez+1
        dalas=[
            [sg.T("Kas Viesturam garšo(iespējamas vairākas atbildes)(Grūts!!!)")],
            [sg.Checkbox("Salātlapas",default=False, key="salad")],[sg.Checkbox("Kivi",default=False, key="kivi")],[sg.Checkbox("Vīnogas",default=False, key="vinog")],[sg.Checkbox("Šokolāde",default=False, key="soko")],
            [sg.Button('Iziet'), sg.Button('Beidzam')],
            [sg.Text(f"Jūsu rezultāts ir {rez}")],
                ]
    elif event =='Beidzam':
        if values ["vinog"]and values["soko"] == True:
              rez=rez+2
        with open(datne, "a", encoding="utf8") as ff:
             ff.write(f"Dalībnieka vārds ir {vards}, un ir ieguvis rezultātu {rez}.\n")
        dalas=[
             [sg.T(f"Jūs esat pabeidzis viktorīnu un ieguvis {rez} punktus!")],
        ]
    logs.close()
    logs = sg.Window("Viktorīna",dalas)

logs.close()