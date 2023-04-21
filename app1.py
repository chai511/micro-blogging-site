from flask import Flask, render_template

app=Flask(__name__)

class Galilean:
    def __init__(self,first,second,third,fourth) -> None:
        self.first=first
        self.second=second
        self.third=third
        self.fourth=fourth

@app.route("/loop/")
def hello_world_jinja():
    color="brown"
    animal_one="fox"
    animal_two="dog"
    orange_amount=10
    apple_amount=20
    donate_amount=15
    first_name="Cptain"
    last_name="Marvell"

    kwargs={
        'color':color,
        'animal_one':animal_one,
        'animal_two':animal_two,
        'orange_amount':orange_amount,
        'apple_amount':apple_amount,
        'donate_amount':donate_amount,
        'first_name':first_name,
        'last_name':last_name
    }
    '''return render_template("expression.html", **kwargs)'''
    movies=['dasara','das ka dhamki', 'dhamaka']
    car={'brand':'Maruthi', 'model':'Swift', 'year':'2012'}
    moons=Galilean('la','li','lu','le')
    kwargs={
        'movies':movies,
        'car':car,
        'moons':moons
     }
    '''return render_template("datastructures.html", **kwargs)'''
    company=''
    '''return render_template("conditionals.html", company=company)'''
    user_movies={
        'Chai':'Khushi',
        'Valli':'Murari',
        'Gayathri':'Das ka Dhamki'
    }
    return render_template("loops.html", user_movies=user_movies)


