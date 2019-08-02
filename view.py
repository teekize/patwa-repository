from flask import (Flask,render_template, url_for,
                     redirect,request,g, flash)

from app.models.database import Database, initalize
import pdb

db =Database()
app =Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

id_information={
                "id_number":35533709,
                "when_found":"Friday 27/10/2019",
                "who_found":"John"
}
# @app.before_request
# def before_request():
#     g.db= Database()
#     return g.db

# @app.after_request
# def after_request(response):
#     g.db.close()
#     return response

@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")

@app.route("/landing", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/profile", methods=["GET"])
def profile():
    return render_template("profile.html")

@app.route("/login", methods=["GET"])
def login():

    return render_template("login.html")
 
@app.route("/register", methods=["POST"])
def register():
    if request.method =="POST":
        form =request.form.get("Username"), request.form.get('Password')

        insert ="insert into users values( null, ?,?)"

        resp =db.query_(insert,form)
        flash('You were successfully logged in {}'.format(resp))
        return redirect(url_for('landing'))
    return render_template('login.html')




@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method =="POST":
        """
        this form receives the form data that the user sends out to search for the 
        id. form_data should only be integer.
        """
        form_data =request.form.get("ID", "nothing has been submitted")
        if len(form_data.strip())==0:
            return "there should be data"
        print(form_data)
        if int(form_data) == id_information["id_number"]:
            return render_template('lost_id.html', id_information=id_information)
    

        # query ="select item_name, item_id from collected_items where lost_item_id = ?"
        
        # form_data =request.form.get("ID", "bado haiko")
        # resp =db.query_(query,form_data)
        # # print(form_)
        
        # response =Database.query_(query, form_)
        return redirect(url_for('landing'))
    return "requets cannot be served using GET request"

if __name__ =="__main__":
    app.run()
    # initalize()