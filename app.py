from flask import Flask, render_template
from markupsafe import escape



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/a-hluti")
def ahluti():
    return render_template('kennitala.html')

@app.route("/k-tala/<kt>")
def ktalan(kt):
    summa=0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html',kt=kt,summa=summa)

@app.route("/b-hluti")
def bhluti():
    return render_template('frettir.html', frettir=frettir)

frettir = [
    ["0","KIM","  KIM JONG un fanst í kjallara hvítahúsins sumir halda að trump hafi sneakað honum inn","Jonni Karl Arm"],
    ["1","Ísland tapar","lenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli. Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum.","Pétur álson"],
    ["2","Snjór í september","Það datt inn heilmikill snjór á Siglufirði og komust íbúar ekki úr húsi vegna snjófalls 330cm af snjó féllu í nótt ","Stefanía kristjansen"],
    ["3","Ólafía stendur sig vel","Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili.","Pumba"]
]
@app.route("/frett/<int:id>")
def news(id):
    return render_template('frett.html', frett=frettir[id],nr=id)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Blessaður %s' % escape(username)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'), 500

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)