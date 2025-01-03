#test for git tracking

from flask import Flask, jsonify, request

app = Flask(__name__)

#Initial data
items = [
    {"id":1, "name":"Item 1", "description":"This is Item 1"},
    {"id":2, "name":"Item 2", "description":"This is Item 2"}
]

@app.route("/")
def home():
    return "Welcome to to do list home page"

#Get:Retreieve all items
@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items) 

#Get:Retreive specific item by id
@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item)

#Post : create new task - API
@app.route("/items", methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

#put:update an existing item
@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    item["name"] = request.json.get('name', item["name"])
    item["description"] = request.json.get('description', item["description"])
    return jsonify(item)

#Delete: Delete an item
@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result" : "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)



