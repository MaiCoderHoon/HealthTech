import json

from fastapi import FastAPI, Path

app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        return json.load(f)
    
@app.get("/")

def home():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message":"A fully functional API for managing patient records" }

@app.get("/patients")
def view_patients():
    data = load_data()
    return {"patients": data}

@app.get("/patients/{patient_id}")
def view_patients__id(patient_id: str = Path(..., description="The ID of the patient to retrieve",example = "P001")):
    data = load_data()
    if patient_id in data:
        return {"patient" : data[patient_id]}
    
    return {"message": "Patient not found"}