import PySimpleGUI as sg
import Generator


sg.theme('SandyBeach')

gender = ["Male", "Female", "Other"]
theme = ["Fantasy", "Space", "Beach", "Random"]
layout = [[sg.Text("Enter Recipient's Info:")],
          [sg.Text("Name:")], [sg.InputText()],
          [sg.Text("Age:")], [sg.InputText()],
          [sg.Text("Gender:")], [sg.InputOptionMenu(gender)],
          [sg.Text("Theme")], [sg.InputText()],
          [sg.Submit(button_text="Generate")], [sg.Cancel()]]

window = sg.Window("Bedtime Builder", layout)


# text_input = values[0]
# sg.popup('You entered', text_input)

while True:
    event, values = window.read()
    if (event == sg.WINDOW_CLOSED) \
            or ((event == 'Cancel') and sg.popup_yes_no('Are you sure you want to exit?') == 'Yes'):
        break
    if event == 'Generate':
        name = values[0]
        age = values[1]
        gender = values[2]
        theme = values[3]
        newStory = Generator.getStory(name, age, gender, theme)
        sg.popup(newStory)





window.close()
