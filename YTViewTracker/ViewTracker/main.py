import viewsTimer
import getViews
import grapher
import gui
import emailer

MANUALCONTROL = False

"https://www.youtube.com/watch?v="

#secondsInWeek = 604800
#secondsInDay = 86400
#secondsInHour = 3600
title = ""
guiData = gui.main()
print("[STATUS] got data from GUI")

if MANUALCONTROL:
    print("[MODE] manual control")
    values = viewsTimer.manualTimes(guiData[0])
else:
    print("[MODE] Automated Control")
    print(f"""[COLLECTING FROM] https://www.youtube.com/watch?v={guiData[0]}
    [TIME BETWEEN SCANS] {guiData[1]}
    [TOTAL NUM OF SCANS] {guiData[2]}""")
    values = viewsTimer.collectTimes(guiData[1], guiData[2], guiData[0])
    print("[STATUS] All data collected")

title = getViews.findVidTitle(getViews.makeRequest(guiData[0]))

if guiData[3] == True:
    emailer.main(guiData[4], title)

with open('values.txt', 'w+') as f:
    for i in values:
        f.write(f"{i}: {values[i]}\n")

grapher.main(values, guiData[0])