pragma solidity ^0.4.11;

contract Lockbox {
  address owner;
  uint unlockTime;

  function Lockbox(uint _unlockTime) public {
    owner = msg.sender;
    unlockTime = _unlockTime;
  }

  function isUnlocked() internal view returns (bool) {
    return now >= unlockTime;
  }

  modifier onlyOwner() { require(msg.sender == owner); _; }
  modifier onlyWhenUnlocked() { require(isUnlocked()); _; }

  function withdrawBalance() payable onlyOwner onlyWhenUnlocked public {
    owner.transfer(address(this).balance);
  }
}

contract EasierToTestLockBox is Lockbox {
  function EasierToTestLockBox(uint _unlockTime) Lockbox(_unlockTime) public {}

  // Make the concept of "now" overridable.

  function getTime() internal view returns (uint) {
    return now;
  }

  // Replace "now" references with "getTime()".

  function isUnlocked() internal view returns (bool) {
    return getTime() >= unlockTime;
  }
}

contract LockboxTest is EasierToTestLockBox(now + 1 minutes) {

  // Add a manipulable fake clock to the contract.

  uint fakeClockTime = now;

  // Override the concept of "now" to use our fake clock.

  function getTime() internal view returns (uint) {
    return fakeClockTime;
  }

  // Test in the constructor.
  // If a `require` fails, Ethereum Wallet will warn you before you deploy.

  function LockboxTest() public {
    require(!isUnlocked());
    fakeClockTime = unlockTime;
    require(isUnlocked());
  }
}
