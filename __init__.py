from flask import Flask, render_template, request, redirect, jsonify, json
import sqlite3

app = Flask(__name__)  # Création de l'application Flask

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

@app.route('/post/<int:post_id>')
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM livres WHERE id = ?', (post_id,)).fetchone()
    conn.close()

    # Si la publication avec l'ID spécifié n'est pas trouvée, renvoie une réponse 404 Not Found
    if post is None:
        return jsonify(error='Post not found'), 404

    # Convertit la publication en un format JSON
    json_post = {'id': post['id'], 'title': post['title'], 'auteur': post['auteur']}
    
    # Renvoie la réponse JSON
    return jsonify(post=json_post)


if __name__ == "__main__":
    app.run(debug=True)  # Ajout de `debug=True` pour faciliter le débogage

