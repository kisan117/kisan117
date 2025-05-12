from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Facebook Token Checker</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            min-height: 100vh;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(120deg, #43cea2 0%, #185a9d 100%);
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: rgba(255,255,255,0.15);
            box-shadow: 0 8px 32px 0 rgba(31,38,135,0.37);
            border-radius: 16px;
            padding: 40px 30px 30px 30px;
            text-align: center;
            backdrop-filter: blur(6px);
            min-width: 320px;
        }
        h2 {
            color: #185a9d;
            margin-bottom: 25px;
            letter-spacing: 1px;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }
        input[type="text"] {
            width: 90%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #b5b5b5;
            font-size: 16px;
            outline: none;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 0;
            width: 60%;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
            margin-top: 10px;
        }
        input[type="submit"]:hover {
            background: linear-gradient(90deg, #185a9d 0%, #43cea2 100%);
        }
        .result {
            margin-top: 25px;
            background: rgba(255,255,255,0.25);
            border-radius: 10px;
            padding: 15px;
            color: #185a9d;
            font-size: 17px;
        }
        .error {
            margin-top: 25px;
            background: #ffdddd;
            border-radius: 10px;
            padding: 15px;
            color: #b00020;
            font-size: 17px;
        }
        a {
            color: #185a9d;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        @media (max-width: 500px) {
            .card {
                padding: 25px 10px 15px 10px;
                min-width: 90vw;
            }
            input[type="submit"] {
                width: 90%;
            }
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Facebook Token Checker</h2>
        <form method="post">
            <input type="text" name="token" placeholder="Enter Facebook Token" required>
            <input type="submit" value="Check Token">
        </form>
        {% if uid %}
            <div class="result">
                <p><b>UID:</b> {{ uid }}</p>
                <p><b>FB Link:</b> <a href="https://facebook.com/{{ uid }}" target="_blank">facebook.com/{{ uid }}</a></p>
            </div>
        {% elif error %}
            <div class="error">
                {{ error }}
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    uid = None
    error = None
    if request.method == 'POST':
        token = request.form.get('token')
        url = f'https://graph.facebook.com/me?fields=id&access_token={token}'
        try:
            resp = requests.get(url)
            data = resp.json()
            if 'id' in data:
                uid = data['id']
            else:
                error = data.get('error', {}).get('message', 'Invalid token')
        except Exception as e:
            error = str(e)
    return render_template_string(HTML_PAGE, uid=uid, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
