# faça a instalação do pytube e do PySimpleGui no cmd:
# pip install pytube
import pytube as yt
# pip install pysimplegui
import PySimpleGUI as sg

sg.theme('Dark Grey 13')

layout = [[sg.Text('Link do video no YouTube')],
          [sg.Input(key='link')],
          [sg.Radio('720p', 1, default=True), sg.Radio(
              '360p', 1), sg.Radio('144p', 1)],
          [sg.Button('Baixar')], ]


window = sg.Window('Get filename example', layout)


while True:
    event, values = window.read()
    valoritag = 0
    if event == sg.WIN_CLOSED:

        break

    if event == 'Baixar':

        if values[0] == True:
            valoritag = 22
        elif values[1] == True:
            valoritag = 18
        else:
            valoritag = 17

        if values['link'] == '':
            link = yt.YouTube('https://youtu.be/V1l6kxQNq54')
            videoSelecionado = link.streams.get_by_itag(valoritag)
            videoSelecionado.download(output_path="./videosBaixados")

        else:
            link = yt.YouTube(values['link'])
            videoSelecionado = link.streams.get_by_itag(valoritag)
            videoSelecionado.download(output_path="./videosBaixados")
