class Student :
    def __init__(self,student_id, name, age, score):
        self.id = student_id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return(
            f"ID:{self.id},"
            f"姓名:{self.name},"
            f"年龄：{self.age},"
            f"成绩:{self.score}"
        )

    @classmethod
    def from_dict(cls,item):
        return cls(
                item["id"],
                item["name"],
                item["age"],
                item["score"]
        )
    
    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @staticmethod
    def is_valid_age(age):
        return age > 0

    #对象转字典
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "score": self.score
        }
    
    def update_score(self, new_score):
        if not self.is_valid_score(new_score):
            return False
        
        self.score = new_score
        return True

    def update_age(self, new_age):
        if not self.is_valid_age(new_age):
            return False
        
        self.age = new_age
        return True

    def is_passed(self):
        return self.score >= 60
