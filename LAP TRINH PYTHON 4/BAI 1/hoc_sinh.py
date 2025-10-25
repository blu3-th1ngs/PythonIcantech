class Student:
    name = ''
    scores = {}

    def score_average(std):
        return (std.scores['Toán'] + std.scores['Lí'] + std.scores['Hóa']) / 3

    def show_rank(std):
        avg_score = int(std.score_average())
        if avg_score >= 9:
            return 'Giỏi'
        elif avg_score >= 6:
            return 'Khá'
        elif avg_score >= 4:
            return 'Trung bình'
        else:
            return 'Yếu'

    def max_score(std):
        highest_subject = max(std.scores, key=std.scores.get)
        highest_value = std.scores[highest_subject]
        return highest_subject, highest_value

    def show_info_student(std):
        print('Họ tên học sinh:', std.name)
        for key in std.scores:
            print(f'Điểm môn {key}: {std.scores[key]}')
        average_return = round(std.score_average(), 2)
        print('Điểm trung bình ba môn:', average_return)
        print('Học sinh xếp loại:', std.show_rank())
        subject, score = std.max_score()
        print(f'Môn có điểm cao nhất: {subject} ({score})')

std = Student()
std.name = 'Vũ Trần Minh Thuyết'
std.scores = {
    'Toán': 10,
    'Lí': 10,
    'Hóa': 9.75
}
std.show_info_student()

std = Student()
std.name = 'Nguyễn Thế Doanh'
std.scores = {
    'Toán': 5,
    'Lí': 6.5,
    'Hóa': 7
}
std.show_info_student()
