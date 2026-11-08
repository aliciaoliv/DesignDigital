def configurar_rotas(app):
    @app.route('/')
    def index():
        return "Aplicação Flask rodando pronta para o EC2"