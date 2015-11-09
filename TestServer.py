from flask import Flask #import library containing everything we need, now WORKS!
app = Flask(__name__) #idk... just do this to make an application I think?


@app.route("/") #if you got to UrL_NAME_SOMETHINg.SOMETHING/ the method below fires
def mainpage(): 
    return "Wassup Noobs, u finna get PK'd by Joe and Sid?"

if __name__ == "__main__": #if you run this program, ACTIVATE! (so we can import this safely)
    app.run(port=80) #port 80 means the default page. if it's not 80, say 5000 then we have to go to 127.0.0.1:5000 to make it work
    print ("hello world") #cuz fuck it, why not?
