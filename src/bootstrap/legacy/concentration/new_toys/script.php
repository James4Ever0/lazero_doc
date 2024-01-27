<?php

	$url = 'http://www.baidu.com/link?url=77I2GJqjJ4zBBpC8yDF8xDhiqDSn1JZjFWsHhEoSNd85PkV8Xil-rckpQ8_kjGKNNq';
	$header = get_headers($url,1);
	if (strpos($header[0],'301') || strpos($header[0],'302')) {
	    if(is_array($header['Location'])) {
	        $info = $header['Location'][count($header['Location'])-1];
	    }else{
	        $info = $header['Location'];
	    }
	}
	echo $info;
// this is slow.
?>
