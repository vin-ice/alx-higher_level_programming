#!/usr/node/bin

exports.nbOccurences = function (list, searchElement) {
  return list.filter((item)=> item === searchElement).length;
};
