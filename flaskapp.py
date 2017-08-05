from flask import Flask, request
from flask import render_template
app = Flask(__name__)

from profdemo import *

@app.route('/', methods = ['Get', 'POST'])
def result():
	if request.method == 'POST':		
		keyword = request.form['Keyword']
		count = int(request.form['Count'])
		result = sentimentCalculator(keyword, count)
		labels = ['positive', 'negative', 'neutral']
		ganda = True
		if (result[0]==0 and result[1] ==0 and result[2]==0) :
			ganda = False
			result = "Sorry, We don't have the tweets."
		return render_template("result.html",values = result, labels = labels, keyword = keyword, ganda = ganda)
	else:
		return render_template('inputform.html')

	
if __name__ == '__main__':
  app.run()