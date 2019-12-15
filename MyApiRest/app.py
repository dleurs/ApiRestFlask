import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Calcul ton IMC. Pour cela,\nAjoute à cette url /imc/?poids=[ton_poids_en_kg]&taille=[ta_taille_en_m]\n"

@app.route('/imc/info/', methods=['GET'])
def info():
    return (
        {
            "- de 16.5" : "famine",
            "16.5 a 18.5": "maigreur",
            "18.5 a 25" : "corpulence normale",
            "30 a 35" : "obesité moderée",
            "35 a 40" : "obesite severe", 
            "+ de 40" :  "obesité morbide ou massive",
        }
    )

@app.route('/imc/', methods=['GET'])
def imc_calculator():
    query_parameters = request.args
    poids = query_parameters.get('poids')
    taille = query_parameters.get('taille')
    imc = round(int(poids) / ((int(taille)/100)**2), 1)
    return ({"imc": str(imc)})

app.run()