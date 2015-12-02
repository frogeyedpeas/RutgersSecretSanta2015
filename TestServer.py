from flask import Flask, render_template #import library containing everything we need, now WORKS!
app = Flask(__name__) #idk... just do this to make an application I think?


@app.route('/') #if you got to UrL_NAME_SOMETHINg.SOMETHING/ the method below fires
@app.route('/index')
def mainpage(): 
    print ("COOL BEANZ MAAAN!")
    return render_template('index.html')
	
@app.route('/getData', methods=['POST'])
def getData():
	print("I have the data!")
	print(request.form['firstname']+'\n'+request.form['lastname'])

if __name__ == "__main__": #if you run this program, ACTIVATE! (so we can import this safely)
    app.run(debug=True, port=80) #port 80 means the default page. if it's not 80, say 5000 then we have to go to 127.0.0.1:5000 to make it work
    print ("hello world") #cuz fuck it, why not?