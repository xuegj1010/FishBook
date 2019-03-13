from flask import Blueprint

web = Blueprint('web', __package__)

from . import book
from . import user