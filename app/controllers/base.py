from flask import render_template, redirect, session

from app import app


@app.route('/')
def inicio():

    if 'usuario' not in session:
        return redirect('/login')

    return render_template('inicio.html')