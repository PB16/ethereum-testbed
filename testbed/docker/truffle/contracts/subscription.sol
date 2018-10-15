pragma solidity ^0.4.19;

// not implementated contract but needed as a strutual guide for the checkExistingOffer to be able to call contract on chain
contract offerFunction {
	function getOffer(uint _ID) public constant returns (uint ID, address provider, string name, string category, uint price, string endpoint, bytes32[] inputs, bytes32[] outputs);
}

contract subscription {
	
	struct SubscriberStruct {
    	uint ID;
     	address[] subscribers;
    }

	address owner;
	mapping (uint => SubscriberStruct) subscriptions;
	
	function subscription() public{
		owner = msg.sender;
	}

	function CheckExistingOffer(uint _ID) public constant returns(bool){
		offerFunction func = offerFunction(0x54d9faa15b8401a9af973fbd3838f1e3c1dbb9e3);
		var (ID, provider, name, category, price, endpoint, inputs, outputs) = func.getOffer(_ID);
		if (ID > 0 && provider != 0x0){
			return true;
		}
		else{
			return false;
		} 
	}

	function createSubscription(uint _ID) public returns(bool){
		if (subscriptions[_ID].ID == 0){
			SubscriberStruct subscriptionList;
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

	function returnSubscribers(uint ID) public constant returns(address[], uint){
		return (subscriptions[ID].subscribers, subscriptions[ID].subscribers.length);
	}

	function checkSubscription(uint ID, address subscriber) public constant returns(bool){
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

	function GetSubscriptionIndex(uint ID, address subscriber) internal constant returns(bool, uint){
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
		var (state, index) = GetSubscriptionIndex(ID, msg.sender);
		if (state == true){
			subscriptions[ID].subscribers[index] = subscriptions[ID].subscribers[subscriptions[ID].subscribers.length -1]; 
			delete subscriptions[ID].subscribers[subscriptions[ID].subscribers.length -1];
			subscriptions[ID].subscribers.length--;
			return true;
		}
		return false;
	}
} 