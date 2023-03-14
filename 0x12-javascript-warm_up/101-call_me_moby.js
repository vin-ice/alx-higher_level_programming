#!/usr/bin/node
const callMeMoby = function (x, theFunction) { while (x >= 1) { theFunction(); x--; } };
module.exports = { callMeMoby };
