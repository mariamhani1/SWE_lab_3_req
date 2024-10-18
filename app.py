from crypt import methods

from flask import Flask,request,jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Doctors Appointment"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

doctor = [
    {'doc1':
        {'doctor_name':'Mohamed Hany',
        'Speciality': 'Gastroenterologist',
        'session_price':'500',
        'Address':'New Cairo'}
     }
]

@app.route('/api/doctors',methods=['GET'])
def get_doctors():
    if all(not d for d in doctor) == 'True':
        return "No Doctors Found",404
    for doc in doctor:
        return doc,200

@app.route('/api/doctors',methods=['POST'])
def post_doctor():
    data = request.get_json()
    c = len(doctor)+1
    doc = {'doc'+str(c):
               {'doctor_name':data['doctor_name'],
                'Speciality':data['Speciality'],
                'session_price':data['session_price'],
                'Address':data['Address']}}
    doctor.append(doc)
    return "Added Successfully",201

@app.route('/api/doctor/<int:id>',methods=['PUT'])
def update_doctor(id):
    data = request.get_json()
    for doc in range(len(doctor)):
        if id == doc+1:
            doctor[doc].update(
                {'doc' + str(id):
                 {'doctor_name': data['doctor_name'],
                  'Speciality': data['Speciality'],
                  'session_price': data['session_price'],
                  'Address': data['Address']}})

            return "Data Updated Successfully",201
        return "Doctor Not Found",404


@app.route('/api/doctor/<int:id>',methods=['DELETE'])
def delete_doctor(id):
    for doc in range(len(doctor)):
        if id == doc + 1:
            del doctor[doc]
            return "Deleted Successfully",204
        return "Doctor Not Found",404
if __name__ == '__main__':
    app.run(debug=True)
