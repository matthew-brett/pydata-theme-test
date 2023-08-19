from docutils import nodes

def setup(app):
    app.set_translator('foo', nodes.NodeVisitor)
