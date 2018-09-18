<?php
  function checkDB($address, $token) {
    require_once('dbConnect.php');
    $conn = dbConnect();
    $result = $conn->prepare("SELECT id FROM token_registry WHERE address= :addr");
    $result->bindParam(':addr', $address);
    $result->execute();

    if($row = $result->fetch()) {
      return "User Exists!";
    }
    else {
      $tokenValues = explode("-", $token);
      $expire = $tokenValues[7] . "-" . $tokenValues[6] . "-" . $tokenValues[5];
      $addToken ="INSERT INTO `token_registry`(`id`, `address`, `token`, `expire`)
      VALUES ('', '$address', '$token', '$expire')";
      $resultCreateUser = $conn->prepare($addToken);
      if($resultCreateUser->execute()) {
        return "TokenCreated";
      }
      else {
        return "TokenCreationFailed";
      }
    }
  }

  if (isset($_POST['address']) && isset($_POST['token'])) {
      echo checkDB($_POST['address'], $_POST['token']);
  }
?>
