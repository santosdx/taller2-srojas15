from flask import render_template, make_response, request, redirect
from flask_restful import Resource


class AnimalController(Resource):

    def get(self):
        return make_response(render_template("animal.html"))

    def post(self):
        recurso = request.form['animal']
        animales = ["gato", "perro", "huron", "boa"]
        for animal in animales:
            if animal.strip().lower() == recurso.strip().lower():
                print("Animal:", recurso)
                url = "/animal/" + recurso
                return redirect(url)
        return redirect('animal')
