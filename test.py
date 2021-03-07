import nistrng
import math
from fractions import Fraction
from

bit_file = open("petra.txt", "r")


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


def frequency_within_block_test(bits):
    # Compute number of blocks M = block size. N=num of blocks
    # N = floor(n/M)
    # miniumum block size 20 bits, most blocks 100
    n = len(bits)
    M = 20
    N = int(math.floor(n / M))
    if N > 99:
        N = 99
        M = int(math.floor(n / N))

    if len(bits) < 100:
        print("Too little data for test. Supply at least 100 bits")
        return False, 1.0, None

    print("  n = %d" % len(bits))
    print("  N = %d" % N)
    print("  M = %d" % M)

    num_of_blocks = N
    block_size = M  # int(math.floor(len(bits)/num_of_blocks))
    # n = int(block_size * num_of_blocks)

    proportions = list()
    for i in range(num_of_blocks):
        block = bits[i * block_size:((i + 1) * block_size)]
        zeroes, ones = count_ones_zeroes(block)
        proportions.append(Fraction(ones, block_size))

    chisq = 0.0
    for prop in proportions:
        chisq += 4.0 * block_size * ((prop - Fraction(1, 2)) ** 2)

    p = gammaincc((num_of_blocks / 2.0), float(chisq) / 2.0)
    success = (p >= 0.01)
    return success, p


bits = []

for line in bit_file:
    bits.append(int(line.split(" ")[1][0]))

print(monobit_test(bits))
print(frequency_within_block_test(bits))
