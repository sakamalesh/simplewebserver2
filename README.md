# Developing a Simple Webserver
## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation
### Step 2:
Design of webserver workflow
### Step 3:
Implementation using Python code
### Step 4:
Serving the HTML pages.
### Step 5:
Testing the webserver

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<HTML>
    <head>
        
    </head>
    <body
        bgcolor="pink">
        <font color="black"  size="75" >
        <center><h1>HOMIES OF SEC</h1></center>
        <table bgcolor="red"
        border="20" 
        align="center">
            <tr
            bgcolor="white"
            cellspace="10">
                <th>NAME</th>
                <TH>DEPT</TH>
                <TH>AGE</TH>
            </tr>
            <TR  bgcolor="white"
            cellspace="10">
                <TD> KAMALESH</TD>
                <TD> CSE</TD>
                <TD>17 </TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> KIRAN</TD>
                <TD> CSE</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> ROHIT</TD>
                <TD> CSE</TD>
                <TD>19</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> PRADEEP</TD>
                <TD> IT</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD>SUBBIAH</TD>
                <TD> IT</TD>
                <TD>17</TD>
            </TR>
            <TR bgcolor="WHITE"
            cellspace="10" >
                <TD> JABEZ</TD>
                <TD> CSE</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD>DEVA SANJAY</TD>
                <TD> CSE</TD>
                <TD>17</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> KAVIYA</TD>
                <TD> CSE</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> RAKSHITHA</TD>
                <TD> IT</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
             cellspace="10">
                <TD> DAISY</TD>
                <TD> IT</TD>
                <TD>18 </TD>
            </TR>
        </table>
    </body>
</HTML>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```


## OUTPUT:

![Screenshot 2024-03-11 190612](https://github.com/sakamalesh/simplewebserver2/assets/149148235/b4c39671-36d5-4a31-a2bb-1e73db8063f5)

![Screenshot 2024-03-11 190635](https://github.com/sakamalesh/simplewebserver2/assets/149148235/6ab8f2be-a17d-4968-b870-41d0f5c3007b)

## RESULT:
Success
