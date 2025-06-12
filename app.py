from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", "")
    service_code = request.values.get("serviceCode", "")
    phone_number = request.values.get("phoneNumber", "")
    text = request.values.get("text", "")

    user_response = text.split("*")

    if text == "":
        response = "CON Welcome! You may qualify for up to KES 40,000.\n1. Continue"
    elif text == "1":
        response = "CON Please enter your ID number:"
    elif len(user_response) == 2 and user_response[0] == "1":
        id_number = user_response[1]
        response = "END Thank you! You qualify for KES 7,870."
    else:
        response = "END Invalid input. Please try again."

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
