from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# In-memory data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

posts = [
    {"id": 1, "title": "Old Post"},
    {"id": 2, "title": "Another Post"}
]

@app.route('/', methods=['GET'])
def get_health():
    return make_response(jsonify({"Status": "OK"}), 200)

@app.route('/users', methods=['GET'])
def get_users():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return make_response(jsonify({"error": "Unauthorized"}), 401)
    return jsonify(users), 200

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'title' not in data:
        return make_response(jsonify({"error": "Bad Request"}), 400)
    post = {
        "id": len(posts) + 1,
        "title": data['title']
    }
    posts.append(post)
    return jsonify(post), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user.update(data)
            return jsonify(user), 200
    return make_response(jsonify({"error": "User not found"}), 404)

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
