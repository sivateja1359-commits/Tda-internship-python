from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store blog posts
posts = []

# ---------------- Base Template ----------------
base_html = """
{% block base %}
<!DOCTYPE html>
<html>
<head>
    <title>My Flask Blog</title>
    <style>
        body { font-family: Arial; margin: 20px; background: #f5f5f5; }
        header { margin-bottom: 20px; }
        nav a { margin-right: 15px; text-decoration: none; color: #333; }
        nav a:hover { text-decoration: underline; }
        .card { background: white; padding: 15px; margin: 10px 0; border-radius: 5px; }
        textarea { width: 300px; height: 130px; }
        input, textarea { padding: 5px; }
        button { padding: 8px 15px; margin-top: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <header>
        <h1>My Personal Blog</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/create">Create Post</a>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

</body>
</html>
{% endblock %}
"""

# ---------------- Home Page ----------------
index_html = """
{% extends base %}
{% block content %}
<h2>All Posts</h2>

{% for post in posts %}
<div class="card">
    <h3><a href="/post/{{ loop.index0 }}">{{ post.title }}</a></h3>
</div>
{% else %}
<p>No posts yet. Create one!</p>
{% endfor %}

{% endblock %}
"""

# ---------------- Create Page ----------------
create_html = """
{% extends base %}
{% block content %}
<h2>Create New Post</h2>

<form method="post">
    <label>Title:</label><br>
    <input type="text" name="title" required><br><br>

    <label>Content:</label><br>
    <textarea name="content" required></textarea><br>

    <button type="submit">Publish</button>
</form>

{% endblock %}
"""

# ---------------- View Post Page ----------------
view_html = """
{% extends base %}
{% block content %}
<h2>{{ post.title }}</h2>
<div class="card">
    <p>{{ post.content }}</p>
</div>
{% endblock %}
"""

# ---------------- Routes ----------------

@app.route("/")
def index():
    return render_template_string(index_html, base=base_html, posts=posts)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        return redirect(url_for("index"))
    return render_template_string(create_html, base=base_html)

@app.route("/post/<int:post_id>")
def view_post(post_id):
    post = posts[post_id]
    return render_template_string(view_html, base=base_html, post=post)

# ---------------- Run App ----------------
if __name__ == "__main__":
    app.run(debug=True)