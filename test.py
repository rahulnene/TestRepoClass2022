import nistrng

bit_file = open("petra.txt", "r")

import math


def count_ones_zeroes(bitstream):
    ones = 0
    zeroes = 0
    for bit in bitstream:
        if bit:
            ones += 1
        else:
            zeroes += 1
    return zeroes, ones


def monobit_test(bits):
    n = len(bits)

    zeroes, ones = count_ones_zeroes(bits)
    s = abs(ones - zeroes)
    print("  Ones count   = %d" % ones)
    print("  Zeroes count = %d" % zeroes)

    p = math.erfc(float(s) / (math.sqrt(float(n)) * math.sqrt(2.0)))

    success = (p >= 0.01)
    return success, p


bits = []

for line in bit_file:
    bits.append(int(line.split(" ")[1][0]))

print(monobit_test(bits))