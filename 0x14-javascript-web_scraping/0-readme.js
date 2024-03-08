#!/usr/bin/node
#!/usr/bin/node
const fs = require("fs");
fs.readFile(process.argv[2], "utf-8", (err, data) => {
  if (err) {
    console.error("Error ready the file");
    return;
  }
  console.log(data);
});
