/*
 * @Date: 2021.09.01 8:50
 * @Description: Omit
 * @LastEditors: Rustle Karl
 * @LastEditTime: 2021.09.01 8:50
 */
import 'dart:math';

List<int> generateLottery() {
  Random rand = Random();
  Set<int> red = {};
  while (red.length < 6) {
    red.add(rand.nextInt(32) + 1);
  }
  List<int> lottory = red.toList();
  lottory.sort();
  lottory.add(rand.nextInt(15) + 1);
  return lottory;
}

List<int> findLeastLottery() {
  Set<List<int>> lotteries = {};
  while (lotteries.length < 1 << 12) {
    lotteries.add(generateLottery()); // Dart
  }
  while (true) {
    List<int> lottery = generateLottery();
    if (!lotteries.contains(lottery)) {
      return lottery;
    }
  }
}
