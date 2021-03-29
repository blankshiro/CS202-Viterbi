#!/usr/bin/env python3

import os
import sys
import subprocess
import random
from time import sleep

CONVOLUTIONAL_CODE_PARAMS = '7 121 121 121 121'
DELAY = 0.5

RED_START = '\033[1;31m'
GREEN_START = '\033[1;32m'
END = '\033[0m'


def to_ascii(binary):
    n = int(binary.replace(' ', ''), 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'ignore')


def to_binary(ascii):
    return (bin(int.from_bytes(ascii.encode(), 'big')))[2:]


def convolutional_encode(bits):
    p = subprocess.run('viterbi/viterbi_main ' + CONVOLUTIONAL_CODE_PARAMS + ' --encode ' + bits, shell=True, capture_output=True)
    return p.stdout.strip().decode()


def viterbi_decode(bits):
    p = subprocess.run('viterbi/viterbi_main ' + CONVOLUTIONAL_CODE_PARAMS + ' ' + bits, shell=True, capture_output=True)
    return p.stdout.strip().decode()


def color_corrupted_bits(bits, corrupted_indices):
    result = ''
    for index, bit in enumerate(bits):
        if index in corrupted_indices:
            result += RED_START + bit + END
        else:
            result += bit
    return result


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} [msg]')
        exit(1)

    msg = sys.argv[1]
    msg_binary = to_binary(msg)
    original_codes = convolutional_encode(msg_binary)
    corrupted_codes = original_codes
    corrupted_bits = []

    try:
        while True:
            os.system('clear')
            print(GREEN_START + msg + END)
            print('  |')
            print('  |  to binary')
            print('  v')
            print(msg_binary)
            print('  |')
            print('  |  sender: convolutional encode')
            print('  v')
            print(original_codes)
            print('  /')
            print('  \  transmit')
            print(f'  /  ({len(corrupted_bits) / len(original_codes) * 100:.2f}% bits corrupted)')
            print('  v')
            corrupted_codes = list(corrupted_codes)
            corrupted_bit = random.randint(0, len(corrupted_codes) - 1)
            if corrupted_bit not in corrupted_bits:
                corrupted_bits.append(corrupted_bit)
                corrupted_codes[corrupted_bit] = str(int(corrupted_codes[corrupted_bit]) ^ 1) # corrupt the bit
            corrupted_codes = ''.join(corrupted_codes)
            colored_codes = color_corrupted_bits(corrupted_codes, corrupted_bits)
            print(colored_codes)
            print('  |')
            print('  |  receiver: viterbi decode')
            print('  v')
            decoded = viterbi_decode(corrupted_codes)
            print(decoded)
            print('  |')
            print('  |  to ascii')
            print('  v')
            output = to_ascii(decoded)
            if output == msg:
                print(GREEN_START + output + END)
            else:
                print(RED_START + output + END)
            print()
            sleep(DELAY)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()