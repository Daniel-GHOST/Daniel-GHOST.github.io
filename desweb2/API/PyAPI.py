from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tareas de ejemplo
tasks = [
    {"id": 1, "title": "Comprar leche", "done": False},
    {"id": 2, "title": "Llamar al médico", "done": False},
]

# Ruta para obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Ruta para obtener una tarea por su ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify({"task": task})

# Ruta para crear una nueva tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if "title" not in data:
        return jsonify({"error": "El campo 'title' es obligatorio"}), 400

    new_id = max(task["id"] for task in tasks) + 1
    new_task = {"id": new_id, "title": data["title"], "done": False}
    tasks.append(new_task)
    return jsonify({"message": "Tarea creada exitosamente", "task": new_task}), 201

# Ruta para actualizar una tarea por su ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json()
    if "title" in data:
        task["title"] = data["title"]
    if "done" in data:
        task["done"] = data["done"]
    
    return jsonify({"message": "Tarea actualizada exitosamente", "task": task})

# Ruta para eliminar una tarea por su ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarea eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
