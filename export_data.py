# export_data.py
from thepensiveFlask import db
from thepensiveFlask.models import Blog, User
import json

def export_blogs():
    blogs = Blog.query.all()
    data = []
    for blog in blogs:
        data.append({
            'title': blog.title,
            'preview': blog.preview,
            'content': blog.content,
        })
    with open('blogs.json', 'w') as f:
        json.dump(data, f)

def export_users():
    users = User.query.all()
    data = []
    for user in users:
        data.append({
            'username': user.username,
            'password': user.password,  # Ensure passwords are hashed
        })
    with open('users.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    export_blogs()
    export_users()
