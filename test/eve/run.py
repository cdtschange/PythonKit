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
#$ curl -H "If-Modified-Since: Wed, 05 Dec 2012 09:53:07 GMT" -i http://127.0.0.1:5000/people
#$ curl -H "If-None-Match: 1234567890123456789012345678901234567890" -i http://127.0.0.1:5000/people
#$ curl -X PATCH -i http://127.0.0.1:5000/people/544250040041e0087684e477 -d '{"firstname": "ronald"}'
#$ curl -H "If-Match: 1234567890123456789012345678901234567890" -X PATCH -i http://127.0.0.1:5000/people/544250040041e0087684e477 -d '{"firstname": "ronald"}'
#$ curl -H "If-Match: b14a4cd77b0a6f83f00617843aec71b890b01475" -X PATCH -i http://127.0.0.1:5000/people/544250040041e0087684e477 -d '{"firstname": "ronald"}'
#$ curl -d '{"firstname": "barack", "lastname": "obama"}' -H 'Content-Type: application/json' http://127.0.0.1:5000/people
#$ curl -d '[{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}]' -H 'Content-Type: application/json' http://127.0.0.1:5000/people
