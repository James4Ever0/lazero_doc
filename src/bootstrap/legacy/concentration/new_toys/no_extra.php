<?php
//curl的百度百科
//$url = 'http://www.baidu.com/link?url=77I2GJqjJ4zBBpC8yDF8xDhiqDSn1JZjFWsHhEoSNd85PkV8Xil-rckpQ8_kjGKNNq';
$fh = fopen('php://stdin', 'r'); 
//echo "[php://stdin]请输入任意字符：\n"; 
$url = trim(fread($fh, 1000));   
// get input 
#echo $url;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
// 不需要页面内容
curl_setopt($ch, CURLOPT_NOBODY, 1);
// 不直接输出
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
// 返回最后的Location
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_exec($ch);
$info = curl_getinfo($ch,CURLINFO_EFFECTIVE_URL);
curl_close($ch);
echo $info;
?>
