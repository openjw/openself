from flask import Blueprint

controller = Blueprint('ADMIN_CONTROLLER', __name__)

@controller.route('/')
def index():
    return 'Hello, Admin!'