import PySimpleGUI as sg
import requests,datetime
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Kraj'),sg.InputText()],
            [sg.Text('Miasto'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ,
            [sg.Text("", key='-KRAJ-')],
            [sg.Text("", key='-MIASTO-')],
            [sg.Text("", key='-TEMP-')],
            [sg.Text("", key='-ODCZUCIE-')],
            [sg.Text("", key='-WIL-')],
            [sg.Text("", key='-MIN-')],
            [sg.Text("", key='-MAX-')],
            [sg.Text("", key='-WIND-')],
            [sg.Text("", key='-KIER-')],
            [sg.Text("", key='-WSCH-')],
            [sg.Text("", key='-ZACH-')]]
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    k1=values[0]
    k2=values[1]
    kraj=  k1
    miasto = k2
    url="https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    querystring = {"city":miasto,"country":kraj}
    headers = {
	"X-RapidAPI-Key": "", #klucz api
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
	}
    response = requests.request("GET", url, headers=headers, params=querystring)
    temperatura=response.json()["temp"] #temperatura akt
    odczucie=response.json()["feels_like"] #odczuwalna temperatura
    wilgotność=response.json()["humidity"] #wilgotność
    min_temp=response.json()["min_temp"] #minimalna temperatura
    max_temp=response.json()["max_temp"] #maksymalna temperatura
    wiatr=response.json()["wind_speed"] #m/s
    kierunek_wiatru=response.json()["wind_degrees"] #stopnie
    wschód=response.json()["sunrise"]
    zachód=response.json()["sunset"]
    wschód_a = datetime.datetime.fromtimestamp(wschód)
    zachód_a=datetime.datetime.fromtimestamp(zachód)
    w=wschód_a.strftime("%d-%m-%Y %H:%M:%S")
    z=zachód_a.strftime("%d-%m-%Y %H:%M:%S")
    window['-KRAJ-'].update("Kraj "+k1)
    window['-MIASTO-'].update("Miasto "+k2)
    window['-TEMP-'].update("Temperatura "+str(temperatura)+" C")
    window['-ODCZUCIE-'].update("Odczucie "+str(odczucie))
    window['-WIL-'].update("Wilgotność "+str(wilgotność)+" %")
    window['-MIN-'].update("Minimalna temperatura "+str(min_temp)+" C")
    window['-MAX-'].update("Maksymalna temperatura "+str(max_temp)+" C")
    window['-WIND-'].update("Prędkość wiatru "+str(max_temp)+" m/s")
    window['-KIER-'].update('Kierunek wiatru '+str(kierunek_wiatru))
    window['-WSCH-'].update('Wschód słońca '+w)
    window['-ZACH-'].update('Zachód słońca '+z)







window.close()