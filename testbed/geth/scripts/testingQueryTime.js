function testQueryTime() {
  var contractInterface = eth.contract(/* Offer contract ABI */);

  var contractResult = contractInterface.at(/* Offer contract address */);
  var iterator = contractResult.getOfferLength();

  var senderAddress = eth.accounts[0];
  personal.unlockAccount(senderAddress, "123456", 10000);

  var t0 = Date.now();

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

  var makeOffer = contract.addOffer.getData(offerName, category[0], model[0], price, endpoint, inputs, outputs, year, month, day, hour);
  eth.sendTransaction({from:senderAddress, to:contractAddress, data: makeOffer, gas:600000});

  while(true) {
    var offer = contractResult.getOffer(0, senderAddress, offerName, category[0], price, endpoint, inputs, outputs);
    if(offer != null || offer != "") {
      break;
    }
  }

  var t1 = Date.now();

  console.log("Successful query took " + (t1 - t0) + " milliseconds.")
}