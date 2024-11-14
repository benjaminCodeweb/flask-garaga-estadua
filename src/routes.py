from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from typing import List, Tuple, Dict, Any
from . import db
from .models import Auto
from .schemas import AutoCreateSchema
from flask_sqlalchemy import  query
from time import time

auto_bp = Blueprint('auto_bp', __name__)

@auto_bp.route("/")
def index() -> str:
    autos : list[tuple[Any]] = Auto.query.all()

    return render_template('index.html', autos=autos)
 
@auto_bp.route('/autos/new')
def nueva_Estadia_form() -> str:
    return render_template('auto_form.html')

@auto_bp.route('/autos', methods=['POST'])
def crear_Estadia() -> str:
    data = request.form
    cant_horas = None
    tiempo_segundos = 0 
    
    
    try:
    
        nueva_estadia = Auto(
            modelo=data['modelo'],
            patente=data['patente'],
            cant_horas=data['cant_horas'],
            image_url=str(data['image_url']),
        )

      
        if 'cant_horas' in data and data['cant_horas']:
            try:
                # Convierte 'cant_horas' a un entero
                cant_horas = int(data['cant_horas'])
                tiempo_segundos = cant_horas * 3600  # Convierte horas a segundos
            except ValueError:
                return "Por favor, ingresa un número válido para Cant horas."

        db.session.add(nueva_estadia)
        db.session.commit()

        return render_template('auto_item.html', auto=nueva_estadia, tiempo=tiempo_segundos)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400



@auto_bp.route('/autos/<int:auto_id>/edit')
def edit_estadia(auto_id: int) -> str:
    auto: Auto  = Auto.query.get_or_404(auto_id)
    return render_template('auto_item.html', auto = auto)

@auto_bp.route('/autos/<int:auto_id>', methods = ['DELETE'])
def eliminar_estadia(auto_id: int) -> str:
    auto: Auto = Auto.query.get_or_404(auto_id)
    db.session.delete(auto)
    db.session.commit()

    autos: list[tuple[Any]] = Auto.query.all()

    return render_template('index.html', autos= autos)
