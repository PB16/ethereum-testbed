pragma solidity ^0.5.2;

import "./Categorized.sol";
import "./Pricing.sol";
import "./DateTime.sol";
import "./strings.sol";

contract Offer is Categorized, Pricing, DateTime {
	using strings for *;
	struct OfferStruct {
		// Ethereum parameters
		uint ID;
		address provider;
		// BIG IoT parameters
		string name;
		string category;
		uint price;
		uint endTime;
		string endpoint;
		bytes32[] inputs;
		bytes32[] outputs;
	}

	uint uniqueIdentifier;
	address owner;
	mapping (uint => OfferStruct) offers;

	constructor() public {
		uniqueIdentifier = 1;
		owner = msg.sender;
	}

	function addOffer(string memory name, string memory category, string memory model, uint price,
					  string memory endpoint, string memory inputs, string memory outputs, uint16 year,
					  uint8 month, uint8 day, uint8 hour) public {
		OfferStruct memory offer;
		offer.ID = uniqueIdentifier;
		offer.provider = msg.sender;
		if(isCategoryAllowed(category) && isPricingModelAllowed(model) && keccak256(abi.encode(name)) != keccak256(abi.encode(""))) {
			offer.name = name;
			offer.price = price;
			offer.category = category;
			offer.endTime = toTimestamp(year, month, day, hour);
			offers[uniqueIdentifier] = offer;
			changeEndpoint(uniqueIdentifier, endpoint);
			addInput(uniqueIdentifier, inputs);
			addOutput(uniqueIdentifier, outputs);
			uniqueIdentifier = uniqueIdentifier + 1;
		}
	}

	function GetIndex(uint ID, string memory input, string memory inputOutputIdentifier) internal pure returns(bool exists, uint index){
		if (offers[ID].ID != 0 && offers[ID].provider == msg.sender){
			if (keccak256(abi.encode(inputOutputIdentifier)) == keccak256(abi.encode('input'))){
				for(uint i = 0; i < offers[ID].inputs.length; i++){
					if (keccak256(abi.encode(offers[ID].inputs[i])) == keccak256(abi.encode(input))){
						return (true, i);
					}
				}
			}
			else {
				if (keccak256(abi.encode(inputOutputIdentifier)) == keccak256(abi.encode('output'))){
					for(uint j = 0; j < offers[ID].outputs.length; j++){
						if (keccak256(abi.encode(offers[ID].outputs[j])) == keccak256(abi.encode(input))){
							return (true, j);
						}
					}
				}
			}
		}
		return (false, 0);
	}

	function addInput(uint ID, string memory _inputs) internal{
		if (msg.sender == offers[ID].provider){
			strings.slice memory part;
			string memory temp = _inputs;
			uint count = temp.toSlice().count(",".toSlice());
			strings.slice memory str = _inputs.toSlice();
			for (uint i = 0; i < count+1; i++){
				str.split(",".toSlice(), part);
				offers[ID].inputs.push(strings.stringToBytes32(part.toString()));
			}
		}
	}

	function addOutput(uint ID, string memory _outputs) internal{
		if (msg.sender == offers[ID].provider){
			strings.slice memory part;
			string memory temp = _outputs;
			uint count = temp.toSlice().count(",".toSlice());
			strings.slice memory str = _outputs.toSlice();
			for (uint i = 0; i < count+1; i++){
				str.split(",".toSlice(), part);
				offers[ID].outputs.push(strings.stringToBytes32(part.toString()));
			}
		}
	}

	function deleteInput(uint ID, string memory _input) public returns(bool deleted){
		(bool state, uint256 index) = GetIndex(ID, _input, 'input');
		if (state == true){
			offers[ID].inputs[index] = offers[ID].inputs[offers[ID].inputs.length -1];
			delete offers[ID].inputs[offers[ID].inputs.length -1];
			offers[ID].inputs.length--;
			return true;
		}
		return false;
	}


	function deleteOutput(uint ID, string memory _output) public returns(bool deleted){
		(bool state, uint256 index) = GetIndex(ID, _output, 'output');
		if (state == true){
			offers[ID].outputs[index] = offers[ID].outputs[offers[ID].outputs.length -1];
			delete offers[ID].outputs[offers[ID].outputs.length -1];
			offers[ID].outputs.length--;
			return true;
		}
		return false;
	}

	function changeEndpoint(uint ID, string memory adressOfEndpoint) internal {
		if (msg.sender == offers[ID].provider){
			offers[ID].endpoint = adressOfEndpoint;
		}
	}

	function deleteOffer(uint ID) public {
		if(msg.sender == offers[ID].provider) {
			delete offers[ID];
		}
	}

	function getOffer(uint _ID) public pure returns (uint ID, address provider, string memory name, string memory category, uint price, string memory endpoint, bytes32[] memory inputs, bytes32[] memory outputs) {
		OfferStruct memory offer;
		offer = offers[_ID];
		return (offer.ID, offer.provider, offer.name, offer.category, offer.price, offer.endpoint, offer.inputs, offer.outputs);
	}

	function offeringQueryOne(string memory category, uint price, bytes32[] memory inputs, bytes32[] memory outputs, uint ittr) public pure returns (uint) {
		bytes memory byteCategory = bytes(category); // Uses memory
		if(byteCategory.length == 0) {
			return 9998;
		}
		uint blockNumber = block.number;
		for (uint i=1; i<ittr; i++) {
			if(keccak256(abi.encode(offers[i].category)) == keccak256(abi.encode(category))) {
				if(price == 0 && inputs.length == 0 && outputs.length == 0) {
					return i;
				}
				if(price != 0 && price < offers[i].price) {
					continue;
				}
				//Search for input
				uint inputCount = 0;
				if(inputs.length > 0) {
					for(uint j=0; j<offers[i].inputs.length; j++) {
						for(uint k=0; k<inputs.length; k++) {
							if(keccak256(abi.encode(offers[i].inputs[j])) == keccak256(abi.encode(inputs[k]))) {
								inputCount = inputCount + 1;
							}
						}
					}
				}
				// Means that the offers provides at least the number of inputs
				if(outputs.length > 0 && inputCount >= inputs.length) {
					//Search for output
					uint outputCount = 0;
					for(uint j=0; j<offers[i].outputs.length; j++) {
						for(uint k=0; k<outputs.length; k++) {
							if(keccak256(abi.encode(offers[i].outputs[j])) == keccak256(abi.encode(outputs[k]))) {
								outputCount = outputCount + 1;
							}
						}
					}
					if(outputCount >= outputs.length) {
						return i;
					}
				}
				else if(inputCount >= inputs.length) {
					return i;
				}
			}
		}
		return 9999;
	}

	function offeringQueryOneOffset(string memory category, uint price, bytes32[] memory inputs, bytes32[] memory outputs, uint ittr, uint offSet) public pure returns (uint) {
		bytes memory byteCategory = bytes(category); // Uses memory
		if(byteCategory.length == 0) {
			return 9998;
		}

		uint loopedThrough = 0;
		uint i=offSet;

		while (i<ittr) {
			if(i == ittr-1 && loopedThrough == 0) {
				i = 0;
				ittr = offSet;
				loopedThrough = 1;
			}

			if(keccak256(abi.encode(offers[i].category)) == keccak256(abi.encode(category))) {
				if(price == 0 && inputs.length == 0 && outputs.length == 0) {
					return i;
				}
				if(price != 0 && price < offers[i].price) {
					continue;
				}
				//Search for input
				uint inputCount = 0;
				if(inputs.length > 0) {
					for(uint j=0; j<offers[i].inputs.length; j++) {
						for(uint k=0; k<inputs.length; k++) {
							if(keccak256(abi.encode(offers[i].inputs[j])) == keccak256(abi.encode(inputs[k]))) {
								inputCount = inputCount + 1;
							}
						}
					}
				}
				// Means that the offers provides at least the number of inputs
				if(outputs.length > 0 && inputCount >= inputs.length) {
					//Search for output
					uint outputCount = 0;
					for(uint j=0; j<offers[i].outputs.length; j++) {
						for(uint k=0; k<outputs.length; k++) {
							if(keccak256(abi.encode(offers[i].outputs[j])) == keccak256(abi.encode(outputs[k]))) {
								outputCount = outputCount + 1;
							}
						}
					}
					if(outputCount >= outputs.length) {
						return i;
					}
				}
				else if(inputCount >= inputs.length) {
					return i;
				}
			}
			i = i + 1;
		}
		return 9999;
	}

	function offeringQueryList(string memory category, uint price, bytes32[] memory inputs, bytes32[] memory outputs, uint ittr) public pure returns (uint[] memory) {
		bytes memory byteCategory = bytes(category); // Uses memory
		uint[] memory candidates;
		if(byteCategory.length == 0) {
			return candidates;
		}
		for (uint i=1; i<ittr; i++) {
			if(keccak256(abi.encode(offers[i].category)) == keccak256(abi.encode(category))) {
				if(price != 0 && price < offers[i].price) {
					continue;
				}
				else if(inputs.length == 0 && outputs.length == 0) {
					candidates.push(i);
				}
				else {
					//Search for input
					uint inputCount = 0;
					if(inputs.length > 0) {
						for(uint j=0; j<offers[i].inputs.length; j++) {
							for(uint k=0; k<inputs.length; k++) {
								if(keccak256(abi.encode(offers[i].inputs[j])) == keccak256(abi.encode(inputs[k]))) {
									inputCount = inputCount + 1;
								}
							}
						}
					}
					// Means that the offers provides at least the number of inputs
					if(outputs.length > 0 && inputCount >= inputs.length) {
						//Search for output
						uint outputCount = 0;
						for(uint j=0; j<offers[i].outputs.length; j++) {
							for(uint k=0; k<outputs.length; k++) {
								if(keccak256(abi.encode(offers[i].outputs[j])) == keccak256(abi.encode(outputs[k]))) {
									outputCount = outputCount + 1;
								}
							}
						}
						if(outputCount >= outputs.length) {
							candidates.push(i);
						}
					}
					else if(inputCount >= inputs.length) {
						candidates.push(i);
					}
				}
			}
		}
		return candidates;
	}

	function offeringQueryListTest(string memory category, uint price, bytes32[] memory inputs, bytes32[] memory outputs, uint ittr) public pure returns (uint) {
		bytes memory byteCategory = bytes(category); // Uses memory
		uint result = 0;
		uint[] memory candidates;
		candidates.push(1);
		if(byteCategory.length == 0) {
			return 0;
		}
		for (uint i=1; i<ittr; i++) {
			if(keccak256(abi.encode(offers[i].category)) == keccak256(abi.encode(category))) {
				if(price != 0 && price < offers[i].price) {
					continue;
				}
				else if(inputs.length == 0 && outputs.length == 0) {
					result = i;
				}
				else {
					//Search for input
					uint inputCount = 0;
					if(inputs.length > 0) {
						for(uint j=0; j<offers[i].inputs.length; j++) {
							for(uint k=0; k<inputs.length; k++) {
								if(keccak256(abi.encode(offers[i].inputs[j])) == keccak256(abi.encode(inputs[k]))) {
									inputCount = inputCount + 1;
								}
							}
						}
					}
					// Means that the offers provides at least the number of inputs
					if(outputs.length > 0 && inputCount >= inputs.length) {
						//Search for output
						uint outputCount = 0;
						for(uint j=0; j<offers[i].outputs.length; j++) {
							for(uint k=0; k<outputs.length; k++) {
								if(keccak256(abi.encode(offers[i].outputs[j])) == keccak256(abi.encode(outputs[k]))) {
									outputCount = outputCount + 1;
								}
							}
						}
						if(outputCount >= outputs.length) {
							result = i;
						}
					}
					else if(inputCount >= inputs.length) {
						result = i;
					}
				}
			}
		}
		return result;
	}

	function getOfferLength() public pure returns (uint length){
		uint offerLength = uniqueIdentifier;
		return offerLength;
	}

	function destroy() public {
		if(owner == msg.sender) {
			selfdestruct(owner);
		}
	}
}
