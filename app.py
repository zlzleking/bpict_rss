import bpict_reader
import rss_server

import time
import threading
from flask import Flask
from flask import Response

end = False
bpict_response={}
bpict_data={}
bpict_rss=[]
time_pre=0

def bpict_update():
    global bpict_response 
    global bpict_data 
    global bpict_rss
    global time_pre
    
    time_now=time.time()
    if time_now >= time_pre + 120:
        bpict_response = bpict_reader.bpict_readnphase.bpict_read()
        bpict_data = bpict_reader.bpict_readnphase.bpict_phase(bpict_response)
        bpict_rss = rss_server.rssize(bpict_data)
        print("Data updated.")
        time_pre=time_now

app = Flask(__name__)
@app.route('/')
def main():
    bpict_update()
    return Response(bpict_rss, mimetype='text/xml')
host_addr = "0.0.0.0"
port_num = "8080"
if __name__ == "__main__":              
    app.run(host=host_addr, port=port_num)