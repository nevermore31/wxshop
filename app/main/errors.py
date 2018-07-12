from . import main_Blueprint

@main_Blueprint.app_errorhandler(404)
def error(e):
    return 'Error',404
