from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🦋<span class="devil">MR DEVIL TOKEN CHAKER</span>🦋</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
        body {
            min-height: 100vh;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            background: url('https://i.ibb.co/MDZC7WzV/057c0a4c922c6f98b8d9715bb537ab83.jpg') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
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
            color: #fff;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }
        .devil {
            background: linear-gradient(90deg, #ff00cc, #3333ff, #00ffcc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            font-size: 1.15em;
            letter-spacing: 1px;
        }
        .subtitle {
            font-size: 15px;
            color: #fff;
            margin-bottom: 25px;
        }
        .social-icons {
            margin-top: 7px;
        }
        .social-icons a {
            display: inline-block;
            margin: 0 10px;
            font-size: 24px;
            vertical-align: middle;
            transition: transform 0.2s;
        }
        .social-icons a:hover {
            transform: scale(1.2);
        }
        .fa-whatsapp {
            color: #25D366;
        }
        .fa-facebook {
            color: #1877f3;
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
            color: #fff;
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
            color: #fff;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .footer {
            margin-top: 25px;
            font-size: 14px;
            color: #fff;
            text-align: center;
        }
        .footer .devil {
            font-size: 1em;
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
        <h2>🦋<span class="devil">MR DEVIL TOKEN CHAKER</span>🦋</h2>
        <div class="subtitle">
            FOR ANY KIND HELP CONTACT <br>
            <span class="social-icons">
                <a href="https://wa.me/919024870456" target="_blank" title="WhatsApp">
                    <i class="fab fa-whatsapp"></i>
                </a>
                <a href="https://www.facebook.com/share/195iPt5waG/MR DEVIL" target="_blank" title="Facebook">
                    <i class="fab fa-facebook"></i>
                </a>
            </span>
        </div>
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
    <div class="footer">
        This tool presenting by <span class="devil">MR DEVIL SHARBI</span> © 2025
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
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
