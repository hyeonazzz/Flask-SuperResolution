<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Potenza - Job Application Form Wizard with Resume upload and Branch feature">
    <meta name="author" content="Ansonika">
    <title>Potenza | Job Application Form Wizard by Ansonika</title>

    <!-- GOOGLE WEB FONT -->
    <link href="https://fonts.googleapis.com/css?family=Work+Sans:400,500,600" rel="stylesheet">

    <!-- BASE CSS -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link href="../css/style.css" rel="stylesheet">

    <!-- YOUR CUSTOM CSS -->
    <link href="../css/custom.css" rel="stylesheet">
    
    <script type="text/javascript">
    function delayedRedirect(){
        window.location = Flask.url_for('result', {})
    }
    </script>

</head>
<body style="background-color:#fff;" onLoad="setTimeout('delayedRedirect()', 5000)">
<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'src/Exception.php';
require 'src/PHPMailer.php';

$mail = new PHPMailer(true);

try {

    //Recipients - main edits
    $mail->setFrom('info@potenza.com', 'Message from POTENZA');                    // Email Address and Name FROM
    $mail->addAddress('jhon@potenza.com', 'Jhon Doe');                             // Email Address and Name TO - Name is optional
    $mail->addReplyTo('noreply@potenza.com', 'Message from POTENZA');              // Email Address and Name NOREPLY
    $mail->isHTML(true);                                                       
    $mail->Subject = 'Message from POTENZA Attachment';                            // Email Subject

    //The email body message
    $message  = "<strong>Presentation</strong><br />";
    $message .= "First and Last Name: " . $_POST['name'];
    $message .= "<br />Email: " . $_POST['email'];
    $message .= "<br />Telephone: " . $_POST['phone'];
    $message .= "<br />Gender: " . $_POST['gender'];                
    
    /* FILE UPLOAD */
    if(isset($_FILES['fileupload'])){
    $errors= array();
    $file_name = $_FILES['fileupload']['name'];
    $file_size =$_FILES['fileupload']['size'];
    $file_type=$_FILES['fileupload']['type'];
    $file_ext=strtolower(end(explode('.',$_FILES['fileupload']['name'])));
    $expensions= array("pdf","doc","docx");// Define with files are accepted
    $uploadfile = tempnam(sys_get_temp_dir(), hash('sha256', $_FILES['fileupload']['tmp_name']));

        if(in_array($file_ext,$expensions)=== false){
            $errors[]="Extension not allowed, please choose a .pdf, .doc, .docx file.";
        }
        // Set the files size limit. Use this tool to convert the file size param https://www.thecalculator.co/others/File-Size-Converter-69.html
        if($file_size > 153600){
            $errors[]='File size must be max 150Kb';
        }
        if(empty($errors)==true){
            move_uploaded_file($_FILES['fileupload']['name'], $uploadfile);
            $mail->AddAttachment($_FILES['fileupload']['tmp_name'], $_FILES['fileupload']['name']);
        }else{
            $message .= "<br />File name: no files uploaded";
            }
        };
    /* end FILE UPLOAD */

    $message .= "<br /><br /><strong>Work Availability</strong>";
    $message .= "<br />Are you available for work: " . $_POST['availability'];

        if (isset($_POST['minimum_salary_full_time']) && $_POST['minimum_salary_full_time'] != "")
            {
                $message .= "<br />Minimum salary: " . $_POST['minimum_salary_full_time'];
                $message .= "<br />How soon would you be looking to start? " . $_POST['start_availability_full_time'];
                $message .= "<br />Are you willing to work remotely? " . $_POST['remotely_full_time'];
            }
        if (isset($_POST['minimum_salary_part_time']) && $_POST['minimum_salary_part_time'] != "")
            {
                $message .= "<br />Minimum salary: " . $_POST['minimum_salary_part_time'];
                $message .= "<br />How soon would you be looking to start? " . $_POST['start_availability_part_time'];
                $message .= "<br />When you prefer to work? " . $_POST['day_preference_part_time'];
            }
        if (isset($_POST['fixed_rate_contract']) && $_POST['fixed_rate_contract'] != "")
            {
                $message .= "<br />Minimum fixed rate: " . $_POST['fixed_rate_contract'];
                $message .= "<br />Minimum hourly rate: " . $_POST['hourly_rate_contract'];
                $message .= "<br />Minimum hours for a contract: " . $_POST['minimum_hours_conctract'];
                $message .= "<br />Are you willing to work remotely? " . $_POST['remotely_contract'];
            }
                        
    $message .= "<br /><br />Terms and conditions accepted: " . $_POST['terms'];

    $mail->Body = "" . $message . "";

    $mail->send();

    // Confirmation/autoreplay email send to who fill the form
    $mail->ClearAddresses();
    $mail->addAddress($_POST['email']); // Email address entered on form
    $mail->isHTML(true);
    $mail->Subject    = 'Confirmation'; // Custom subject
    $mail->Body = "" . $message . "";

    $mail->Send();

    echo '<div id="success">
            <div class="icon icon--order-success svg">
                 <svg xmlns="http://www.w3.org/2000/svg" width="72px" height="72px">
                  <g fill="none" stroke="#8EC343" stroke-width="2">
                     <circle cx="36" cy="36" r="35" style="stroke-dasharray:240px, 240px; stroke-dashoffset: 480px;"></circle>
                     <path d="M17.417,37.778l9.93,9.909l25.444-25.393" style="stroke-dasharray:50px, 50px; stroke-dashoffset: 0px;"></path>
                  </g>
                 </svg>
             </div>
            <h4><span>Request successfully sent!</span>Thank you for your time</h4>
            <small>You will be redirect back in 5 seconds.</small>
        </div>';
    } catch (Exception $e) {
        echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
    }
    
?>
<!-- END SEND MAIL SCRIPT -->   

</body>
</html>