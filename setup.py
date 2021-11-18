from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')          

def hello_world():

    return  render_template ("inicio2.html") 

@app.route('/registro')          

def registro():

    return  render_template ("registro.html")    


@app.route('/iniciado')  
def iniciado():

    return render_template("iniciado.html")


@app.route('/nombre', methods=["post"])
def nombre():
    name=request.form["name"]
    return render_template("nombre2.html",name=name)


@app.route('/quienes')          

def quienes():

    return  render_template ("quienessomos.html")








if __name__=="__main__":   

    app.run(debug=True)   
