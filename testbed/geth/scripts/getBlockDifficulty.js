var txtFile = "/var/www/html/difficultyPlot/file.txt";
var file = new File(txtFile);

endBlockNumber = eth.blockNumber;
var difficulty = [];
var xArray = [];
file.open("w");
for (var i = 0; i <= endBlockNumber; i++) {
	block = eth.getBlock(i).difficulty;
	difficulty.push(block);	
	xArray.push(i);
	file.writeln(i, block);
}
file.close();
/*var trace = {
	x:xArray,
	y:difficulty,
	type:'line'
};
var data = [trace];
plot = document.getElementById('plot');
plotly.plot(plot, data);
*/
