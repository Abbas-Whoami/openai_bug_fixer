from flask import Flask, render_template, request
import openai


app = Flask(__name__)

openai.api_key = ''


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.get_data(as_text=True)
    print(message)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."
        },
        {"role": "user", "content": message}
    ]
    )
    print(completion.choices[0].message)
    if completion.choices[0].message!=None:
        return completion.choices[0].message['content']

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run(debug=True)

