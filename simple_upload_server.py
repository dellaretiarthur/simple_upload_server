from flask import Flask, request, redirect, url_for, flash, render_template_string

app = Flask(__name__)
app.secret_key = "super secret key"  # Necessário para mensagens flash

# Página HTML para o upload de arquivos
HTML = """
<!doctype html>
<title>Upload de Arquivos</title>
<h2>Upload de Arquivos</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
"""


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Verifica se o post tem o arquivo parte
        if "file" not in request.files:
            flash("Nenhum arquivo parte")
            return redirect(request.url)
        file = request.files["file"]
        # Se o usuário não selecionar um arquivo, o navegador
        # submeterá um arquivo vazio sem um nome de arquivo.
        if file.filename == "":
            flash("Nenhum arquivo selecionado para upload")
            return redirect(request.url)
        if file:
            # Aqui você pode salvar o arquivo em algum lugar
            file.save(f"./uploads/{file.filename}")
            flash("Arquivo enviado com sucesso")
            return redirect(url_for("upload_file"))
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
