import os
import time
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

# set the maximum number of attempts before blocking IP
MAX_ATTEMPTS = 3

# create a dictionary to store IP addresses and their attempts
ip_attempts = {}

# create a list to store blocked IPs
blocked_ips = []

# create a dictionary to store login/logout times
login_times = {}

# create a list to store logs
logs = []

# define the route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    # check if user is already logged in
    if 'logged_in' in request.cookies:
        return redirect(url_for('dashboard'))

    # check if user has entered the correct password
    if request.method == 'POST' and request.form['password'] == 'Tommylong12':
        # set the logged_in cookie for 24 hours
        resp = redirect(url_for('dashboard'))
        resp.set_cookie('logged_in', 'true', max_age=86400)
        return resp

    # increment the number of attempts for this IP address
    ip = request.remote_addr
    if ip in ip_attempts:
        ip_attempts[ip] += 1
    else:
        ip_attempts[ip] = 1

    # if the maximum number of attempts has been reached, block the IP
    if ip_attempts[ip] >= MAX_ATTEMPTS:
        blocked_ips.append(ip)
        ip_attempts[ip] = 0
        logs.append(f'{datetime.now()}: IP address {ip} has been blocked after {MAX_ATTEMPTS} failed attempts')

    return render_template('login.html')

# define the route for the dashboard page
@app.route('/dashboard')
def dashboard():
    # check if user is logged in
    if 'logged_in' not in request.cookies:
        return redirect(url_for('login'))

    # get the current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # get the IP address of the user
    ip = request.remote_addr

    # check if the user's IP is blocked
    if ip in blocked_ips:
        return render_template('blocked.html')

    # add the login time to the dictionary
    login_times[ip] = now

    return render_template('dashboard.html', ip=ip, login_time=login_times[ip], logs=logs) #return back the HTML

# define the route for logging out
@app.route('/logout')
def logout():
    # remove the logged_in cookie
    resp = redirect(url_for('login'))
    resp.delete_cookie('logged_in')
    ip = request.remote_addr
    logs.append(f'{datetime.now()}: IP address {ip} has logged out')
    return resp

# define the route for manually blocking IPs
@app.route('/block_ip', methods=['GET', 'POST'])
def block_ip():
    # check if user is logged in
    if 'logged_in' not in request.cookies:
        return redirect(url_for('login'))

    # check if user has submitted a form
    if request.method == 'POST':
        # get the password and IP address submitted by the user
        password = request.form['password']
        ip = request.form['ip']

        # check if the password is correct
        if password != 'TommyLong12@':
            return render_template('block_ip.html', message='Invalid password')

        # block the IP address
        blocked_ips.append(ip)
        logs.append(f'{datetime.now()}: IP address {ip} has been manually blocked by admin')

        return redirect(url_for('dashboard'))

    return render_template('block_ip.html')
        
# a code to check if the password is correct, if not add the ip to the list of blocked IP
app.run(host='127.0.0.1', port=8080, debug=True)