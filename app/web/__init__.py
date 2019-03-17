from flask import Blueprint

web = Blueprint('web', __name__)

from . import book
from . import auth
from . import drift
from . import gift
from . import main
from . import wish
