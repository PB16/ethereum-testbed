function getTransactionsByAccountNew(account) {
  var endBlockNumber = eth.blockNumber;
  console.log("endBlog = " + endBlockNumber);
  if(account == null) {
    for(var i = 0; i < endBlockNumber; i++) {
      var block = eth.getBlock(i, true);
      if(block.transactions != null) {
        block.transactions.forEach(function(e) {
          console.log("------ Block Number " + i + "-------")
          console.log("from = " + e.from);
          console.log("to = " + e.to);
          console.log("value = " + e.value + "\n \n");
        });
      }
    }
  }
  return "Script Complete";
}
