#!/usr/bin/env python3


import jk_utils.rng


LENGTH = 16
COUNT = 10


RESERVOIR1 = "abcdefghijklmnopoqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ"
RESERVOIR2 = RESERVOIR1 + "1234567890"
EXTRA = "

RNG = jk_utils.rng.URandomGenerator()



def generatePwd(length:int):
    assert isinstance(length, int)
    assert length > 1

    s = RNG.nextCharacter(RESERVOIR1)
    lastC = s[0]
    while len(s) < LENGTH:
        nextC = RNG.nextCharacter(RESERVOIR2)
        if nextC != lastC:
            s += nextC
            lastC = nextC
    return s



print()
for i in range(0, COUNT):
    print("\t" + generatePwd(LENGTH))
print()


