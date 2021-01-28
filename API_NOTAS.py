from flask import Flask, Request


app = Flask("EscolaAlf")


# página onde os professores podem cadastrar os gabaritos das provas.
@app.route("/gabarito", methods=["POST"])
def cadastrogabarito():
    return {"id": "0"}


app.run(port=6000)
