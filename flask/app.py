from flask import Flask, render_template
from numpy import nan, log
import pandas

app = Flask(__name__)

@app.template_filter( 'scale_kcat' )
def color_kcat( kcat ):
    if kcat == nan:
        return rgba( 1, 1, 1, 0.1 )
    else:
        return 

@app.route( '/' )
def index():
  df = pandas.read_csv( '../data/pub_data.csv', index_col=0 )
  ii = [ i for i in df.iterrows() ]
  return render_template( 'index.html', ii=ii )

if __name__ == '__main__':
    app.run()
