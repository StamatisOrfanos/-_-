from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
import json


# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database
db = client['InfoSys']
students = db['Students']

# Initiate Flask App
app = Flask(__name__)


#1st Question: Get the name of the students that have an address with data 
@app.route('/getAllStudentsAddress', methods=['GET'])
def get_student_by_address():    

    result = students.find( {"address": {"$ne": "[]"}})
    
    if   result == None:
        return Response('no student found',status=500,mimetype='application/json')

    else:
    	names = students.find( {"address1": {"$ne": "[]"}})
    	list1 = []
    	
    	for i in names:
            student = {'name':i["name"]}
            list1.append(student)
    		
    return jsonify(list1)



#2nd Question: Get the address of a student based on the email (I choose to print both the address and the email in case there is need to match)
@app.route('/getStudentsAddress/<student_email>', methods=['GET'])
def get_address_by_email(student_email):
    
    if student_email == None:
	    return Response('no student found',status=500,mimetype='application/json')

    result = students.find({"$and": [ {"student_email": {"$exists":"true"}}, {"address": {"$ne": "[]"}}] }) 
    
    if result  == None:
        return Response("Bad request", status=500, mimetype='application/json')
    
    else:
	    addresses = students.find({"$and": [ {"student_email": {"$exists":"true"}}, {"address": {"$ne": "[]"}}] })
	    list2 = []
	    for i in addresses:
	    	address = {'address':str(i["address"]) }
	    	list2.append(address)
    return jsonify(list2)


#3rd Question: Get the names of a student that have both an address and are born in the 1980s
@app.route('/getEightiesAddress', methods=['GET'])
def get_student_by_Eighties_Address():
    result = students.find({"$and": [ {"address": {"$ne": "[]"}}, {"yearOfBirth": { "$and": [{ "$gte": 1980}, {"$lte": 1989}] }} ] })
    
    if result == None:
        return Response('no student found',status=500,mimetype='application/json')
    
    else:
	    num_names = result
	    list3 = []
	    for i in num_names:	
		    student = {'name':i["name"]}
		    list3.append(student)
    return jsonify(list3)




#4th Question: Get the number of all the students that have an address 
@app.route('/countAddress', methods=['GET'])
def get_count_of_Students_with_Address():
    number_of_students = students.find({"address": {"$ne": "[]"}}).count()
    return jsonify({"Number of students": number_of_students})



#5th Question: Insert the name of the student and the address data
@app.route('/insertstudent', methods=['POST'])
def insert_student():
    data = None
    try:
        data = json.loads(request.data.decode('UTF-8'))
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
        
    if data == None:
       return Response("bad request",status=500,mimetype='application/json')
    
    if not "name" in data or not "email" in data or not "yearOfBirth" in data or not "address" in data:
        return Response("Information incompleted",status=500,mimetype="application/json")
        
    existing_user = students.find({"email":data["email"]}).count()
    
    if existing_user == 0 :
        student = { "name": data["name"], "email": data["email"], "yearOfBirth": data["yearOfBirth"], "address": data["address"]}
        #We add the new student with the data for the name, email, yearOfBirth and the address data
        
        students.insert_one(student)
        return Response("was added to the MongoDB",status=200,mimetype='application/json') 
    else:
        return Response("A user with this email already exists in MongoDB",status= 200, mimetype="application/json")



#6th Question: Get the number of all the students that have an address 
@app.route('/countYearOfBirth/<yearOfBirth>', methods=['GET'])
def get_count_of_Students_with_YearOfBirth(yearOfBirth):
    theYear = int(yearOfBirth)
    number_of_students = students.find({"yearOfBirth": theYear}).count()
    return jsonify({"Number of students": number_of_students})



# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
