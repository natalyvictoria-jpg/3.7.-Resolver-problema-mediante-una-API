from flask import Blueprint, jsonify, request
from app import db
from app.models import Estudiante

estudiantes_bp = Blueprint("estudiantes", __name__, url_prefix="/api")


@estudiantes_bp.route("/estudiantes", methods=["POST"])
def crear_estudiante():
    """
    Registrar un nuevo estudiante
    ---
    tags:
      - Estudiantes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            nombre:
              type: string
              example: "Ana Garcia"
            carrera:
              type: string
              example: "ITIC"
            semestre:
              type: integer
              example: 5
    responses:
      201:
        description: Estudiante registrado exitosamente
      400:
        description: Datos incorrectos o faltantes
    """
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    for campo in ["nombre", "carrera", "semestre"]:
        if campo not in datos:
            return jsonify({"error": f"El campo '{campo}' es requerido"}), 400

    nuevo = Estudiante(
        nombre=datos["nombre"],
        carrera=datos["carrera"],
        semestre=datos["semestre"]
    )
    db.session.add(nuevo)
    db.session.commit()

    return jsonify({
        "mensaje": "Estudiante registrado exitosamente",
        "estudiante": nuevo.to_dict()
    }), 201


@estudiantes_bp.route("/estudiantes", methods=["GET"])
def obtener_estudiantes():
    """
    Obtener todos los estudiantes
    ---
    tags:
      - Estudiantes
    parameters:
      - in: query
        name: carrera
        type: string
        description: Filtrar por carrera
      - in: query
        name: nombre
        type: string
        description: Buscar por nombre
      - in: query
        name: semestre
        type: integer
        description: Filtrar por semestre
    responses:
      200:
        description: Lista de estudiantes
    """
    carrera = request.args.get("carrera")
    nombre  = request.args.get("nombre")
    semestre = request.args.get("semestre")

    query = Estudiante.query

    if carrera:
        query = query.filter(Estudiante.carrera.ilike(f"%{carrera}%"))
    if nombre:
        query = query.filter(Estudiante.nombre.ilike(f"%{nombre}%"))
    if semestre:
        query = query.filter(Estudiante.semestre == int(semestre))

    estudiantes = query.all()

    return jsonify({
        "total": len(estudiantes),
        "estudiantes": [e.to_dict() for e in estudiantes]
    }), 200


@estudiantes_bp.route("/estudiantes/<int:id>", methods=["GET"])
def obtener_estudiante(id):
    """
    Obtener un estudiante por ID
    ---
    tags:
      - Estudiantes
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Datos del estudiante
      404:
        description: Estudiante no encontrado
    """
    estudiante = Estudiante.query.get_or_404(id)
    return jsonify(estudiante.to_dict()), 200


@estudiantes_bp.route("/estudiantes/<int:id>", methods=["PUT"])
def actualizar_estudiante(id):
    """
    Actualizar un estudiante existente
    ---
    tags:
      - Estudiantes
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          properties:
            nombre:
              type: string
              example: "Ana Garcia Lopez"
            carrera:
              type: string
              example: "ITIC"
            semestre:
              type: integer
              example: 6
    responses:
      200:
        description: Estudiante actualizado
      404:
        description: Estudiante no encontrado
    """
    estudiante = Estudiante.query.get_or_404(id)
    datos = request.get_json()

    if "nombre" in datos:
        estudiante.nombre = datos["nombre"]
    if "carrera" in datos:
        estudiante.carrera = datos["carrera"]
    if "semestre" in datos:
        estudiante.semestre = datos["semestre"]

    db.session.commit()

    return jsonify({
        "mensaje": "Estudiante actualizado exitosamente",
        "estudiante": estudiante.to_dict()
    }), 200


@estudiantes_bp.route("/estudiantes/<int:id>", methods=["DELETE"])
def eliminar_estudiante(id):
    """
    Eliminar un estudiante
    ---
    tags:
      - Estudiantes
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Estudiante eliminado
      404:
        description: Estudiante no encontrado
    """
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()

    return jsonify({
        "mensaje": f"Estudiante {estudiante.nombre} eliminado exitosamente"
    }), 200