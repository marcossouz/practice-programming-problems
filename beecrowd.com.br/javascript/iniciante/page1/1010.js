var readline = require('readline');
var fs = require('fs');
const { exit } = require('process');

for(var i in [...Array(3).keys()]) {
  var myInterface = readline.createInterface({
    input: fs.createReadStream(`inputData/1010/${i}.in`)
  });

  var lines = [];
  myInterface.on('line', function (line) {
    lines.push(line);
  });
  
  var ii = 0
  myInterface.on('close', function() {
      // URI JUDGE INICIO

      array1 = lines.shift().split(' ')
      array2 = lines.shift().split(' ')

      let numero = parseInt(array1[0])
      let numero2 = parseInt(array2[0])

      let qt = parseInt(array1[1])
      let qt2 = parseInt(array2[1])

      let valor = parseFloat(array1[2])
      let valor2 = parseFloat(array2[2])

      let result = `VALOR A PAGAR: R$ ${((qt * valor) + (qt2 * valor2)).toFixed(2)}`;
      
      console.log(result);
      // URI JUDGE FIM
      ii++
  });

  myInterface.on('error', function(err) {
      console.log(err)
  });
}