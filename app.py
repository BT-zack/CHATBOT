from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route('/')
def chat():
    return render_template("chat.html")

@app.route('/api/message', methods=['POST'])
def api_message():
    data = request.get_json()
    user_input = data.get("message", "")
    response = get_bot_response(user_input)
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
