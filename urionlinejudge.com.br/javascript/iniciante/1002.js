var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

var expected = ['A=12.5664', 'A=31819.3103', 'A=70685.7750']

for(var i in [...Array(3).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`../inputData/1002/${i}.in`)
  });

  var lines = [];
  myInterface.on('line', function (line) {
    lines.push(line);
  });
  
  var ii = 0
  myInterface.on('close', function() {
      // URI JUDGE INICIO

      const PI = 3.14159;
      let number = parseFloat(lines.shift());
      let area = PI * Math.pow(number, 2)
      let result = `A=${area.toFixed(4)}`;
      
      console.log(result);

      // URI JUDGE FIM
      if(expected[ii] !== result) {
        console.error(`FAIL expected: ${expected[ii]}`, `result: ${result}`)
        exit(1);
      }
      ii++
  });

  myInterface.on('error', function(err) {
      console.log(err)
  });
}