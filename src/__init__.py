from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify,session
from .models.Todo import  Todo
from .models import db

import os
from .forms.todo_form import TodoForm

def create_app():
    
    app = Flask(__name__)
    
    db.init_app(app)
    APP_ROOT = os.path.dirname(os.path.dirname(__file__))
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(APP_ROOT, 'sqlite.db')
    
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
    app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    @app.route('/')
    def index():
        todos = Todo.query.all()
        return render_template('home.html', todos=todos)
        

    @app.route('/detail/<int:id>')
    def detail(id):
        todo = Todo.query.get_or_404(id)
        return render_template('todo/detail.html', todo=todo)


    

    @app.route('/update/<int:id>' ,methods=['GET', 'POST'])
    def update(id):
        todo = Todo.query.get_or_404(id)
        form = TodoForm()
        print(form.data)
        if form.validate_on_submit():
            todo.title = form.title.data
            todo.description = form.description.data
            todo.done = form.done.data
            print(form.data)
            db.session.commit()
            db.session.refresh(todo)
            db.session.close()
            return redirect(url_for('index'))
        return render_template('todo/update.html', form=form, id=id)
        
    @app.route('/delete/<int:id>')
    def delete(id):
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        flash('Todo item deleted!')
        return redirect(url_for('index'))
       

    @app.route('/create', methods=['GET', 'POST'])
    def create():
        form = TodoForm()
        if form.validate_on_submit():
            todo = Todo(title=form.title.data, description=form.description.data, done=form.done.data)
            db.session.add(todo)
            db.session.commit()
            flash('Todo item created!')
            return redirect(url_for('index'))
        return render_template('todo/create.html', form=form)
    

    with app.app_context():
        db.create_all()
        db.session.commit()

        

        
        


    return app
    