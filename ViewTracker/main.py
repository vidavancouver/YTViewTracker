import viewsTimer
import grapher
import gui

MANUALCONTROL = False

"https://www.youtube.com/watch?v="

#secondsInWeek = 604800
#secondsInDay = 86400
#secondsInHour = 3600

guiData = gui.main()

if MANUALCONTROL:
    values = viewsTimer.manualTimes(guiData[0])
else:

    print(f"""[COLLECTING FROM] https://www.youtube.com/watch?v={guiData[0]}\n
    [TIME BETWEEN SCANS] {guiData[1]}\n
    [TOTAL NUM OF SCANS] {guiData[2]}""")
    values = viewsTimer.collectTimes(guiData[1], guiData[2], guiData[0])
    print("[STATUS] All data collected")

with open('values.txt', 'w+') as f:
    for i in values:
        f.write(f"{i}: {values[i]}\n")

grapher.main(values, guiData[0])