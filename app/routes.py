from flask import Blueprint, render_template
from .rbac.decorators import require_role
from flask_login import login_required, current_user

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def home():
    return "<h1>Welcome to Smart city portal</h1>"  

@core_bp.route('/admin-panel')
@require_role('admin')
def admin_panel():
    return "Welcome, Admin!"

@core_bp.route('/dashboard')
@login_required
def dashboard():
    print("🎯 Current user:", current_user)
    return f"You're logged in as {current_user.email} 🎉"