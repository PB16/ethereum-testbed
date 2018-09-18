function auth(offer, address) {
  var contractInterface = web3.eth.contract([
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
        "name": "ID",
        "type": "uint256"
      }
    ],
    "name": "createSubscription",
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
  }
  ]);

  var contractResult = contractInterface.at("0x0acfCB78C7f42D4Ed25F1d72B1Ee7FaC75b9510A");
  contractResult.checkSubscription(offer, address ,function(error, result) {
    if(!error) {
      if(result == true) {
        //console.log(guid());
        addToken(address, guid());
      }
      else {
        console.log(false);
      }
    }
    else {
      console.log(error);
    }
  });
};

function addToken(address, token) {
  $.ajax({
    url: './php/dbInsert.php',
    type: 'post',
    data: {"address": address, "token": token},
    success:function(data) {
      console.log(data);
    }
  });
}


function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1);
  }

  function date() {
    var targetDate = new Date();
    targetDate.setDate(targetDate.getDate() + 10);
    var dd = targetDate.getDate();
    var mm = targetDate.getMonth() + 1; // 0 is January, so we must add 1
    var yyyy = targetDate.getFullYear();
    var dateString = dd + "-" + mm + "-" + yyyy;
    return dateString;
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4() + '-' + date();
};
