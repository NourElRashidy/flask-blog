from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Post
import time

engine = create_engine(
    "mysql+pymysql://root:newrootpassword@localhost/garonzblog?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()

Post.Base.metadata.create_all(engine)


session.query(Post.Post).delete()
for i in range(0, 5) :
    test_post = Post.Post(author='nour', title='test '+str(i), body='test body '+str(i), publish_date = time.time())
    session.add(test_post)
session.commit()

def get_posts():
    return session.query(Post.Post).order_by(Post.Post.publish_date)

def add_post(author, title, body):
    new_post = Post.Post(author=author, title=title, body=body, publish_date = time.time())
    print(author, title, body)
    session.add(new_post)
    session.commit()
