from flask import Flask, Response, request, redirect
from twilio import twiml
# import random

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def much_reply():
    resp = twiml.Response()
    inbound_message = request.form.get("Body")
    if inbound_message.lower() == "speak":
        resp.message("much talk\nsuch conversation\n\nwow")
    else:
        resp.message("bark?")
    return Response(str(resp),mimetype="application/xml"),200

if __name__ == "__main__":
    app.run(debug=True)
