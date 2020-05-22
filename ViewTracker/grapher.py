import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import getViews



def main(dick, KEY):

    values = assemble(dick)

    plt.plot(values[0],values[1])
    plt.xlabel("Times")
    plt.ylabel("views (millions)")
    title = getViews.findVidTitle(getViews.makeRequest(KEY))
    plt.title(title)
    plt.show()


def assemble(dick):
    assert type(dick) == dict
    times = []
    views = []
    for i in dick:
        dick[i] = dick[i]/1000000
        times.append(i)
        views.append(dick[i])
    lis = [times, views]
    print(lis)
    return(lis)

