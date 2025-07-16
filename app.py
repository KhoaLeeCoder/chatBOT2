from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"  # <-- thay bằng key của bạn
MODEL = "mistralai/mistral-7b-instruct"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    messages = [
        {"role": "system", "content": "Tôi là một chatbot thân thiện."},
        {"role": "user", "content": user_msg}
    ]
    try:
        response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages
    )
        reply = response["choices"][0]["message"]["content"]
    except Exception as e:
     print("lỗi gọi API:", e)
     reply = "Bot gặp lỗi khi xử lý yêu cầu của bạn. Vui lòng thử lại sau."


    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)