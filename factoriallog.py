import logging


logging.basicConfig(filename = 'myProgrammingLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total


def factorialNoError(n):
    total = 1
    if n == 0:
        return 1
    else:
        for i in range(n + 1):
            total *= i
    return total

print(factorial(0))
print(factorialNoError(0))

logging.debug('End of program')
