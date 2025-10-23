from flask import Flask, jsonify
import os
from wakeonlan import send_magic_packet

app = Flask(__name__)

CONFIG = {
    "PC-Janios": {
        "mac": "10:ff:e0:b1:75:ba",
        "broadcast": "192.168.3.255"
    }
}

@app.route("/wake/<name>")
def wake(name):
    if name not in CONFIG:
        return jsonify({"error": "Device not found"}), 404
    mac = CONFIG[name]["mac"]
    broadcast = CONFIG[name]["broadcast"]
    send_magic_packet(mac, ip_address=broadcast)
    return jsonify({"success": True, "device": name, "mac": mac, "broadcast": broadcast})

@app.route("/")
def index():
    return jsonify({"devices": list(CONFIG.keys())})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
