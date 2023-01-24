from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/books')
def list_of_books():
    books = [
        {'name': 'The Call of the Wild', 'author': 'Jack London'},
        {'name': 'Heart of Darkness', 'author': 'Joseph Conrad'}
    ]
    return jsonify(books)

if __name__ == '__main__':
    app.run()