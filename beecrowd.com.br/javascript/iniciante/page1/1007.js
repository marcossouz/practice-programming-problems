var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

for(var i in [...Array(3).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`inputData/1007/${i}.in`)
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
      let c = parseInt(lines.shift());
      let d = parseInt(lines.shift());
      let media = ((a * b) - (c * d));
      let result = `DIFERENCA = ${media}`;
      
      console.log(result);
      // URI JUDGE FIM
      ii++
  });

  myInterface.on('error', function(err) {
      console.log(err)
  });
}