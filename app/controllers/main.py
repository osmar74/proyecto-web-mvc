# app/controllers/main.py
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('layout.html', content="Página inicial (antes de login)")
