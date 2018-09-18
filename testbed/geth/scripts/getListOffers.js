function offeringQueryList(category, price, inputs, outputs, ittr, list, loops) {
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
        },
        {
          "name": "offSet",
          "type": "uint256"
        }
      ],
      "name": "offeringQueryOneOffset",
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

  var t0 = Date.now();
  //var contractResult = contractInterface.at("0x1b24add6acd315456bdb7e96ded9c708f0f07894"); // Fair Contract
  var contractResult = contractInterface.at("0xc668da74171eaadd4bd1015bb67fa95013aa147e"); // Unfair Contract
  var inputs32 = [];
  for(var i=0; i<inputs.length; i++) {
    inputs32.push(web3.fromAscii(inputs[i]));
  }

  var outputs32 = [];
  for(var i=0; i<outputs.length; i++) {
    outputs32.push(web3.fromAscii(outputs[i]));
  }

  if(list == true) {
    var resultList = contractResult.offeringQueryList(category, price, inputs32, outputs32, ittr);

    var t1 = Date.now();
    console.log("Search took: " + (t1 - t0) + " milliseconds.");
    var useFull = [];
    for(var i = 0; i < resultList.length; i++) {
      if(resultList[i] != 0)
        useFull.push(resultList[i]);
    }

    t0 = Date.now();
    var rand = Math.random() * useFull.length;
    var getData = contractResult.getOffer(useFull[rand]);
    t1 = Date.now();
    console.log("Lookup time: " + (t1 - t0) + " milliseconds.")
    return getData[5];
  }

  else  {
    // Fill array
    var uniqueOffers = [];
    var arrayLength = Math.ceil(ittr / 4);
    for (var i = 0; i < arrayLength; i++) uniqueOffers[i] = 0;
    if(loops != 0) {
      for(var i=0; i<loops; i++) {
        if((i%10) == 0) {
          console.log("loops:" + i + "/" + loops);
        }

        var rand  = Math.floor(ittr * rnd());
        var resultOne = contractResult.offeringQueryOneOffset(category, price, inputs32, outputs32, ittr, rand);
        var getData = contractResult.getOffer(resultOne);
        var index = Math.floor(getData[0]-1);
        //console.log(rand + " = " + getData[0] + " = " + index);
        uniqueOffers[index]++;
      }
      console.log("\n \n");
      console.log(uniqueOffers);
      var sum = 0;
      for(var i=0; i<arrayLength; i++) {
        var mean = (1 / arrayLength) * loops;
        sum = sum + Math.pow( (uniqueOffers[i] - mean), 2 );
      }

      var max = Math.max.apply(Math, uniqueOffers); // 306
      var min = Math.min.apply(Math, uniqueOffers);
      console.log(max + "-" + min + "=" + (max-min));
      var standard = Math.sqrt((sum / loops));
      console.log(standard);
      return 0;
    }

    else {
      for(var i=5; i<=12; i++) {
        var average = 0;
        for(var j=0; j<3; j++) {
          var rand  = Math.floor(Math.pow(2, i) * rnd());     // returns a number between 0 and ittr
          var t0 = Date.now();
          var resultOne = contractResult.offeringQueryOneOffset(category, price, inputs32, outputs32, Math.pow(2, i), rand);
          var t1 = Date.now();
          var getData = contractResult.getOffer(resultOne);
          average = average + (t1 - t0);
          console.log(Math.pow(2, i) + ";" + (t1 - t0));
        }
        console.log(Math.pow(2, i) + ";" + (average / 3));
      }
    }
    return getData[0];
  }
}

function rnd() {
  return Math.random();
}

function removeElementsWithValue(arr, val) {
    var i = arr.length;
    while (i--) {
        if (arr[i] === val) {
            arr.splice(i, 1);
        }
    }
    return arr;
}
