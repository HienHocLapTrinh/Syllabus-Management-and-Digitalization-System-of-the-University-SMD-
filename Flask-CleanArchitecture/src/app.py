from flask import Flask, jsonify, redirect, url_for
# from api.routes import register_routes
from flask_admin import Admin
from flask_admin import AdminIndexView
from api.swagger import spec
from api.controllers.todo_controller import bp as todo_bp
from api.controllers.auth_controller import auth_bp as auth_bp
from infrastructure.databases import init_db
from api.middleware import middleware
from api.responses import success_response
from config import Config
from flasgger import Swagger
from config import SwaggerConfig
from flask_swagger_ui import get_swaggerui_blueprint
from api.controllers.admin_controller import admin_bp
from api.controllers.student_controller import student_bp


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        # Tạm thời cho phép tất cả (test)
        # Sau này thêm logic auth JWT: check token từ header hoặc session
        # Ví dụ: return current_user.is_authenticated (nếu dùng flask-login)
        return True

    def index(self):
        # Khi không accessible → redirect về /admin/home
        return redirect(url_for('smd_admin.admin_home'))  # 'smd_admin.admin_home' là endpoint của blueprint
    
    @property
    def name(self):
        return 'Dashboard'
    
def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.config.from_object(Config)
    
    # Đăng ký blueprint trước
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)


    # register_routes(app)
     # Thêm Swagger UI blueprint
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Syllabus Management and Digitalization System"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    try:
        init_db(app)
    except Exception as e:
        print(f"Error initializing database: {e}")

    # Register middleware
    middleware(app)

    # Register routes
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            # Thêm các endpoint khác nếu cần
            if rule.endpoint.startswith(('todo.', 'course.', 'user.', 'auth.')):
                view_func = app.view_functions[rule.endpoint]
                print(f"Adding path: {rule.rule} -> {view_func}")
                spec.path(view=view_func)
            # view_func = app.view_functions[rule.endpoint]
            # print(f"Adding path: {rule.rule} -> {view_func}")
            # spec.path(view=view_func)
    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())
    
    @app.route('/')
    def home():
        return "Welcome to SMD API. /docs for API docs, /admin for Admin Dashboard."
    return app
# Run the application

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=9999, debug=True)
