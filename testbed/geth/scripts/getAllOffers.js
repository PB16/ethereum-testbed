function getAllOffers() {
  var contractInterface = eth.contract([
    {
      "constant": true,
      "inputs": [],
      "name": "getMyOffers",
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
      "inputs": [],
      "name": "getOfferLength",
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
      "constant": false,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        },
        {
          "name": "adressOfEndpoint",
          "type": "string"
        }
      ],
      "name": "setEndpoint",
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
        }
      ],
      "name": "deleteEndpoint",
      "outputs": [],
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
      "name": "getOffer",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        },
        {
          "name": "",
          "type": "address"
        },
        {
          "name": "",
          "type": "string"
        },
        {
          "name": "",
          "type": "string"
        },
        {
          "name": "",
          "type": "uint256"
        },
        {
          "name": "",
          "type": "string"
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
      "name": "deleteOffer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
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
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getAllOffers",
      "outputs": [
        {
          "components": [
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
              "name": "endTime",
              "type": "uint256"
            },
            {
              "name": "endpoint",
              "type": "string"
            }
          ],
          "name": "",
          "type": "tuple[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "getUniqueID",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
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
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    }
  ]);

  var contractResult = contractInterface.at("0x010de9544731130c352f074aa23bae5178963301");
  /*var iterator = contractResult.getOfferLength();
  var Offers = new Array(10);
  for(var i = 1; i < iterator; i++) {
    Offers[i] = new Array(6);
    for(var j = 0; j < 6; j++) {
      Offers[i][j] = contractResult.getOffer(i)[j];
    }
    //[ID, Addr, Name, Category, Price, Endpoint]
    console.log("ID = " + Offers[i][0] + ", Name = " + Offers[i][2] + ", Category = " + Offers[i][3] + ", Price = " + Offers[i][4]);
  }*/
  var Offers = contractResult.getAllOffers();
  console.log(Offers);
}


/*  var pro
  var name = contractResult.getOffer(i)[2];
  var category = contractResult.getOffer(i)[3];
  var price = contractResult.getOffer(i)[4];
  var endpoint = contractResult.getOffer(i)[5];
*/
