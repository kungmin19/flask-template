from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' , title = 'My Home Page')

@app.route('/about')
def about():
    title = 'About Me'
    name='John Doe'
    email='Std67122420124'
    Phone='123-456-7890'
    return render_template('about.html',
                    title=title,
                    name=name,
                    email=email,
                    Phone=Phone)

@app.route('/faverite_song/song')
def faverite_song():
    title = 'My Faverite Song'
    song = ['tidalwave', 'heavent and back', 'into it', 'TheWall']
    return render_template('faverite_song.html',
                            song=song,
                            title=title)

@app.route('/sport')
def sports():
    title = 'My Faverite Sport'
    sport = ['basketball', 'baseball', 'badminton', 'swimming']
    return render_template('sports.html',
                           sport=sport,
                            title=title)  
  
@app.route('/greeting/<username>')
def wellcome(username):
    title = 'Wellcome Page'
    return render_template('wellcome.html',
                            username=username,
                            title=title)

@app.route('/movies')
def movies():
    title='Favorite Movies Page'
    movies = ['ไททานิค','2012วันสิ้นโลก','BADBOY','จูแมนจี้','กำเเพงมรณะ']
    return render_template('movies.html',
                           title=title,
                            movies=movies,)