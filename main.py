from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
@app.route('/register',methods=['POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        return render_template('success.html')
    return render_template('index.html')
if __name__=='__main__':
    print("xyz")
    app.run(host='0.0.0.0',port=8000)