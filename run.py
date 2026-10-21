from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True faz o servidor reiniciar automaticamente ao salvar edições de código
    app.run(debug=True, port=5000)