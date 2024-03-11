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