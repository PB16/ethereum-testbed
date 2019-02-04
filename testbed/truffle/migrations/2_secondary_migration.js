var subscription = artifacts.require("./subscription.sol");


module.exports = function(deployer) {
  deployer.deploy(subscription);
};
