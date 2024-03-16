from flask import Flask
from flask_security import Security, auth_required, roles_required, roles_accepted
from model import db
import config
from auth import user_datastore

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.security = Security(app, user_datastore)

@app.route("/")
@auth_required("token")
def home():
    return "This is a home page !!"


@app.route("/user")
@auth_required()
@roles_accepted("user", "admin")
def user():
    return "This is a user page"

if __name__ == "__main__":
    app.run(debug=True)

# 401 --> Unauthenticated
# 403 --> Forbidden
