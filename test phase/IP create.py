
from flask import Flask , jsonify
app = Flask(__name__)
import subprocess

@app.route('/')
def home():
    Process=subprocess.Popen(["iwlist","wlan1","scan"],stdout=subprocess.PIPE,universal_newlines=True)
    out,err=Process.communicate()
    new_l=out.split('\n')
    arr = new_l
    return jsonify(arr)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)



