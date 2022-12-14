from flask import render_template, flash, redirect, url_for
from app import app, db
from app.formulaires import FormulaireEtablirSession, FormulaireEnregistrement
from app.models import Utilisateur
from flask_login import current_user, login_user, logout_user, login_required
from flask import request
from werkzeug.urls import url_parse
from PIL import Image, ImageDraw, ImageFont
import random
import base64
from io import BytesIO
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.dernier_acces = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():

    utilisateurC = current_user
    publicationsC = current_user.publications.all()

    return render_template('index.html', titre='Accueil', utilisateurs=utilisateurC, publications = publicationsC)

@app.route('/utilisateur/<nom>')
@login_required
def utilisateur(nom):
    utilisateur = Utilisateur.query.filter_by(nom=nom).first_or_404()
    publications = utilisateur.publications.all()

    return render_template('utilisateur.html', utilisateur=utilisateur, publications = publications)

@app.route('/enregistrer', methods=['GET', 'POST'])
def enregistrer():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    formulaire = FormulaireEnregistrement()
    if formulaire.validate_on_submit():
        utilisateur = Utilisateur(nom=formulaire.nom.data, email = formulaire.courriel.data)
        utilisateur.enregistrer_mot_de_passe(formulaire.mot_de_passe.data)
        #fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
        image = Image.new('RGB', (128, 128), color = 'black')
        for i in range(20):
            x = random.randint(0, 128)
            y = random.randint(0, 128)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            h = random.randint(10, 20)
            #fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', h)
            d = ImageDraw.Draw(image)
            d.text((x,y), utilisateur.nom, fill=(r,g,b))

        tampon = BytesIO()
        image.save(tampon, format='JPEG')
        image_base64 = base64.b64encode(tampon.getvalue()).decode("utf-8")
        utilisateur.avatar= "data:image/jpg;base64," + image_base64
        #print("data:image/jpg;base64," + image_base64)

        db.session.add(utilisateur)
        db.session.commit()
        flash('Vous ??tes maintenant enregistr??s')
        return redirect(url_for('etablir_session'))
    return render_template('enregistrement.html', title='Enregistrer', formulaire=formulaire)


@app.route('/etablir_session', methods=['GET', 'POST'])
def etablir_session():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    formulaire = FormulaireEtablirSession()
    if formulaire.validate_on_submit():
        utilisateur = Utilisateur.query.filter_by(nom=formulaire.nom.data).first()
        if utilisateur is None or not utilisateur.valider_mot_de_passe(formulaire.mot_de_passe.data):
            flash('Nom utilisateur ou mot de passe invalides')
            return redirect(url_for('etablir_session'))
        login_user(utilisateur, remember=formulaire.se_souvenir_de_moi.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '' :
            return redirect(url_for('index'))
        return redirect(next_page)
    return render_template('etablir_session.html', title='??tablir une session', formulaire=formulaire)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))