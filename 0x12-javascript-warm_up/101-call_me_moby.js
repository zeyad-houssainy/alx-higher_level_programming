#!/usr/bin/node
exports.callMeMoby = function (x, theFunction){
    for (let i = 0; i < x; i++){
        theFunction()
    }
}


const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(5, function () {
  console.log('C is fun');
});