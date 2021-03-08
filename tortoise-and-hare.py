#!/usr/bin/python3

'''
Created by Hosein Hadipour
Date: March 8, 2021
 ____________________________
< Cow can say cat is cute :) >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

import hashlib
import random
import string
import time

letter = string.ascii_uppercase + string.ascii_lowercase + string.digits

prefix = "Cow can say cat is cute :)"
collision_length = 40

def truncated_sha3_512(message):
    input_message = prefix + str(message)
    output = hashlib.sha3_512(input_message.encode())
    output = output.hexdigest()[:collision_length//4]
    return output
    
def cycle_detection(x0, f):
    """
    Tortoise and Hare algorithm to find a cycle in the following sequence:
    [x0, x1 = f(0), x2 = f(x1), x3 = f(x2), ..., xi = f(xi-1), ...]
    """
    tortoise = f(x0)
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        data1 = tortoise
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    lam = 1
    hare = f(tortoise)
    while hare != tortoise:
        data2 = hare
        hare = f(hare)
        lam += 1

    return mu, lam, data1, data2

def main():
    initial_message = ''.join([random.choice(letter) for _ in range(10)])
    start_time = time.time()
    mu, lam, data1, data2 = cycle_detection(initial_message, truncated_sha3_512)
    elapsed_time = time.time() - start_time
    print("starting point = %d\ncyclelength = %d" % (mu, lam))
    print("message 1: %s" % prefix + data1)
    print("message 2: %s" % prefix + data2)
    X1 = prefix + data1
    X2 = prefix + data2
    print("SHA3-512(message 1) = %s" % hashlib.sha3_512(X1.encode()).hexdigest())
    print("SHA3-512(message 2) = %s" % hashlib.sha3_512(X2.encode()).hexdigest())
    print("Elapsed time: %0.4f seconds" % elapsed_time)

if __name__ == '__main__':
    main()

