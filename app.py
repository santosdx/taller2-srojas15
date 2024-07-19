from flask import Flask
from flask_restful import Api
from models.gato import Gato
from models.perro import Perro
from models.boa_constrictor import BoaConstrictor
from models.huron import Huron
from controllers.animal_controller import AnimalController

app = Flask(__name__)
api = Api(app)


@app.route("/animal/gato")
def gato():
    el_gato = Gato("Artemis", 1, 4)
    print('EL gato "{0}" hace {1}'.format(el_gato.get_nombre(), el_gato.hacer_sonido()))
    return el_gato.hacer_sonido()


@app.route("/animal/perro")
def perro():
    el_perro = Perro("Chocolate", 1, 4)
    print('EL perro "{0}" hace {1}'.format(el_perro.get_nombre(), el_perro.hacer_sonido()))
    return el_perro.hacer_sonido()


@app.route("/animal/huron")
def huron():
    el_huron = Huron("Tomas", 1.5, 4, "Australia", 2.5)
    print('El huron "{0}" hace {1}'.format(el_huron.get_nombre(), el_huron.hacer_sonido()))
    return el_huron.hacer_sonido()


@app.route("/animal/boa")
def boa():
    la_boa = BoaConstrictor("Resbalosa", 2, 8, "Brasil", 10)
    print('La boa "{0}" hace {1}'.format(la_boa.get_nombre(), la_boa.hacer_sonido()))
    return la_boa.hacer_sonido()


api.add_resource(AnimalController, '/animal')
