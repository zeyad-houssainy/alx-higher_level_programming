#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w, h){
        if (w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }
}

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);
