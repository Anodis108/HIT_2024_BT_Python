class Job:
    def __init__(self, id_job, name_job, major, salary) -> None:
        self._id_job = id_job
        self._name_job = name_job
        self._major = major
        self._salary = salary
        
    def __str__(self) -> str:
        return f'ID: {self._id}, Tên: {self._job_name}, Lĩnh vực: {self._job_field}, Lương: {self._salary}'
        
class AI(Job):
    def __init__(self, pythonSkill, mlSkill, deepSkill, mathSkill, **kwargs) -> None:
        super().__init__(**kwargs)
        self._pythonSkill = pythonSkill
        self._mlSkill = mlSkill
        self._deepSkill = deepSkill
        self._mathSkill = mathSkill
        self._score_dict = {
            'pythonSkill': self._pythonSkill,
            'mlSkill'    : self._mlSkill,
            'deepSkill'  : self._deepSkill,
            'mathSkill'  : self._mathSkill
        }
    
    def __str__(self) -> str:
        return f'ID: {self._id_job}, Tên: {self._name_job}, Lĩnh vực: {self._major}, Lương: {self._salary}, pythonSkill: {self._pythonSkill}, deepSkill: {self._deepSkill}, mathSkill: {self._mathSkill}'
    
    def evaluate(self):
        _dict = self._score_dict
        score = sum(_dict.values()) / len(_dict)
        if score > 9.0:
            return "Rất phù hợp"
        elif score > 7.0:
            return "Phù hợp"
        elif score > 5.0:
            return "Tạm được"
        elif score > 3.0:
            skills_can_bo_sung = []
            for skill, diem in _dict.items():
                if diem < 4.0:
                    skills_can_bo_sung.append(skill)
            return f"Cần bổ sung thêm kiến thức: {skills_can_bo_sung}"
        else:
            return "Cần học lại kiến thức nền tảng"
        
class BackEnd(Job):
    def __init__(self, SQLSkill, OOPSkill, api_Skill, javaSkill, **kwargs) -> None:
        super().__init__(**kwargs)
        self._SQLSkill = SQLSkill
        self._OOPSkill = OOPSkill
        self._apiSkill = api_Skill
        self._javaSkill = javaSkill
        self._score_dict = {
            'SQLSkill' : self._SQLSkill,
            'OOPSkill' : self._OOPSkill,
            'api_Skill': self._apiSkill,
            'javaSkill': self._javaSkill
        }
        
    def __str__(self) -> str:
        return f'ID: {self._id_job}, Tên: {self._name_job}, Lĩnh vực: {self._major}, Lương: {self._salary},SQLSkill: {self._SQLSkill}, OOPSkill: {self._OOPSkill},api_Skill: {self._apiSkill}, javaSkill: {self._javaSkill}'
    
    def evaluate(self):
        _dict = self._score_dict
        score = sum(_dict.values()) / len(_dict)
        if score > 9.0:
            return "Rất phù hợp"
        elif score > 7.0:
            return "Phù hợp"
        elif score > 5.0:
            return "Tạm được"
        elif score > 3.0:
            skills_can_bo_sung = []
            for skill, diem in _dict.items():
                if diem < 4.0:
                    skills_can_bo_sung.append(skill)
            return f"Cần bổ sung thêm kiến thức: {skills_can_bo_sung}"
        else:
            return "Cần học lại kiến thức nền tảng"
        
class FrontEnd(Job):
    def __init__(self, Html_Skill, Css_Skill, Nodejs_Skill, UX, UI,**kwargs) -> None:
        super().__init__(**kwargs)
        self._Html_Skill = Html_Skill
        self._Css_Skill = Css_Skill
        self._Nodejs_Skill = Nodejs_Skill
        self._UX = UX
        self._UI = UI
        self._score_dict = {
            'Html_Skill': self._Html_Skill,
            'Css_Skill': self._Css_Skill,
            'Nodejs_Skill': self._Nodejs_Skill,
            'UX': self._UX,
            'UI': self._UI
        }
    
    def __str__(self) -> str:
        return f'ID: {self._id_job}, Tên: {self._name_job}, Lĩnh vực: {self._major}, Lương: {self._salary}, Html_skill: {self._Html_Skill}, Css_Skill: {self._Css_Skill}, Node_js_Skill: {self._Nodejs_Skill}, UI: {self._UI}, UX: {self._UX}'
    
    def evaluate(self):
        _dict = self._score_dict
        score = sum(_dict.values()) / len(_dict)
        if score > 9.0:
            return "Rất phù hợp"
        elif score > 7.0:
            return "Phù hợp"
        elif score > 5.0:
            return "Tạm được"
        elif score > 3.0:
            skills_can_bo_sung = []
            for skill, diem in _dict.items():
                if diem < 4.0:
                    skills_can_bo_sung.append(skill)
            return f"Cần bổ sung thêm kiến thức: {skills_can_bo_sung}"
        else:
            return "Cần học lại kiến thức nền tảng"
        
class FullStack(BackEnd, FrontEnd):
    def __init__(self, SQLSkill, OOPSkill, api_Skill, javaSkill, **kwargs) -> None:
        super().__init__(SQLSkill, OOPSkill, api_Skill, javaSkill, **kwargs)
        self._score_dict['Html_Skill'] = kwargs.get('Html_Skill')
        self._score_dict['Css_Skill'] = kwargs.get('Css_Skill')
        self._score_dict['Nodejs_Skill'] = kwargs.get('Nodejs_Skill')
        self._score_dict['UX'] = kwargs.get('UX')
        self._score_dict['UI'] = kwargs.get('UI')
                    
    def __str__(self) -> str:
        return f'ID: {self._id_job}, Tên: {self._name_job}, Lĩnh vực: {self._major}, Lương: {self._salary},SQLSkill: {self._SQLSkill}, OOPSkill: {self._OOPSkill},api_Skill: {self._apiSkill}, javaSkill: {self._javaSkill}, Html_skill: {self._Html_Skill}, Css_Skill: {self._Css_Skill}, Node_js_Skill: {self._Nodejs_Skill}, UI: {self._UI}, UX: {self._UX}'
                        
                       
    def evaluate(self):
        _dict = self._score_dict
        score = sum(_dict.values()) / len(_dict)
        if score > 9.0:
            return "Rất phù hợp"
        elif score > 7.0:
            return "Phù hợp"
        elif score > 5.0:
            return "Tạm được"
        elif score > 3.0:
            skills_can_bo_sung = []
            for skill, diem in _dict.items():
                if diem < 4.0:
                    skills_can_bo_sung.append(skill)
            return f"Cần bổ sung thêm kiến thức: {skills_can_bo_sung}"
        else:
            return "Cần học lại kiến thức nền tảng"                  
        
if __name__ == '__main__':
    # Create 4 object AI, BackEnd, FrontEnd, FullStack
    ai = AI(id_job=1, name_job='AI', major='IT', salary=2000, pythonSkill=10, mlSkill=1, deepSkill=1, mathSkill=2 )
    backend = BackEnd(id_job=2, name_job='BackEnd', major='IT', salary=1500, SQLSkill = 0, OOPSkill = 1, api_Skill = 2, javaSkill = 3)
    frontend = FrontEnd(id_job=3, name_job='FrontEnd', major='IT', salary=1250, Html_Skill = 10, Css_Skill=10, Nodejs_Skill=10, UX=10, UI=10)
    fullstack = FullStack(id_job=4, name_job='FullStack', major='IT', salary=2500, SQLSkill = 0, OOPSkill = 1, api_Skill = 2, javaSkill = 310,Html_Skill = 10, Css_Skill=10, Nodejs_Skill=10, UX=10, UI=10 )
    
    print("\nAI: ", ai.evaluate())
    print(ai)
    print("\nBackEnd: ", backend.evaluate())
    print(backend)
    print("\nFrontEnd: ", frontend.evaluate())
    print(frontend)
    print("\nFullStack: ", fullstack.evaluate())
    print(fullstack)