from flask import Blueprint, render_template
from .rbac.decorators import require_role

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def home():
    return "<h1>Welcome to Smart city portal</h1>"  

@core_bp.route('/admin-panel')
@require_role('admin')
def admin_panel():
    return "Welcome, Admin!"