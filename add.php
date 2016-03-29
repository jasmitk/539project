<?php  
session_start();

# require pdo line
require_once "pdo.php";


if (isset($_POST['Cancel']) ) {
    header('Location: home.html');
    exit();
}



// If the user requested "add"
if (isset ($_POST['Add'])) {
    if (isset($_POST['first_name']) && isset($_POST['last_name']) 
     && isset($_POST['email']) && isset($_POST['headline'])) && isset($_POST['summary'])){

        if ((strlen($_POST['first_name']) < 1) || (strlen($_POST['last_name']) < 1) || (strlen($_POST['email']) < 1) || (strlen($_POST['headline']) < 1) || (strlen($_POST['summary']) < 1)) {
            $_SESSION['failure'] = "All fields are required";
            header('Location: add.php');
            return;
        }

        else {
            $stmt = $pdo->prepare('INSERT INTO Profile
                (first_name, last_name, email, headline, summary) VALUES ( :fn, :ln, :e, :hl :s)');
            $stmt->execute(array(
                ':fn' => $_POST['first_name'],
                ':ln' => $_POST['last_name'],
                ':e' => $_POST['email'],
                ':hl' => $_POST['headline']),
                ':s' => $_POST['summary'])
            );
            header('Location: home.html');
            // echo "ALL OK";
            $_SESSION['success'] = "Record added";
        }
    }
}
?>
