from project.factory import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=9000)
