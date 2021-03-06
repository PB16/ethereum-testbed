pragma solidity ^0.5.2;

import "./StringUtils.sol";

contract Pricing {
  function isPricingModelAllowed(string memory model) pure internal returns(bool) {
    if(StringUtils.equal(model, "FREE")) {
      return true;
    }
    if(StringUtils.equal(model, "PER_ACCESS")) {
      return true;
    }
    if(StringUtils.equal(model, "PER_BYTE")) {
      return true;
    }
    if(StringUtils.equal(model, "PER_MESSAGE")) {
      return true;
    }
    if(StringUtils.equal(model, "PER_MONTH")) {
      return true;
    }
    return false;
  }
}
