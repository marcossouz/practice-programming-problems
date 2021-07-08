var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

for(var i in [...Array(3).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`inputData/1008/${i}.in`)
  });

  var lines = [];
  myInterface.on('line', function (line) {
    lines.push(line);
  });
  
  var ii = 0
  myInterface.on('close', function() {
      // URI JUDGE INICIO

      let a = parseInt(lines.shift());
      let b = parseInt(lines.shift());
      let c = parseFloat(lines.shift());
      let salary = b * c
      let result = `NUMBER = ${a}\nSALARY = U$ ${salary.toFixed(2)}`;
      
      console.log(result);
      // URI JUDGE FIM
      ii++
  });

  myInterface.on('error', function(err) {
      console.log(err)
  });
}