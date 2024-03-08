const fs = require('fs');
fs.readFile('test.txt', 'utf-8', (err, data) => {
  if (err) {
    console.error('Error ready the file');
    return;
  }
  console.log(data);
});
