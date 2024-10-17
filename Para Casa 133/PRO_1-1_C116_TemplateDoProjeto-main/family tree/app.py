# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Rian Willian" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def first_flask():
    return "Pai"
# defina a rota para a página da mãe
@app.route("/mãe")
def second_flask():
    return "Mãe"
# defina a rota para a página do amigo
@app.route("/amigo")
def third_flask():
    return "Amigo"
# adicione outras rotas, se você quiser
@app.route("/index")
def first_page(): 
    name = "Rian" 
    return render_template("index.html", index_variable = name)


# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
