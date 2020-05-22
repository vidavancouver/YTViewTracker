import PySimpleGUI as sg 
import sys

def main():
    layout = [
        [sg.Text("Enter a youtube video ID"), sg.InputText()],
        [sg.Text("Hours between scans?"), sg.InputText()],
        [sg.Text("How many total scans?"),sg.InputText()],
        [sg.Radio("Send me an E-Mail when finished. [BETA]", "RADIO1", default=False)],
        [sg.Text("E-mail (optional)"), sg.InputText()],
        [sg.OK(), sg.Cancel(), sg.Help()]
    ]
    window = sg.Window("ViewTracker", layout)
    event, values = window.read()
    window.close()

    if event == "Help":
        sg.popup("""box 1. A youtube ID should be an 11 character long string at the end of a youtube video URL
        box 2. Accepts both integers and decimal numbers, as long as it equates to being a whole minute.
        box 3. Accepts integer. The number of times total the views will be collected.
        Raw Data from the most recent completed scan can be found in the file "Values.txt" """)
    elif event == "Cancel":
        print("[STATUS] Aborting")
        sys.exit()
    elif event == "OK":
        print("[STATUS] Proceeding")
        try:
            values[1] = int(float(values[1]) * 3600)
            values[2] = int(values[2])
            print("[DEBUG] Formatted Dictionary entries")
        except Exception as e:
            print("please only enter numbers for the last two input fields")
            print(e)
        print(f"collected: {values}")
        return(values)

if __name__ == "__main__":
    main()