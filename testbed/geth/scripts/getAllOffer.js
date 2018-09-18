function getAllOffers() {
  var contractInterface = eth.contract([ { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": false, "inputs": [ { "name": "name", "type": "string" }, { "name": "category", "type": "string" }, { "name": "model", "type": "string" }, { "name": "price", "type": "uint256" }, { "name": "endpoint", "type": "string" }, { "name": "inputs", "type": "string" }, { "name": "outputs", "type": "string" }, { "name": "year", "type": "uint16" }, { "name": "month", "type": "uint8" }, { "name": "day", "type": "uint8" }, { "name": "hour", "type": "uint8" } ], "name": "addOffer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getMyOffers", "outputs": [ { "name": "offerings", "type": "uint256[]", "value": [] } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "ID", "type": "uint256" } ], "name": "deleteOffer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "_ID", "type": "uint256" } ], "name": "getOffer", "outputs": [ { "name": "ID", "type": "uint256", "value": "92" }, { "name": "provider", "type": "address", "value": "0xeb226676b8046f87c25c04dcba27bfde3c514730" }, { "name": "name", "type": "string", "value": "testOffering57" }, { "name": "category", "type": "string", "value": "BusCategory" }, { "name": "price", "type": "uint256", "value": "0" }, { "name": "endpoint", "type": "string", "value": "100.101.102.103" }, { "name": "inputs", "type": "bytes32[]", "value": [ "0x696e707574310000000000000000000000000000000000000000000000000000", "0x696e707574320000000000000000000000000000000000000000000000000000", "0x696e707574330000000000000000000000000000000000000000000000000000" ] }, { "name": "outputs", "type": "bytes32[]", "value": [ "0x6f75747075743100000000000000000000000000000000000000000000000000", "0x6f75747075743200000000000000000000000000000000000000000000000000", "0x6f75747075743300000000000000000000000000000000000000000000000000" ] } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getOfferLength", "outputs": [ { "name": "length", "type": "uint256", "value": "11235" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "destroy", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" } ]);

  var contractResult = contractInterface.at("0x39c267ca27c3C3adbBB62d42B06B2Bd1e93572AD");
  var iterator = contractResult.getOfferLength();

  var Offers = new Array();
  Offers.push(new Array(6)); // Empty fill

  for(var i = 1; i < iterator; i++) {
    if((i % 100) == 0) {
      console.log("Progress: " + (i / iterator)*100 + "%");
    }
    var Offer = new Array(10);
    for(var j = 0; j < 10; j++) {
      Offer[j] = contractResult.getOffer(i)[j];
    }
    Offers.push(Offer);
  }
  return Offers;
}

function offeringQuery(category, inputs, outputs) {
  // Sanity Check
  var t0 = Date.now();
  if(category == null || category == "") {
    return "Category needs to be set!";
  }

  if(inputs == null || outputs == null) {
    return "Input and Output needs at least an Empty array!";
  }

  var candidates = new Array();
    var array = getAllOffers();

  // Find offering based on Category
  for(var i=1; i<array.length; i++) {
    if(array[i][3] == category) {
      candidates.push(i)
    }
  }

  if(candidates.length == 0) {
    return "No Offers match the category!";
  }
  else {
    if(inputs.length == 0 && outputs.length == 0) {
      var t1 = Date.now();
      console.log("Search took " + (t1 - t0) + " milliseconds.")
      return candidates;
    }

    // Check if inputs alter the candidates
    if(inputs.length != 0) {
      var isAllZero = candidates.length; // Check if inputs return zero results
      //var currLength = candidates.length;
      for(var i = 0; i < candidates.length; i++) {
        var index = candidates[i];
        for(var j=0; j < inputs.length; j++) {
          var input = inputs[j];
          if(!arrayContainsUTF(input, array[index][6])) {
            candidates[i] = -1;
            isAllZero--;
          }
        }
      }
    }
    // Check if outputs alter the candidates
    if(outputs.length != 0 && isAllZero > 0) {
      //var currLength = candidates.length;
      for(var i = 0; i < candidates.length; i++) {
        var index = candidates[i];
        for(var j=0; j < outputs.length; j++) {
          var output = outputs[j];

          if(!arrayContainsUTF(output, array[index][7])) {
            candidates[i] = -1;
          }
        }
      }
    }

    // Clean - Remove all negative results from candidates
    var results = new Array();
    for(var i = 0; i < candidates.length; i++) {
      if(candidates[i] != -1) {
        results.push(candidates[i]);
      }
    }
    if(results.length == 0) {
      return "No Offers match the category!";
    }

    var t1 = Date.now();
    console.log("Search took " + (t1 - t0) + " milliseconds.")
    return results;
  }
}

// Using web3 function toUtf8: byte32 -> utf8 string
function arrayContainsUTF(needle, arrhaystack)
{
    var tempArr = new Array();
    for(var i = 0; i < arrhaystack.length; i++) {
      tempArr.push(web3.toUtf8(arrhaystack[i]));
    }

    return (tempArr.indexOf(needle) > -1);
}
