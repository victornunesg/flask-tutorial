# Flask - framework de python que trata toda a parte por trás da criação de um site
# tratamento com o servidor, gerenciamento de links e etc
# Flask é mais simples que o Django0 o site vem mais leve e cru, porém o Django é mais roubusto

# Importando o Flask dentro da biblioteca
from flask import Flask

# Importando a função render template do Flask para auxiliar na chamada de páginas html, na pasta templates
from flask import render_template

# Criando o site
# Seguindo a documentação do Flask, é recomendado que o site seja chamado de app
app = Flask(__name__)  # ao iniciar o site, esse comando é necessário

# criar a primeira pgina do site
# toda página sempre tem um route (link, o caminho que vem após o domínio) e uma função
# route -> hashtagtrainamentos.com/contatos
# site se chama app, por isso temos app. Route pois iremos definir o link dentro do parêntese
# neste caso teremos o link da homepage
# chama-se decorator, é uma linha de código que atribui uma nova funcionalidade para a função que vem logo abaixo
# ou seja, a função homepage será exibida na home page do website


@app.route("/")
def homepage():  # função -> o que será exibido na página
    return render_template("homepage.html")
# aqui temos que colocar o que a página deve exibir, chamando o arquivo HTML dentro de 'templates' com o render
# não é necessário colocar o caminho da pasta, pois a função render_template automaticamente procura a pasta 'templates'


@app.route("/contatos")  # o link não necessariamente precisa ser do mesmo nome da função e vice versa
def contatos():
    return render_template("contatos.html")
# no return teremos a interação com o front-end, podendo chamar arquivos HTML/CSS
# recomenda-se criar uma pasta no mesmo local do projeto com o nome 'templates' de acordo com o framework Flask
# nessa pasta, pode-se inserir arquivos html para melhorar o layout do website

# criando páginas de modo dinâmico
# <> diz ao Flask que o que for escrito depois da / é o nome do usuário
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):  # para funcionar a função precisa receber o nome do usuario como parametro
    return render_template("usuarios.html", nome_usuario=nome_usuario)  # passando o valor para o HTML
# o primeiro 'nome_usuario' é a variável que está lá no HTML e o segundo nome é o que veio do render_template
# no html, chamar a variavel entre duas chaves, vide arquivo html de exemplo

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
# Ativando o debug para evitar de, ao alterar o código, ser necessário parar a compilação e rodar novamente
# dessa forma, basta atualizar a página no navegador para obter as atualizações
# esse comando faz com que o código abaixo seja executado somente quando estivermos rodando diretamente esse arquivo,
# ou seja, caso esse código seja importado por outro arquivo, não será executado. É importante ter essa parte do código
# pois pode dar erro quando for compilado depois que o site estiver pronto


# para colocar o site no ar publicamente, temos que seguir um passo a passo
# neste caso, estaremos utilizando o servidor do heroku (gratuito para poucos acessos)
# 1) garantir que o app.run esta dentro do if da linha 47
# 2) criar a conta no heroku > new > create new app > escolher o nome (url do site)
# 3) sera mostrado o passo a passo para deploy do site, instalando o heroku CLI primeiramente (necessario ter o git)
# 4) o pycharm precisa reconhecer as instalacoes, nao eh automatico, basta reiniciar o pycharm para dar baixa
# 5) no terminal, conferir se ao digitar `git` e `heroku`, a lista dos comandos sera apresentada.qualquer coisa
#  reiniciar o pc
# 6) pra funcionar, o servidor precisa identificar o que fizemos de python no codigo, o que temos instalado
# 7) criar arquivo txt chamado 'procfile' (sem extensao definida) novo arquivo > digitar nome e pronto
# 8) abrir o procfile como txt (deve estar junto do codigo) e digitar, de acordo com o flask,
# o seguinte codigo 'gunicorn meu_site:app'
# 9) como estamos o guinicorn, no terminal do codigo main, digitar 'pip install gunicorn'
# 10) criar arquivo txt chamado 'requirements.txt' usando o comando 'pip freeze > requirements.txt', esse comando faz
# com que o flask jogue todas as informacoes pertinentes do codigo nesse arquivo para interpretacao do servidor

# agora vamos pegar o projeto e jogar no online usando o passo a passo do heroku
# 1) no terminal, digitar 'heroku login', apos apertar qualquer tecla, o browser sera aberto para logar
# 2) voltar no site do heroku para as demais instrucoes
# 3) no terminal, dar o 'git init' (configurar antes se nao estiver instalado)
# 4) outro comando no terminal 'heroku git remote -a nomedoseusite'
# 5) mais tres passos no heroku

# esse passo a passo do heroku seria apenas para colocar o site no ar
# caso haja acrescimo de paginas ou demais alteracoes, eh necessario apenas:

# 1) git add
# 2) git commit -am "mensagem"
# 3) git push heroku master
