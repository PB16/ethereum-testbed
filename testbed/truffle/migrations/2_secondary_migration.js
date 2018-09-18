var StringUtilsLib = artifacts.require("./StringUtils.sol");
var stringsLib = artifacts.require("./strings.sol");
var Offer = artifacts.require("./Offer.sol");

module.exports = function(deployer) {
  deployer.deploy(StringUtilsLib);
  deployer.deploy(stringsLib);
  deployer.link(StringUtilsLib, Offer)
  deployer.link(stringsLib, Offer)
  deployer.deploy(Offer);
};
