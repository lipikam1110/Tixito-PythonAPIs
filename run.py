from app import create_app

app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use a different port number, e.g., 5001


# if __name__ == '__main__':
#     app.run(debug=True)
