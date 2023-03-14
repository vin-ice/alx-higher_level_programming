#!/usr/bin/node
exports.esrever = function (list) {
  let tmp; const half = list.length / 2;
  for (let i = 0; i < half; i++) {
    tmp = list[i];
    list[i] = list[(half * 2 - 1) - i];
    list[(half * 2 - 1) - i] = tmp;
  }
  return list;
};
