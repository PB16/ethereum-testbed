
function deleteTransactions(startID, endID){
	var contractAddress = "0xc8f391e7449601d8bd1ac3cde0a233ec64af9371";
	var contractInterface = returnContractInterface();
	var contract = contractInterface.at(contractAddress);
	var senderAddress = eth.accounts[1];
	var receiverAddress = eth.accounts[1];


	personal.unlockAccount(senderAddress, "1234", 10000);

	for(i = startID; i =< endID; i++) {
		var deleteOffer = contract.deleteOffer.getData(i);
		eth.sendTransaction({from:senderAddress, to:contractAddress, data: deleteOffer, gas:30000});
	}

}
function returnContractInterface(){
	var contractInterface = eth.contract([
	{
	  "inputs": [],
	  "payable": false,
	  "stateMutability": "nonpayable",
	  "type": "constructor"
	},
	{
	  "constant": false,
	  "inputs": [
		{
		  "name": "name",
		  "type": "string"
		},
		{
		  "name": "category",
		  "type": "string"
		},
		{
		  "name": "model",
		  "type": "string"
		},
		{
		  "name": "price",
		  "type": "uint256"
		},
		{
		  "name": "endpoint",
		  "type": "string"
		},
		{
		  "name": "inputs",
		  "type": "string"
		},
		{
		  "name": "outputs",
		  "type": "string"
		},
		{
		  "name": "year",
		  "type": "uint16"
		},
		{
		  "name": "month",
		  "type": "uint8"
		},
		{
		  "name": "day",
		  "type": "uint8"
		},
		{
		  "name": "hour",
		  "type": "uint8"
		}
	  ],
	  "name": "addOffer",
	  "outputs": [],
	  "payable": false,
	  "stateMutability": "nonpayable",
	  "type": "function"
	},
	{
	  "constant": false,
	  "inputs": [
		{
		  "name": "ID",
		  "type": "uint256"
		},
		{
		  "name": "_input",
		  "type": "string"
		}
	  ],
	  "name": "deleteInput",
	  "outputs": [
		{
		  "name": "deleted",
		  "type": "bool"
		}
	  ],
	  "payable": false,
	  "stateMutability": "nonpayable",
	  "type": "function"
	},
	{
	  "constant": false,
	  "inputs": [
		{
		  "name": "ID",
		  "type": "uint256"
		},
		{
		  "name": "_output",
		  "type": "string"
		}
	  ],
	  "name": "deleteOutput",
	  "outputs": [
		{
		  "name": "deleted",
		  "type": "bool"
		}
	  ],
	  "payable": false,
	  "stateMutability": "nonpayable",
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
	  "name": "deleteOffer",
	  "outputs": [],
	  "payable": false,
	  "stateMutability": "nonpayable",
	  "type": "function"
	},
	{
	  "constant": true,
	  "inputs": [
		{
		  "name": "_ID",
		  "type": "uint256"
		}
	  ],
	  "name": "getOffer",
	  "outputs": [
		{
		  "name": "ID",
		  "type": "uint256"
		},
		{
		  "name": "provider",
		  "type": "address"
		},
		{
		  "name": "name",
		  "type": "string"
		},
		{
		  "name": "category",
		  "type": "string"
		},
		{
		  "name": "price",
		  "type": "uint256"
		},
		{
		  "name": "endpoint",
		  "type": "string"
		},
		{
		  "name": "inputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "outputs",
		  "type": "bytes32[]"
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
		  "name": "category",
		  "type": "string"
		},
		{
		  "name": "price",
		  "type": "uint256"
		},
		{
		  "name": "inputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "outputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "ittr",
		  "type": "uint256"
		}
	  ],
	  "name": "offeringQueryOne",
	  "outputs": [
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
		  "name": "category",
		  "type": "string"
		},
		{
		  "name": "price",
		  "type": "uint256"
		},
		{
		  "name": "inputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "outputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "ittr",
		  "type": "uint256"
		}
	  ],
	  "name": "offeringQueryList",
	  "outputs": [
		{
		  "name": "",
		  "type": "uint256[]"
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
		  "name": "category",
		  "type": "string"
		},
		{
		  "name": "price",
		  "type": "uint256"
		},
		{
		  "name": "inputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "outputs",
		  "type": "bytes32[]"
		},
		{
		  "name": "ittr",
		  "type": "uint256"
		}
	  ],
	  "name": "offeringQueryListTest",
	  "outputs": [
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
	  "inputs": [],
	  "name": "getOfferLength",
	  "outputs": [
		{
		  "name": "length",
		  "type": "uint256"
		}
	  ],
	  "payable": false,
	  "stateMutability": "view",
	  "type": "function"
	},
	{
	  "constant": false,
	  "inputs": [],
	  "name": "destroy",
	  "outputs": [],
	  "payable": false,
	  "stateMutability": "nonpayable",
	  "type": "function"
	}
  ]);
	return contractInterface;
}