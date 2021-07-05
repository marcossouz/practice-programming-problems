var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

var expected = ['X = 19', 'X = -6', 'X = 8']

for(var i in [...Array(3).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`../inputData/1001/${i}.in`)
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
      let result = `X = ${ a + b }`;
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