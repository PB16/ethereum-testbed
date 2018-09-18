<?php
use Web3\Contract;
use Web3\Web3;
use Web3\Providers\HttpProvider;
use Web3\Utils;
require('./vendor/autoload.php');

class AuthClass {
  protected $contract;
  protected $contractAddress;

  protected $testAbi = '[
    {
      "constant": true,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        }
      ],
      "name": "returnSubscribers",
      "outputs": [
        {
          "name": "",
          "type": "address[]"
        },
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        }
      ],
      "name": "deleteSubscription",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        }
      ],
      "name": "createSubscription",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "ID",
          "type": "uint256"
        },
        {
          "name": "subscriber",
          "type": "address"
        }
      ],
      "name": "checkSubscription",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_ID",
          "type": "uint256"
        }
      ],
      "name": "CheckExistingOffer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    }
  ]';

  public function checkSubscription($offer, $address) {
    $web3 = new Web3('http://127.0.0.1:8545'); //P rovider
    $this->contract = new Contract($web3->provider, $this->testAbi);
    $this->contractAddress = '0x1c149aeb1cd960b20e57f166011e955006e02043';
    $contract = $this->contract;
    $contract->at($this->contractAddress)->call("checkSubscription", $offer, $address, function($error, $result) use ($contract) {
      if ($err !== null) {
          return $this->fail($err->getMessage());
      }
      else {
        if($result[""]) {
          echo "Subscribed!";
        }
        else {
          echo "Not subscribed";
        }
      }
    });
  }
}
?>
