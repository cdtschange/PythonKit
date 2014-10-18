from eve import Eve
app = Eve()

if __name__ == '__main__':
	app.run()

#$ curl -i http://127.0.0.1:5000
#$ curl http://127.0.0.1:5000/people
#$ curl -d '[{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/people
#$ curl -i http://127.0.0.1:5000/people/obama

#$ curl -i http://127.0.0.1:5000/people?where={"lastname": "Doe"}
#$ curl -i http://127.0.0.1:5000/people?where=lastname=="Doe"
#$ curl -i http://127.0.0.1:5000/people?sort=city,-lastname
#$ curl -i http://127.0.0.1:5000/people?sort=[("lastname", -1)]
#$ curl -i http://127.0.0.1:5000/people?max_results=20&page=
#$ curl -H "Accept: application/xml" -i http://127.0.0.1:5000/people
