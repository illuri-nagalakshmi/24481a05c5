from flask import Flask, render_template, request

app = Flask(name)

@app.route('/')
def welcome():
return render_template('base.html')

@app.route('/greet/<uname>')
def greet(uname):
return f'''
<div style=" text-align:center; margin-top:100px; font-family:Arial; color:blue; font-size:30px; ">
Good morning! {uname}
</div>
'''

@app.route('/user', methods=['GET', 'POST'])
def myprofile():
data = None

if request.method == 'POST':
    data = request.form

return render_template('base.html', data=data)


if name == 'main':
app.run(debug=True)
