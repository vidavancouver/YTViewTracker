from datetime import datetime
import time

import getViews

secondsInWeek = 604800
secondsInDay = 86400
secondsInHour = 3600

 
def collectTimes(interval, iterations, KEY):
    dick = {}
    for i in range(iterations):
        print(f"{i} iteration")
        time.sleep(interval)
        print(f"{datetime.now()}: collecting views")
        currentViews = getViews.main(KEY)
        dick[str(datetime.now())] = currentViews
        print(dick)
    return dick


def manualTimes(KEY):
    dick = {}
    print("[MANUAL CONTROL] Press 'Enter' to capture current YouTube data.\n Type 'END' to finish the collection and plot graph")
    while True:
        inp = input(">>> ")
        if inp != "END":
            print(f"{datetime.now().time()}: collecting views")
            currentViews = getViews.main(KEY)
            dick[str(datetime.now())] = currentViews
        else:
            return(dick)