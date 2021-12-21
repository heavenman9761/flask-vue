from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
import uuid

Books = Namespace('Books')

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@Books.route('/')
class all_Books(Resource):
    def get(self):
        response_object = {'status': 'success'}
        response_object['books'] = BOOKS
        return jsonify(response_object)

@Books.route('/addBook')
class add_book(Resource):
    def post(self):
        response_object = {'status': 'success'}
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'        
        return jsonify(response_object)

@Books.route('/<book_id>')
class get_book(Resource):
    def put(self, book_id):
        response_object = {'success': 'success'}
        post_data = request.get_json()
        self.remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
        return jsonify(response_object)

    def delete(self, book_id):
        response_object = {'success': 'success'}
        self.remove_book(book_id)

        response_object['message'] = 'Book removed!'
        return jsonify(response_object)

    def remove_book(self, book_id):
        for book in BOOKS:
            if book['id'] == book_id:
                BOOKS.remove(book)
                return True
        return False