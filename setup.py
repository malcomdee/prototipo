from flask import Flask, render_template, request

app = Flask(__name__)   








@app.route('/')          

def hello_world():

    return  render_template ("registro.html") 
    
@app.route('/nombre', methods=["post"])
def nombre():
    name=request.form["name"]
    return render_template("nombre2.html",name=name)

@app.route('/inicio')          

def inicio():

    return  render_template ("inicio2.html") 

@app.route('/quienes')          

def quienes():

    return  render_template ("quienessomos.html")

@app.route('/calculadora')          

def calculator():

    return  render_template ("index2.html")

@app.route('/calculo', methods=["POST"])       

def resultado():

    nr1 = request.form["nr1"]

    a = request.form["a"]

    nr2 = request.form["nr2"]
    if a == "+":

        result= int(nr1)+int(nr2)

    if a == "-":

        result= int(nr1)-int(nr2)

    if a == "*":

        result= int(nr1)*int(nr2)

    if a == "/":

        result= int(nr1)/int(nr2)

    if a == "**":

        result= int(nr1)**int(nr2)


    return  render_template ("result2.html", nr1 = nr1 , a = a, nr2 = nr2, result=result) 







if __name__=="__main__":   

    app.run(debug=True)    

