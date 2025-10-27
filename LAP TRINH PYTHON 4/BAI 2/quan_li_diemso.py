class Student:
    def __init__(self, nam, mat, lit, eng):
        self.name = nam
        self.scores = {
            'Toán': mat,
            'Văn': lit,
            'Anh': eng,
        }

    @classmethod
    def from_string(cls, student_string):
        na, ma, lit, eng = student_string.split(',')
        ma = int(ma)
        lit = int(lit)
        eng = int(eng)
        return cls(na.strip(), ma, lit, eng)

    @staticmethod
    def get_school_info():
        return 'ICANTECH'

    def score_average(self):
        return (self.scores['Toán'] + self.scores['Văn'] + self.scores['Anh']) / 3

    def show_rank(self):
        avg_score = int(self.score_average())
        if avg_score >= 9:
            return 'Giỏi'
        elif avg_score >= 6:
            return 'Khá'
        elif avg_score >= 4:
            return 'Trung bình'
        else:
            return 'Yếu'

    def show_info_student(self):
        print('Học sinh', self.name, 'tại', self.get_school_info(),
              'có thông tin về điểm số như sau:')
        for key in self.scores:
            print(f"Điểm môn {key}: {self.scores[key]}")
        average_return = self.score_average()
        average_return = round(average_return, 2)
        print('Điểm trung bình ba môn:', average_return)
        print('Xếp loại học sinh:', self.show_rank())


student_string = input('Thông tin học sinh: ')
std1 = Student.from_string(student_string)
std1.show_info_student()