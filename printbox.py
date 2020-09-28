'''

*************
*           *
*           *
*           *
*           *
*           *
*           *
*************



'''

def printBox(symbol, height , width):
    if len(symbol) != 1:
        raise Exception('Length of "symbol" must be one')
    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)



printBox('&', 12, 8)
printBox('**', 10, 12)
