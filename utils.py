import requests
import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import time


def pressure(orderbook, gamma=2):
    data = orderbook
    ret = {}
    for label in ['ask', 'bid']:
        d0 = data[0]['orderbook_units'][0][f'{label}_price']
        delta = np.abs(data[0]['orderbook_units'][0]
                       [f'{label}_price'] - data[0]['orderbook_units'][1][f'{label}_price'])
        p = 0
        for d in data[0]['orderbook_units']:
            # print("{:.8f}".format(np.exp(-((np.abs(d[f'{label}_price']-d0))/delta)/gamma)), "{:.8f}".format(d[f'{label}_size']), end=" ")
            # print("{:.8f}".format(d[f'{label}_size']*np.exp(-(np.abs(d[f'{label}_price']-d0)/delta)/2)))
            p += d[f'{label}_size'] * \
                np.exp(-(np.abs(d[f'{label}_price']-d0)/delta)/2)
        ret[label] = p
    return ret
