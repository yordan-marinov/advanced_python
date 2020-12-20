class Programmer:

    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, curse_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {curse_name}"

        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed:

            if new_language != self.language:
                old_language = self.language
                self.language = new_language

                return f"{self.name} switched from " \
                       f"{old_language} to {self.language}"

            return f"{self.name} already knows {new_language}"

        return f"{self.name} needs " \
               f"{skills_needed - self.skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
