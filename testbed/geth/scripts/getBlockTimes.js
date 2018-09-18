function extractTimes(startblock, endblock){
	var endBlockNumber = eth.blockNumber;
	var totalTransactions = 4096;
	var firstBlock = startblock;
	var lastBlock = endblock;
	var n = 5;
	var timeArray = [];
	var intervalArray = [];
	var intervalCount = 100;
	var sumOfTransactions = 0;

	for (var i = firstBlock; i <= lastBlock; i++) {
		transactions = eth.getBlockTransactionCount(i);
		sumOfTransactions += transactions;
		if (sumOfTransactions >= Math.pow(2, n)){
			time = eth.getBlock(i).timestamp - eth.getBlock(firstBlock).timestamp;
			timeArray.push(time);
			n++;
		}

		while(sumOfTransactions >= intervalCount){
			time = eth.getBlock(i).timestamp - eth.getBlock(firstBlock).timestamp;
			intervalArray.push(time);
			intervalCount = intervalCount + 100;
		}

		if (sumOfTransactions >= totalTransactions){
			break;
		}	
	}
	console.log("binary interval: " + timeArray);
	console.log("interval = 100: " + intervalArray);
	return true;
}

function blockTimes(){
	var endBlockNumber = eth.blockNumber;
	var timestamp = [];
	for (var i = 1; i <= endBlockNumber; i++) {
		block = eth.getBlock(i).timestamp - eth.getBlock(i-1).timestamp;
		timestamp.push(block);	
	}
	console.log(timestamp);
	return true;
}