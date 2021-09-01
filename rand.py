'''
Date: 2021.08.31 16:17:51
Description: Omit
LastEditors: Rustle Karl
LastEditTime: 2021.09.01 13:24:32
'''
from random import randint


def generate_lottery() -> tuple:
    red = set()

    while len(red) < 6:
        red.add(randint(1, 33))

    lottery = sorted(red)
    lottery.append(randint(1, 16))

    # 列表不可哈希
    return tuple(lottery)


def find_least_lottery() -> tuple:
    lotteries = set()

    while len(lotteries) < 1 << 12:
        lotteries.add(generate_lottery())

    while True:
        lottery = generate_lottery()
        if lottery not in lotteries:
            return lottery


if __name__ == '__main__':
    for _ in range(100):
        print(find_least_lottery())
