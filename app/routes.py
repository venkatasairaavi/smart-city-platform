from flask import Blueprint, render_template

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def home():
    return "<h1>Welcome to Smart city portal</h1>"  