from eve import Eve
app = Eve()

if __name__ == '__main__':
	app.run()

#$ curl -i http://eve-demo.herokuapp.com/people?where={"lastname": "Doe"}
#$ curl -i http://eve-demo.herokuapp.com/people?where=lastname=="Doe"
#$ curl -i http://eve-demo.herokuapp.com/people?sort=city,-lastname
#$ curl -i http://eve-demo.herokuapp.com/people?sort=[("lastname", -1)]
#$ curl -i http://eve-demo.herokuapp.com/people?max_results=20&page=2