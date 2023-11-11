
from flask import flash, request
import sys
from flask import Flask, jsonify, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from extensions import db
from resources.user import UserListResource
from resources.crime import CrimeListResource, CrimeResouces
from resources.cell import CellListResource, CellResouces
from resources.prisoner  import PrisonerListResource , PrisonerResouces
from resources.prisonercrime import PrisonerCrimeListResource ,PrisonerCrimeResouces



def create_app():
    print("Hello", file=sys.stderr)
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    routes(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(CrimeListResource, '/crime')
    api.add_resource(CrimeResouces, '/crime/<int:crime_id>')
    api.add_resource(CellListResource, '/cell')
    api.add_resource(CellResouces, '/cell/<int:cell_id>')
    api.add_resource(PrisonerListResource, '/prisoner')
    api.add_resource(PrisonerResouces, '/prisoner/<int:prisoner_id>')
    api.add_resource(PrisonerCrimeListResource, '/pcrimes')
    api.add_resource(PrisonerCrimeResouces, '/pcrimes/<int:pcrime_id>')

def routes(app):
    @app.route('/')
    def index():
        prisoners_data = PrisonerListResource.get(self=None)
        return render_template('index.html',prison=prisoners_data[0]['data'])
    @app.route('/all-crimes')
    def crimes():
        crimes_data = CrimeListResource.get(self=None)
        return render_template('crimes.html',crimes=crimes_data[0]['data'])
    @app.route('/all-cells')
    def cells():
        cells_data = CellListResource.get(self=None)
        return render_template('cells.html',cells=cells_data[0]['data'])
    @app.route('/prisoner-crimes')
    def prcrimes():
        n = PrisonerCrimeListResource
        pcrimes = n.get(self=None)
        return render_template('prisoner_crimes.html',pcrimes=pcrimes[0]['data'])
#     @app.route('/edit/<int:prisoner_id>')
#     def edit(prisoner_id):
#         prisoner_resource_instance = PrisonerResouces()
#         prisoner_data = prisoner_resource_instance.get(prisoner_id)
#         #prisoners_data = PrisonerResouces.get(None,prisoner_id)
#         if prisoner_data is None:
#             return {"messaige":"Prisoner not found "}
#         return prisoner_data
#     @app.route('/delete/<int:prisoner_id>')
#     def delete(prisoner_id):
#         prisoner_resource_instance = PrisonerResouces()
#         result = prisoner_resource_instance.get(prisoner_id)
#         body , status = result
#         if status != 200:
#             return result
#         res = prisoner_resource_instance.delete(prisoner_id)
#         return redirect(url_for('index',message='Data deleted successfully!'))


        




if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
