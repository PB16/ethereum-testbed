pragma solidity ^0.5.2;

// not implementated contract but needed as a strutual guide for the checkExistingOffer to be able to call contract on chain
contract offerFunction {
	function getOffer(uint _ID) public pure returns (uint ID, address provider, string memory name, string memory category, uint price, string memory endpoint, bytes32[] memory inputs, bytes32[] memory outputs);
}

contract subscription {
	
	struct SubscriberStruct {
    	uint ID;
     	address[] subscribers;
    }

	address owner;
	mapping (uint => SubscriberStruct) subscriptions;
	
	constructor() public{
		owner = msg.sender;
	}

	function CheckExistingOffer(uint _ID) public pure returns(bool){
		offerFunction func = offerFunction(0x54d9fAa15b8401A9AF973fBd3838f1E3c1dBb9E3);
		(uint256 ID, address provider, string memory name, string memory category, uint256 price, string memory endpoint, bytes32[] memory inputs, bytes32[] memory outputs) = func.getOffer(_ID);
		if (ID > 0 && provider != address(0x0)){
			return true;
		}
		else{
			return false;
		} 
	}

	function createSubscription(uint _ID) public returns(bool){
		if (subscriptions[_ID].ID == 0){
			SubscriberStruct memory subscriptionList;
			address[] memory firstSubscriber = new address[](1);
			firstSubscriber[0] = msg.sender;
			subscriptionList.ID = _ID;
			subscriptionList.subscribers = firstSubscriber;
			subscriptions[_ID] = subscriptionList;
		}
		else{
			subscriptions[_ID].subscribers.push(msg.sender);
		}
		return true;
	}

	function returnSubscribers(uint ID) public view returns(address[] memory, uint){
		return (subscriptions[ID].subscribers, subscriptions[ID].subscribers.length);
	}

	function checkSubscription(uint ID, address subscriber) public view returns(bool){
		if (subscriptions[ID].ID != 0){
			for(uint i = 0; i < subscriptions[ID].subscribers.length; i++){
				if (subscriptions[ID].subscribers[i] == subscriber){
					return true;
				}
			}
			return false;
		}
		else{
			return false;
		}

	}

	function GetSubscriptionIndex(uint ID, address subscriber) internal view returns(bool, uint){
		if (subscriptions[ID].ID != 0){
			for(uint i = 0; i < subscriptions[ID].subscribers.length; i++){
				if (subscriptions[ID].subscribers[i] == subscriber){
					return (true, i);
				}
			}
			return (false, 0);
		}
		else{
			return (false, 0);
		}

	}

	function deleteSubscription(uint ID) public returns(bool){
		(bool state, uint256 index) = GetSubscriptionIndex(ID, msg.sender);
		if (state == true){
			subscriptions[ID].subscribers[index] = subscriptions[ID].subscribers[subscriptions[ID].subscribers.length -1]; 
			delete subscriptions[ID].subscribers[subscriptions[ID].subscribers.length -1];
			subscriptions[ID].subscribers.length--;
			return true;
		}
		return false;
	}
} 