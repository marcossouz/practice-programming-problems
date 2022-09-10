var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

for(var i in [...Array(4).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`inputData/1009/${i}.in`)
  });

  var lines = [];
  myInterface.on('line', function (line) {
    lines.push(line);
  });
  
  var ii = 0
  myInterface.on('close', function() {
      // URI JUDGE INICIO

      let name = lines.shift();
      let fixed_salary = parseFloat(lines.shift());
      let vendas = parseFloat(lines.shift());
      
      let salary = fixed_salary + (vendas * 0.15);
      let result = `TOTAL = R$ ${salary.toFixed(2)}`;
      
      console.log(result);
      // URI JUDGE FIM
      ii++
  });

  myInterface.on('error', function(err) {
      console.log(err)
  });
}