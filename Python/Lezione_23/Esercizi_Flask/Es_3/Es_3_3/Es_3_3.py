# Mini blog

# Definire route /post/<int:id> che restituisca un articolo fittizio.

# Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.

from flask import Flask, url_for, render_template

app = Flask (__name__)

article_templates = {
    1: "Alieni.html",
    2: "Marte.html",
    3: "Killer.html"
}

@app.route('/')
def show_home() -> str:
    return f"""

        <h1> Benvenuto! </h1> <br>

        <h3> <a href="{url_for("show_posts")}"> I nostri articoli </a> </h3>

        """
@app.route('/posts')
def show_posts() -> str:

    return f"""
    
    <a href="{url_for("show_post", id = 1)}"> Alieni sulla Luna </a> <br>
    <a href="{url_for("show_post", id = 2)}"> Acqua su Marte </a> <br>
    <a href="{url_for("show_post", id = 3)}"> Serial Killer in giro per Roma </a> <br>

    """

@app.route('/post/<int:id>')
def show_post(id: int) -> str:

    template = article_templates.get(id)

    if not template:
        return "<h3> Articolo non trovato. </h3>"
    
    else:
        return render_template(template)


app.run(debug= True)