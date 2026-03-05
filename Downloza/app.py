from flask import send_from_directory

@app.route('/sw.js')
def monetag_sw():
    return send_from_directory('static', 'sw.js')
