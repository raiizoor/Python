from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla import filters
from flask_admin.actions import action
from delivery.ext.db.models import User
from delivery.ext.db import db
from flask import flash, Markup

##def format_user(self, request, user, *args):
    ##return user.email.split("@")[0]


class UserAdmin(ModelView):
      """Interface admin de user"""


      column_formatters = {
          #"email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}<b>')          
      }

      column_list = ['email', 'name', 'admin']
      
      column_searchable_list = ['email']

      column_filters = [
          filters.FilterLike(
              User.email,
              "Email",
              options=(("gmail", "Gmail"), ("hotmail", "Hotmail"), ("outlook", "Outlook"))
          ),
          'name', 
          'admin'
          ]

      can_edit = False

      @action(
          'togle_admin',
          'Togle admin status',
          'Are you sure?'
      )
      def toggle_admin_status(self, ids):
            users = User.query.filter(User.id.in_(ids)).all()
            for user in users:  
              user.admin = not user.admin
            db.session.commit()
            flash(f"{len(users)}Usuário alterados com sucesso.", "success")
    
      @action("send_email", "send Email to all users", "Are you sure?")
      def send_email(self, ids):
          users = User.query.filter(User.id.in_(ids)).all()
          # 1) redirect para um form para escrever a mensagem do email
          # 2) enviar o email  
          flash(f"{len(users)} emails enviados com sucesso.", "success")