from delivery.ext.db.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)