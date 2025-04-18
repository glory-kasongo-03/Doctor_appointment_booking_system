class EHR:
    def __init__(self, ehr_id: str, medical_history: str, diagnosis: str, treatment_plan: str):
        self.ehr_id = ehr_id
        self.medical_history = medical_history
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan

    def view_record(self):
        print(f"Viewing EHR {self.ehr_id}")
        return {
            "Medical History": self.medical_history,
            "Diagnosis": self.diagnosis,
            "Treatment Plan": self.treatment_plan
        }

    def update_record(self, new_diagnosis: str, new_treatment_plan: str):
        self.diagnosis = new_diagnosis
        self.treatment_plan = new_treatment_plan
        print(f"EHR {self.ehr_id} updated.")
