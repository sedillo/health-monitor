from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/reprovision', methods=['POST'])
def reprovision():
    # Trigger Ansible playbook
    subprocess.run(["ansible-playbook", "-i", "production", "/app/reprovision.yml"])
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

