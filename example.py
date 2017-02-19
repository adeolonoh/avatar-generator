from avatar_generator import Avatar
from flask import Flask, make_response
app = Flask(__name__)

@app.route('/<text>.png')
def example(text):
    #avatar = Avatar.generate(500, 255, text, 'PNG')
    avatar = Avatar.generate(500, 255, text, 'PNG', (236, 238, 241), (170, 181, 194))
    headers = { 'Content-Type': 'image/png' }
    return make_response(avatar, 200, headers)

if __name__ == "__main__":
    app.run()
