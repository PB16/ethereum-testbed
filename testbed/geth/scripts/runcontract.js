function accessContract() {
  var contractInterface = eth.contract([[ { "constant": false, "inputs": [], "name": "kill", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "greet", "outputs": [ { "name": "", "type": "string", "value": "Tester" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_greeting", "type": "string", "index": 0, "typeShort": "string", "bits": "", "displayName": "&thinsp;<span class=\"punctuation\">_</span>&thinsp;greeting", "template": "elements_input_string", "value": "Tester" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ] ]);
  var contractAddr = contractInterface.at("0xEFd6705E9078252BbabC913ec51378209bf85c4C")
  console.log(contractAddr.greet());
  //console.log("contractAddr.greet = ", contractAddr.greet());
