from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def merit_calculator():
    resultado = None
    color = "black"  # Color predeterminado
    if request.method == "POST":
        try:
            formacion = float(request.form["formacion"])
            experiencia = float(request.form["experiencia"])
            idiomas = float(request.form["idiomas"])
            informatica = float(request.form["informatica"])
            total = formacion + experiencia + idiomas + informatica

            if total < 50:
                color = "red"
            elif 50 <= total < 80:
                color = "black"
            else:
                color = "green"

            resultado = f"Puntuación Total: {total}"
        except ValueError:
            resultado = "Por favor, ingrese valores numéricos válidos."

    return render_template("index.html", resultado=resultado, color=color)

if __name__ == "__main__":
    app.run(debug=True)
