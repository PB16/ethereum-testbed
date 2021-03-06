function createTransactions(transactions){
	var contractAddress = returnContractAddress();
	var contractInterface = returnContractInterface();
	var contract = contractInterface.at(contractAddress);
	var senderAddress = eth.accounts[0];
	var receiverAddress = eth.accounts[1];

	personal.unlockAccount(senderAddress, "1234", 10000);
	var name = "testOffering";
	var category = ["ParkingCategory", "BusCategory", "TrafficCategory", "ChargingCategory"];
	var model = ["FREE", "PER_MONTH", "PER_ACCESS"];
	var price = 10;
	var endpoint = "100.101.102.103";
	var inputs = "input1,input2,input3";
	var outputs = "output1,output2,output3";
	var year = 2018;
	var month = 4;
	var day = 26;	
	var hour = 12;

	for(i = 0; i < transactions; i++) {
		offerName = name + i;
		var makeOffer = contract.addOffer.getData(offerName, category[i%4], model[i%3], price, endpoint, inputs, outputs, year, month, day, hour);
		eth.sendTransaction({from:senderAddress, to:contractAddress, data: makeOffer, gas:600000});
	}

}

function createDemoTransactions(transactions){
  var contractAddress = returnContractAddress();
  var contractInterface = returnContractInterface();
  var contract = contractInterface.at(contractAddress);
  var senderAddress = eth.accounts[0];
  var receiverAddress = eth.accounts[1];

  personal.unlockAccount(senderAddress, "1234", 10000);
  var name = "Offering";
  var category = ["MobilityFeatureCategory", "TransportationCategory", "MobilityFeatureCategory", "TransportationCategory"];
  var model = ["FREE", "PER_MONTH", "PER_ACCESS"];
  var price = 0;
  var endpoint = "192.168.1.105";
  var inputs = "1,2,3";
  var outputs = "1,2,3";
  var year = 2018;
  var month = 6;
  var day = 30; 
  var hour = 12;

  for(i = 0; i < 4; i++) {
    offerName = name + (i+1);
    price = price + 10;
    var makeOffer = contract.addOffer.getData(offerName, category[i%4], model[2], price, endpoint, inputs, outputs, year, month, day, hour);
    eth.sendTransaction({from:senderAddress, to:contractAddress, data: makeOffer, gas:600000});
  }

}

function moreGas(transactions){
  for(i = 0; i < transactions; i++) {
    var senderAddress = eth.accounts[0];
    var receiverAddress = eth.accounts[1];
    eth.sendTransaction({from:senderAddress, to:receiverAddress, gas:25000});
  }
}

function createUnfairTransactions(transactions, unfairAmount){
	var contractAddress = returnContractAddress();
	var contractInterface = returnContractInterface();
	var contract = contractInterface.at(contractAddress);
	var senderAddress = eth.accounts[0];
	var receiverAddress = eth.accounts[1];

	personal.unlockAccount(senderAddress, "1234", 10000);
	var name = "testOffering";
	var categoryUnfair = ["ParkingCategory"];
	var categoryRest = ["BusCategory", "TrafficCategory", "ChargingCategory"];
	var model = ["FREE", "PER_MONTH", "PER_ACCESS"];
	var price = 10;
	var endpoint = "100.101.102.103";
	var inputs = "input1,input2,input3";
	var outputs = "output1,output2,output3";
	var year = 2018;
	var month = 4;
	var day = 26;	
	var hour = 12;

	for(i = 0; i < transactions; i++) {
		if (i < unfairAmount){
			offerName = name + i;
			var makeOffer = contract.addOffer.getData(offerName, categoryUnfair[0], model[i%3], price, endpoint, inputs, outputs, year, month, day, hour);
			eth.sendTransaction({from:senderAddress, to:contractAddress, data: makeOffer, gas:600000});
		}
		else{
			offerName = name + i;
			var makeOffer = contract.addOffer.getData(offerName, categoryRest[i%3], model[i%3], price, endpoint, inputs, outputs, year, month, day, hour);
			eth.sendTransaction({from:senderAddress, to:contractAddress, data: makeOffer, gas:600000});
		}
	}

}

function deleteTransactions(startID, endID){
	var contractAddress = returnContractAddress();
	var contractInterface = returnContractInterface();
	var contract = contractInterface.at(contractAddress);
	var senderAddress = eth.accounts[0];
	var receiverAddress = eth.accounts[1];

	personal.unlockAccount(senderAddress, "1234", 10000);
	for(i = startID; i <= endID; i++) {
		var deleteOffer = contract.deleteOffer.getData(i);
		eth.sendTransaction({from:senderAddress, to:contractAddress, data: deleteOffer, gas:30000});
	}
}

function modifyTransactions(startID, endID){
	var contractAddress = returnContractAddress();
	var contractInterface = returnContractInterface();
	var contract = contractInterface.at(contractAddress);
	var senderAddress = eth.accounts[0];
	var receiverAddress = eth.accounts[1];

	personal.unlockAccount(senderAddress, "1234", 10000);
	for(i = startID; i <= endID; i++) {
		var deleteInput = contract.deleteInput.getData(i, "192.168.1.101");
		eth.sendTransaction({from:senderAddress, to:contractAddress, data: deleteInput, gas:30000});
	}
}

function returnContractAddress(){
  //var contractAddress = "0xeeabb8864589e3545ae6f7ebcf8e4f86faa0dfdb1b24add6acd315456bdb7e96ded9c708f0f07894"; //New Fair contract
  var contractAddress = "0x4f719379a1e86D9d4D84A757eEB70222629B2608"; //Unfair contract
	return contractAddress;
}

function returnContractInterface(){
	var contractInterface = eth.contract( [
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_ID",
          "type": "uint256"
        }
      ],
      "name": "CheckExistingOffer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_ID",
          "type": "uint256"
        }
      ],
      "name": "createSubscription",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        }
      ],
      "name": "returnSubscribers",
      "outputs": [
        {
          "name": "",
          "type": "address[]"
        },
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        },
        {
          "name": "subscriber",
          "type": "address"
        }
      ],
      "name": "checkSubscription",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        }
      ],
      "name": "deleteSubscription",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]);
	return contractInterface;
}