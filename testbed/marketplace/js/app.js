App = {
  web3Provider: "",
  contracts: {},

  init: function() {
    return App.initWeb3();
  },

  initWeb3: function() {
    return App.initContract();
  },


  initContract: function() {
    var contractInterface = web3.eth.contract([ { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": false, "inputs": [ { "name": "name", "type": "string" }, { "name": "category", "type": "string" }, { "name": "model", "type": "string" }, { "name": "price", "type": "uint256" }, { "name": "endpoint", "type": "string" }, { "name": "inputs", "type": "string" }, { "name": "outputs", "type": "string" }, { "name": "year", "type": "uint16" }, { "name": "month", "type": "uint8" }, { "name": "day", "type": "uint8" }, { "name": "hour", "type": "uint8" } ], "name": "addOffer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getMyOffers", "outputs": [ { "name": "", "type": "uint256[]", "value": [ "0", "0", "0", "0", "1", "2", "3" ] } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "ID", "type": "uint256" } ], "name": "deleteOffer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getAllOffers", "outputs": [ { "components": [ { "name": "ID", "type": "uint256" }, { "name": "provider", "type": "address" }, { "name": "name", "type": "string" }, { "name": "category", "type": "string" }, { "name": "price", "type": "uint256" }, { "name": "endTime", "type": "uint256" }, { "name": "endpoint", "type": "string" }, { "name": "inputs", "type": "bytes32[]" }, { "name": "outputs", "type": "bytes32[]" } ], "name": "", "type": "tuple[]" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "ID", "type": "uint256" } ], "name": "getOffer", "outputs": [ { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" }, { "name": "", "type": "string", "value": "" }, { "name": "", "type": "string", "value": "" }, { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "string", "value": "" }, { "name": "", "type": "bytes32[]", "value": [] }, { "name": "", "type": "bytes32[]", "value": [] } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getOfferLength", "outputs": [ { "name": "", "type": "uint256", "value": "4" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "destroy", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" } ]);

    var contractResult = contractInterface.at("0x7d0363f14fCE1123E720435C451234B379dEff97");
    var iterate = 0;
    contractResult.getOfferLength(function(error, result){
      if(!error) {
        iterate = result.c[0];
        var offersRow = $('#offersRow');
        var offerTemplate = $('#offerTemplate');
        for(var i = 1; i < iterate; i++) {
          contractResult.getOffer(i, function(error, result){
               if(!error) {
                  offerTemplate.find('.panel-title').text(result[2]);
                  offerTemplate.find('.unt-category').text(result[3]);
                  offerTemplate.find('.unt-price').text(result[4]);
                  // Input Elements
                  var inputList = "<ul>";
                  result[6].forEach(function(input) {
                    inputList = inputList.concat("<li>" + web3.toUtf8(input) + "</li>");
                  });
                  inputList = inputList.concat("</ul>");
                  offerTemplate.find('.unt-inputList').html(inputList);

                  // Output Elements
                  var outputList = "<ul>";
                  result[7].forEach(function(input) {
                    outputList = outputList.concat("<li>" + web3.toUtf8(input) + "</li>");
                  });
                  outputList = outputList.concat("</ul>");

                  offerTemplate.find('.unt-outputList').html(outputList);
                  offersRow.append(offerTemplate.html());
               }

               else {
                 console.error(error);
               }
           });
        }
      }
      else {
        return -1;
      }
    });
    return App.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-adopt', App.handleAdopt);
  },
};

$(function() {
  $(window).load(function() {
    App.init();
  });
});
