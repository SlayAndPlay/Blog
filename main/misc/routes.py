from flask import render_template, request, Blueprint, url_for
from main.models import Post

misc = Blueprint('misc', __name__)


@misc.route("/")                         # routes - urls
@misc.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=post, title="Home")     # posts allow us to pass in data
                                                        # that we can use in html file.


@misc.route("/about")
def about():
    image_file = url_for('static', filename='profile_pics/christian_perez.jpeg')
    return render_template("about.html", title="About", image_file=image_file)


