<?php
  $offer = $_GET['offer'];
  $address = $_GET['address'];
  require('./scripts/auth.php');
  $contract = new AuthClass();
  $contract->checkSubscription($offer, $address);
 ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
  </body>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="js/bootstrap.min.js"></script>
  <script src="js/web3.min.js"></script>
  <script src="js/auth.js"></script>
</html>
