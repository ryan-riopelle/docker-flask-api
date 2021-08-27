<html>
    <head>
        <title>My Observatory</title>
    </head>

    <body>
        <h1>Welcome to my Taco Shop</h1>
        <ul>
            <?php
            $json = file_get_contents('http://taco-service/');
            $obj = json_decode($json);
            $tacos = $obj->Tacos;
            foreach ($tacos as $taco) {
                echo "<li>$galaxy</li>";
            }
            ?>
        </ul>
    </body>
</html>