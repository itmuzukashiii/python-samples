```html
C:\Users\admin>curl -X GET -v http://localhost:54321

Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:54321...
* Connected to localhost (127.0.0.1) port 54321 (#0)
> GET / HTTP/1.1
> Host: localhost:54321
> User-Agent: curl/7.83.1
> Accept: */*

* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.10.6
< Date: Wed, 16 Nov 2022 10:18:29 GMT
< Content-type: text/html; charset=utf-8
< Content-Length: 472

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="local_web_server.bat">local_web_server.bat</a></li>
<li><a href="local_web_server.py">local_web_server.py</a></li>
<li><a href="sample.html">sample.html</a></li>
</ul>
<hr>
</body>
</html>
* Closing connection 0
```
