var jsonInput = require("./output.json");
// for (var i = 0; i < ; i++) {
//     var obj = jsonInput[i];
//     for (var key in obj) {
//         console.log(key);
//     }
//     console.log(i);
// }

function isNumeric(num){
    return !isNaN(num)
}

var stringOutput = "var addressPoints = [";

for (var i = 0; i < jsonInput.products_found.length; i++) {
    if (isNumeric(jsonInput.products_found[i].latitude) && isNumeric(jsonInput.products_found[i].longitude) &&
    jsonInput.products_found[i].latitude != "0.0" && jsonInput.products_found[i].longitude != "0.0") {
        stringOutput += "[" + jsonInput.products_found[i].latitude + ", " +
            jsonInput.products_found[i].longitude + "],\n";
    }
}

if (stringOutput.charAt(stringOutput.length - 2) == ",") {
    stringOutput = stringOutput.substr(0, stringOutput.length - 2);
}
// if (stringOutput == ",") {
//     console.log("fds");
// }

stringOutput += "];";

console.log(stringOutput);