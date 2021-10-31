# Put your app in here.
import operations
import flask

app = flask.Flask(__name__)

@app.route('/add')
def add(): 
    lst_args = get_args()
    return str(operations.add(lst_args[0], lst_args[1]))

@app.route('/sub')
def sub():
    lst_args = get_args()
    return str(operations.sub(lst_args[0], lst_args[1]))

@app.route('/mult')
def mult():
    lst_args = get_args()
    return str(operations.mult(lst_args[0], lst_args[1]))

@app.route('/div')
def div():
    lst_args = get_args()
    return str(operations.div(lst_args[0], lst_args[1]))

def get_args():
    a = flask.request.args["a"]
    b = flask.request.args["b"]
    return [int(a),int(b)]

@app.route('/math/<operation>')
def oper(operation):
    lst_args = get_args()
    operators = {"add": operations.add,
                "sub": operations.sub,
                "mult": operations.mult,
                "div": operations.div}
    return str(operators[operation](lst_args[0], lst_args[1]))