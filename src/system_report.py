from user_account import UserAccount

class SystemReport:
    def __init__(self, report_id: str, type_: str, content: str, generated_by: UserAccount):
        self.report_id = report_id
        self.type = type_
        self.content = content
        self.generated_by = generated_by

    def generate(self):
        print(f"Report {self.report_id} of type {self.type} generated.")

    def export(self):
        print(f"Report {self.report_id} exported.")
