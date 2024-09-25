from flask import Flask, jsonify, request
from data_dict_simple import simple
from flask_cors import CORS
from students import read, update_github_username, fetch_github_repos, all_students, delete_student_by_id

app = Flask(__name__)
CORS(app)




# GET
@app.route('/students')
def read_all():
    students = read() # Kaldes for at hente en liste af alle studerende fra databasen
    if students:
        return jsonify(students), 200 # OK.     Returneres som JSON
    else:
        return jsonify({"error": "No students found"}), 404 # NOT FOUND 




# POST
@app.route('/students', methods=['POST'])
def create():
    data = request.get_json() # Bruges til at hente JSON-data fra body

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400 # Bad request
    
    simple.append(data)
    return jsonify(simple), 201 # Created



# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    result, status_code = delete_student_by_id(id) # Sletter en student ud fra id

    if status_code == 200:
        return jsonify(result), 200 # Ok
    else:
        return jsonify(result), 404 # Not found




# PUT
@app.route('/students/<int:id>', methods=['PUT'])
def update_github_username_route(id):
    data = request.get_json()

    if not data or 'github_username' not in data:
        return jsonify({"error": "No github_username provided"}), 400 # Bad request
    
    github_username = data.get("github_username")

    result, status_code = update_github_username(id, github_username)

    if status_code == 200:
        return jsonify({"message": "GitHub username updated succesfully"}), 200 #Ok
    else:
        return jsonify({"error": "Student not found"}), 404 #Not found





# GET REPO
@app.route('/students/repos', methods =['GET'])
def get_students_repo():
    students = all_students()

    students_with_repos = []

    for student in students:
        student_id, first_name, last_name, github_username = student


        if github_username:
            repos = fetch_github_repos(github_username)
        
        else:
            repos = []

        students_with_repos.append({
            "id": student_id,
            "name": f"{first_name}, {last_name}",
            "github_username": github_username,
            "repositories": repos
        })

    return jsonify(students_with_repos)







if __name__ == '__main__':
    app.run(debug=True)