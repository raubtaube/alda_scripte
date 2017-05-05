import os
from os.path import join
from contextlib import redirect_stdout
import io
import sys


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def main():
    path = '/home/mgutsche/HiWi/AlDa2017/Korrekturen/Zettel01' # den pfad hier anpassen
    correct_primes = set(get_primes(1000))

    for root, dirs, files in os.walk(path):
        for fname in files:
            if fname == "sieve.py":
                syntax_err = False
                py_str = open(join(root, fname), 'rU').read()
                print(10*"-")
                print("Testing ", root)
                #print(repr(py_str))
                py_str = py_str.replace('print', '#print') # to comment out print statements

                try:
                    exec(py_str , globals())
                    test_primes = set(sieve(1000))

                except SyntaxError:
                    print("Syntax Error")
                    continue


                print("Correct? : {}".format( test_primes == correct_primes ))
                if not set(test_primes) == set(correct_primes):
                    print("Missing Primes:", correct_primes - test_primes )
                    print("Not Primes:", test_primes - correct_primes)



if __name__ == "__main__":
    main()
