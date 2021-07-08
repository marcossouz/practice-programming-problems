var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

for(var i in [...Array(3).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`inputData/1005/${i}.in`)
  });

  var lines = [];
  myInterface.on('line', function (line) {
    lines.push(line);
  });
  
  var ii = 0
  myInterface.on('close', function() {
      // URI JUDGE INICIO

      let a = parseFloat(lines.shift());
      let b = parseFloat(lines.shift());
      let media = ((a * 3.5) + (b * 7.5)) / 11
      let result = `MEDIA = ${media.toFixed(5)}`;
      
      console.log(result);
      // URI JUDGE FIM
      ii++
  });

  myInterface.on('error', function(err) {
      console.log(err)
  });
}