from flask import Flask, render_template
from wxpy import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    # init
    bot = Bot()
    friends = bot.friends()
    sex_dict = {'male': 0, 'female': 0}
    for friend in friends:
        if friend.sex == 1:
            sex_dict['male'] += 1
        elif friend.sex == 2:
            sex_dict['female'] += 1

    male = sex_dict['male'] / 100
    female = sex_dict['female'] / 100
    return render_template('male_female.html', male=male, female=female)


if __name__ == '__main__':
    app.run(debug=True)

