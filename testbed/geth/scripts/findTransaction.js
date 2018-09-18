function findTransaction() {
  //contractAddress = 0xb54291b6516850dfA8FaB00481BD88cF701cE202;
  //var filter = eth.filter({address: 0xb54291b6516850dfA8FaB00481BD88cF701cE202, to:'latest'});

  var filter = web3.eth.filter('pending');

  filter.watch(function (error, log) {
    console.log(log); //  {"address":"0x0000000000000000000000000000000000000000", "data":"0x0000000000000000000000000000000000000000000000000000000000000000", ...}
  });
}
