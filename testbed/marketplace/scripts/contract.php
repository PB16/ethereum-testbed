<?php

use Web3\Contract;
use Web3\Web3;
use Web3\Providers\HttpProvider;
use Web3\Utils;
require('./vendor/autoload.php');

class ContractClass
{
  protected $contract;
  protected $contractAddress;
  protected $testAbi = '[
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "category",
          "type": "string"
        },
        {
          "name": "model",
          "type": "string"
        },
        {
          "name": "price",
          "type": "uint256"
        },
        {
          "name": "endpoint",
          "type": "string"
        },
        {
          "name": "inputs",
          "type": "string"
        },
        {
          "name": "outputs",
          "type": "string"
        },
        {
          "name": "year",
          "type": "uint16"
        },
        {
          "name": "month",
          "type": "uint8"
        },
        {
          "name": "day",
          "type": "uint8"
        },
        {
          "name": "hour",
          "type": "uint8"
        }
      ],
      "name": "addOffer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getMyOffers",
      "outputs": [
        {
          "name": "offerings",
          "type": "uint256[]"
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
      "name": "deleteOffer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
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
      "name": "getOffer",
      "outputs": [
        {
          "name": "ID",
          "type": "uint256"
        },
        {
          "name": "provider",
          "type": "address"
        },
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "category",
          "type": "string"
        },
        {
          "name": "price",
          "type": "uint256"
        },
        {
          "name": "endpoint",
          "type": "string"
        },
        {
          "name": "inputs",
          "type": "bytes32[]"
        },
        {
          "name": "outputs",
          "type": "bytes32[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getOfferLength",
      "outputs": [
        {
          "name": "length",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "destroy",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]';

  public function call() {
    $web3 = new Web3('http://127.0.0.1:8545'); //Provider
    $this->contract = new Contract($web3->provider, $this->testAbi);
    $this->contractAddress = '0x39c267ca27c3c3adbbb62d42b06b2bd1e93572ad';
    $contract = $this->contract;
    $contract->at($this->contractAddress)->call("getOfferLength", function($error, $result) use ($contract) {
      if ($err !== null) {
          return $this->fail($err->getMessage());
      }
      if (isset($result)) {

        for($i=1; $i < $result["length"].'int'; $i++) {
          echo '<div class="col-sm-6 col-md-4 col-lg-3">';
          echo '<div class="panel panel-default">';
          $contract->at($this->contractAddress)->call("getOffer", $i, function($error, $result) use ($contract) {
            echo '<div class="panel-heading">';
            echo "<strong>Title</h3></strong>: <span class='unt-title'>" .
            $result["name"] . "</span><br/>";
            echo '</div>';
            echo '<div class="panel-body">';
            echo "<strong>Category</strong>: <span class='unt-category'>" .
            $result["category"] . "</span><br/>";
            echo "<strong>Price</strong>: <span class='unt-price'>" .
            $result["price"] . "</span><br/>";
            echo "<strong>Endpoint</strong>: <span class='unt-endpoint'>" .
            $result["endpoint"] . "</span><br/>";

            echo '<strong>Inputs</strong>: <span class="unt-inputList"></span>';
            echo '<ul>';
            foreach($result["inputs"] as $input) {
              echo '<li>' . Utils::hexToBin($input) . '</li>';
            }
            echo '</ul>';
            echo '</span>';

            echo '<strong>Outputs</strong>: <span class="unt-outputList"></span>';
            echo '<ul>';
            foreach($result["outputs"] as $output) {
              echo '<li>' . Utils::hexToBin($output) . '</li>';
            }
            echo '</ul>';
            echo '</span>';
          });
          echo '</div></div></div>';
        }
      }
    });
  }
}

/*
$contract->at($address)->call("getOfferLength", function($error, $result) use ($contract) {
  if($error) {
    throw $error;
  }
  else {
    if ($result) {
      foreach($result as $value) {
        for($i=1; $i < (int)($value.'int'); $i++) {
          $contract->call("getOffer", $i,  function($getOfferError, $getOfferResult) use ($contract) {
            foreach($getOfferResult as $offer) {
              var_dump($offer[5]);
              echo "\n \n";
            }
          });
        }
      }
    }
  }
});
$contract = new Contract($web3->provider, $testAbi);
$address = "0x931acbb5723c5b11c3bc73303538e2a73cb29f5f";
$id = 1;
$contract->at($address)->call("getOffer", 3, function($error, $result) use ($contract) {
  if($error) {
    throw $error;
  }
  else {
    if ($result) {
      $result->assertEquals($result['firstName'], 'Peter');
      $this->assertEquals($result['lastName'], 'Lai');
      $this->assertEquals($result['age']->toString(), '18');

    }
  }
});
}

*/
