from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
# Replace 'your_database_name' with your actual database name
db = client['tripdb']
# Replace 'users' with your actual collection name
users_collection = db['users']


@app.route('/add_review', methods=['POST'])
def add_review():
    print("Executing")
    data = request.form

    # Extract data from the request payload
    username = data.get('username')
    place_name = data.get('placeName')
    review = data.get('review')
    rating = data.get('rating')

    print(rating)

    # Find the user document
    user = users_collection.find_one({'username': username})

    if user:
        trips = user.get('trips', [])


        # Check if the place already exists in the user's trips
        if place_name in trips:
            

            # If the place exists, update the review
            users_collection.update_one(
                {'username': username, 'trips': place_name},
                {'$push': {'reviews': {'name': place_name,
                                       'review': review, 'rating': rating}}}
            )
            return jsonify({'message': f'Review added for {place_name}.'}), 200
        else:
            # If the place does not exist, add a new trip and review
            users_collection.update_one(
                {'username': username},
                {'$push': {'trips': place_name, 'reviews': {
                    'review': review, 'rating': rating}}}
            )
            return jsonify({'message': f'New trip {place_name} added with review.'}), 200
    else:
        return jsonify({'error': 'User not found.'}), 404


@app.route('/')
def index():
    return render_template("add_review.html")


@app.route('/index1')
def index1():
    return render_template("index1.html")


if __name__ == '__main__':
    app.run(debug=True)
