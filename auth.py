import random
import string
import secrets

#flask app goes here
app = Flask(__name__)

@app.route("/")
def hello_world():
    message = "Welcome you to this Authentication API \ncreated using Flask library\n# Main-Menu : \n/generatekey : to generate a key \n/generatehashkey : to generate the hashkey"
    return message

@app.route("/generatekey/")
def generateKey():
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(8)))
    return result_str

@app.route("/generatehashkey/")
def generateHashkey():
    hashkey = secrets.token_hex(32)
    return hashkey


if __name__=="__main__":
    app.run(debug=True)