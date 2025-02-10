from flask import render_template, request, redirect, url_for
from ai.code_solver import solve_code_problem
from ai.design_to_code import design_to_code

def configure_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/solve", methods=["POST"])
    def solve():
        problem = request.form.get("problem")
        solution = solve_code_problem(problem)
        return render_template("result.html", solution = solution)
    
    @app.route("/generate", methods=["POST"])
    def generate():
        image = request.files.get("image")
        code = design_to_code(image)
        return render_template("result.html", solution= code)