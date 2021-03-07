import nistrng
import math
from fractions import Fraction
from gamma_functions import *

bit_file = open("petra.txt", "r")

testlist = [
    'monobit_test',
    'frequency_within_block_test',
    'runs_test',
    'longest_run_ones_in_a_block_test',
    # 'binary_matrix_rank_test',
    'dft_test',
    'non_overlapping_template_matching_test',
    # 'overlapping_template_matching_test',
    # 'maurers_universal_test',
    # 'linear_complexity_test',
    'serial_test',
    'approximate_entropy_test',
    'cumulative_sums_test'
    # 'random_excursion_test',
    # 'random_excursion_variant_test'
    ]


def count_ones_zeroes(bitstream):
    ones = 0
    zeroes = 0
    for bit in bitstream:
        if bit:
            ones += 1
        else:
            zeroes += 1
    return zeroes, ones


bits = []
success_count, fail_count = 0, 0
for line in bit_file:
    bits.append(int(line.split(" ")[1][0]))

for test in testlist:
    m = __import__("sp800_22_" + test)
    func = getattr(m, test)
    print("TEST: %s" % test)
    success, p, plist = func(bits)
    if success:
        print("PASS")
        success_count += 1
    else:
        print("FAIL")
        fail_count += 1

print(f"{success_count} successes, {fail_count} failures")
