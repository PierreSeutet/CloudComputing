from flask import Flask
from flask import render_template, url_for, request, redirect
app = Flask(__name__,template_folder='templates')
import os
import tensorflow as tf
import pandas as pd
from transformers import pipeline

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        model = tf.keras.models.load_model('/Users/matteo/Desktop/dockertest/model_de_ouf.h5')
        print("cd",type(request.form['cdpostal']))
        input = {'codePostal': float(request.form['cdpostal']), 'Size': float(request.form['taille']), 'nb_piece': float(request.form['nbpiece']), 'Nb_bathroom': float(request.form['Nb_bathroom']), 'Num_Etage': float(request.form['num_Etage']), 'Nombre_etages': float(request.form['Nombre_etages']), 'Type': float(request.form['type']), 'Meuble': float(request.form['Meuble']), 'Chauffage': float(request.form['Chauffage']), 'TerrasseBalcon': float(request.form['Terrasse']), 'Gardien': float(request.form['Gardien']), 'Acces_handicape': float(request.form['Acces_handicape']), 'Securite': float(request.form['Securite']), 'Cave': float(request.form['Cave']), 'Ascenseur': float(request.form['Ascenseur']), 'Parking': float(request.form['Parking']), 'Climatisation': float(request.form['Climatisation']), 'Piscine': float(request.form['Piscine']), 'Jardin': float(request.form['Jardin']), 'Garage': float(request.form['Garage'])}
        print(input)
        print(type (input))
        mm = pd.DataFrame.from_dict(input, orient='index',columns=["Mon_logement" ])
        valeur_a_predire = mm.T.values
        
        print(valeur_a_predire)
        print(type(valeur_a_predire))

        predicted = model.predict(valeur_a_predire)
        print("YES")

        print(predicted)
        print(type(predicted))
        print(predicted[0][0])
        prediction = predicted[0][0]
        print(prediction)
        print(type(prediction))
        print(str(prediction))
        print(type(str(prediction)))
    return str(prediction)

        #return render_template('index.html', glon=glon, output = "oio" )
    #else  : 
     #   return render_template('index.html')
# @app.route('/return_form/<glon>', methods = ['GET', 'POST'])
# def return_form(glon):
#     return render_template('return_form.html', glon=glon)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))