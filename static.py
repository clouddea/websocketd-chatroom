from flask import *
import os
import time

app = Flask("__main__")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploadPicture", methods=["POST"])
def uploadPicture():
    id = request.form["id"]
    ct = time.localtime(time.time())
    filename = "%s%s%s%s%s%s%s%s"%(ct.tm_year, ct.tm_mon, ct.tm_mday, ct.tm_hour, ct.tm_min, ct.tm_sec, id, request.files["picture"].filename)
    request.files["picture"].save(os.path.join("uploads", filename))
    return filename;

@app.route("/uploads/<pictureName>")
def uploads(pictureName):
    with open("./uploads/%s"%(pictureName,), mode="rb") as file:
        return file.read(); 
    









app.run(host = "0.0.0.0", port = 8081)
