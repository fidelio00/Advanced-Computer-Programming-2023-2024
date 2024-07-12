# hello-render.py
from flask import Flask, render_template, request
# render_template è utilizzato per renderizzare i template HTML. 
# request viene utilizzato per accedere ai dati delle richieste HTTP
import os
# os è utilizzato qui per gestire i percorsi dei file.

#app = Flask(__name__)
# template_dir è la variabile che contiene il percorso assoluto 
# della cartella 02_templates, che contiene i template HTML
template_dir = os.path.abspath('./02_templates/')
print(f"Template directory: {template_dir}")  # Aggiunto per il debug
app = Flask(__name__, template_folder=template_dir)

# Flask renderizza e ritorna il template index.html.
@app.route("/index")
def index():
    return render_template('index.html')


# <name> è un parametro variabile. 
# Flask renderizza il template user.html passando il parametro name.
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# Se name è "pippo", viene passato al template user_adv.html 
# anche una lista di elementi. Altrimenti, viene renderizzato 
# user_adv.html senza parametri aggiuntivi.
@app.route('/user_adv/<name>')
def user_adv(name):
    if name == "pippo":
        return render_template('user_adv.html', name=name, elements=['String', 10, {'key':'value'}])
    else:    
        return render_template('user_adv.html')



@app.route('/user_agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return user_agent

# test: curl --json '{"text":"prova"}' http://127.0.0.1:5000/json
# Riceve il corpo della richiesta in formato JSON, 
# lo stampa nella console e lo restituisce come risposta.
@app.post('/json')
def json():
   json = request.get_json()
   print(json)
   return json

# test: curl -d 'prova' http://127.0.0.1:5000/data
# Riceve il corpo della richiesta come testo semplice, 
# lo stampa nella console e lo restituisce come risposta.
@app.post('/data')
def data():
   data = request.get_data(as_text=True)
   print(data)
   return data

# test: curl "http://127.0.0.1:5000/hello?name=pippo&surname=pippozzo"
# Legge i parametri di query name e surname dalla richiesta, 
# li stampa nella console e li restituisce come risposta.
@app.get('/hello')
def hello():
   params = request.args
   print("name:", params['name'])       
   print("surname:", params['surname']) 
   return params


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)




