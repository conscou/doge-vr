from flask import Flask, Response, request, redirect
from twilio import twiml
import random

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def much_reply():
    resp = twiml.Response()
    inbound_message = request.form.get("Body")
    messages = ["much talk\nsuch conversation\n\nwow", \
            "much chat\nsuch small talk\n\n wow", \
            "such text\nvery sms\n\nmuch twilio",\
            "much hack\nwow\n\nsuch prime",\
            "such unity3d\nmuch blender\n\nsuch cardboard\n",\
            "wow\nsuch compliment\n\nmuch bashful"]
    if inbound_message.lower() == "speak":
        resp.message(random.choice(messages))
    elif inbound_message.lower() == "roll over":
        resp.message("no")
    else:
        resp.message("bark?")
    return Response(str(resp),mimetype="application/xml"),200

if __name__ == "__main__":
    app.run(debug=True)
