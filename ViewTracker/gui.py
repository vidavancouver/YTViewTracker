import PySimpleGUI as sg 
import sys

def main():
    layout = [
        [sg.Text("Enter a youtube video ID")],
        [sg.InputText()],
        [sg.Text("How many hours between scans?")],
        [sg.InputText()],
        [sg.Text("How many total scans?")],
        [sg.InputText()],
        [sg.Help()],
        [sg.OK(), sg.Cancel()]
    ]
    window = sg.Window("ViewTracker", layout)
    event, values = window.read()
    window.close()

    if event == "Help":
        sg.popup("""1. A youtube ID should be an 11 character long string at the end of a youtube video URL\n
        2. Accepts both integers and decimal numbers, as long as it equates to being a whole minute.\n
        3. Accepts integer. The number of times total the views will be collected.""")
    elif event == "Cancel":
        sys.exit()
    else:
        try:
            values[1] = int(float(values[1]) * 3600)
            print(values[1])
            values[2] = int(values[2])
        except Exception as e:
            print("please only enter numbers for the last two input fields")
            print(e)
            main()
        print(f"collected: {values}")
        return(values)
main()