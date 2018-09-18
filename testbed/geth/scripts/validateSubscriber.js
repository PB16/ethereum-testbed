  function validateSubscriber(user, offerID) {
  var contractInterface = eth.contract([ { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": false, "inputs": [ { "name": "name", "type": "string" }, { "name": "category", "type": "string" }, { "name": "model", "type": "string" }, { "name": "price", "type": "uint256" }, { "name": "endpoint", "type": "string" }, { "name": "inputs", "type": "string" }, { "name": "outputs", "type": "string" }, { "name": "year", "type": "uint16" }, { "name": "month", "type": "uint8" }, { "name": "day", "type": "uint8" }, { "name": "hour", "type": "uint8" } ], "name": "addOffer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getMyOffers", "outputs": [ { "name": "", "type": "uint256[]", "value": [ "0", "0", "0", "0", "1", "2", "3" ] } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "ID", "type": "uint256" } ], "name": "deleteOffer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getAllOffers", "outputs": [ { "components": [ { "name": "ID", "type": "uint256" }, { "name": "provider", "type": "address" }, { "name": "name", "type": "string" }, { "name": "category", "type": "string" }, { "name": "price", "type": "uint256" }, { "name": "endTime", "type": "uint256" }, { "name": "endpoint", "type": "string" }, { "name": "inputs", "type": "bytes32[]" }, { "name": "outputs", "type": "bytes32[]" } ], "name": "", "type": "tuple[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "ID", "type": "uint256" } ], "name": "getOffer", "outputs": [ { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" }, { "name": "", "type": "string", "value": "" }, { "name": "", "type": "string", "value": "" }, { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "string", "value": "" }, { "name": "", "type": "bytes32[]", "value": [] }, { "name": "", "type": "bytes32[]", "value": [] } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getOfferLength", "outputs": [ { "name": "", "type": "uint256", "value": "4" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "destroy", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" } ]);

  var contractResult = contractInterface.at("0x7d0363f14fCE1123E720435C451234B379dEff97");
  var positiveResult = contractResult.getUsers(user, offerID);

  /*var positiveResults = false;
  for(var i=0; i < users.length; i++) {
    if(user == users[i]) {
      positiveResults = true
    }
  }
  return positiveResults;*/
}
