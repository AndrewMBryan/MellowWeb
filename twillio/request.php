<?php
header('Content-type: text/xml');
?>
<Response>
    <Dial callerId="+14049961894"><?php  echo $_POST['To'];?></Dial>
</Response>