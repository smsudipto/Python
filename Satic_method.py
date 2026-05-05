class school:
    school_name="BUBT"

    @staticmethod
    def calculate_grade(mark):
        if mark>90:
            return 'A+'
        if mark>=33:
            return 'pass'
        else:
            return 'F'
print(school.calculate_grade(32))

