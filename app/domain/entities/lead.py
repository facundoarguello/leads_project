from datetime import datetime

class LeadEntity:


    def __init__(self, id: int, fullname: str, email: str, address : str ,phone: str, subject: str, course_time: int, career:str ,inscription: datetime, number_courses:int):
        self.id = id
        self.fullname = fullname
        self.address = address
        self.email = email
        self.phone = phone
        self.subject = subject
        self.course_time = course_time
        self.career = career
        self.inscription = inscription
        self.number_courses = number_courses
class LeadEntityFactory:

    @staticmethod
    def create(id: int, fullname: str, address: str,email: str, phone: str, subject: str,
                course_time: int, career:str ,inscription: datetime, number_courses:int) -> LeadEntity:
        return LeadEntity(id, fullname, email, address,phone, subject, course_time, career, inscription, number_courses)
