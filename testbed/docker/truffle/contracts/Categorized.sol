pragma solidity ^0.4.17;

import "./StringUtils.sol";

contract Categorized {
  function isCategoryAllowed(string category) pure internal returns(bool) {
    if(StringUtils.equal(category, "MobilityFeatureCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "ParkingCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "ParkingSpaceCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "ParkingSiteCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "TransportationCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "BikeSharingStationCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "CarDiagnosticsCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "BusCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "LocationTrackingCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "PeopleDensityEstimationCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "PeopleDensityOnBusCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "PeopleMobilityWithinAreaCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "PeopleDensityInAreaCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "TrafficCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "TrafficObstacleCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "TrafficDataCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "AccidentCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "ChargingCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "ChargingPointCategory")) {
      return true;
    }
    if(StringUtils.equal(category, "ChargingStationC")) {
      return true;
    }

    return false;
  }
}


/*
fooStruct myStruct = fooStruct(1,2);
fooStruct myStruct = fooStruct({foo:1, fighter:2});

// for temporary data - will only write to memory
fooStruct memory myStruct;
myStruct.figther = 2;

// for persistent data, has to be initialized from a state variable. `storage` is the default and a warning will be thrown by Solidity compiler versions starting with 4.17
fooStruct storage myStruct = ...;
myStruct.fighter = 2; // will write directly to storage

*/
