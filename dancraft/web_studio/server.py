"""
DanCraft Studio Local Web Server
실행 방법: python server.py
브라우저 접속: http://localhost:8501
"""

import http.server
import socketserver
import os
import webbrowser

PORT = 8501
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"🚀 [DanCraft Studio] 웹 스튜디오가 시작되었습니다: {url}")
        print("중지하려면 Ctrl+C를 누르십시오.")
        httpd.serve_forever()
