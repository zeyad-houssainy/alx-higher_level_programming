#!/usr/bin/node
// Fix: Convert CommonJS module to ES module
exports.esrever = function (list) {
    let newList = [];
    for (let i of list) {
        newList.unshift(i);
    }
    return newList;
}
