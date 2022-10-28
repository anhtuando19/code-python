# khởi tạo class
class Student:
    def __init__(self, name, age, toan, van):
        self.name = name
        self.age = age
        self.toan = toan
        self.van = van
        self.teacher = "Khanh Linh"

    def diem_TB(self):  # hàm tính điểm trung bình
        diem_tb = (self.toan + self.van)/2
        return diem_tb

    def infor(self):  # hàm in ra infor
        ave = str(self.diem_TB())
        print("Tên: " + self.name)
        print("Tuổi: " + str(self.age))
        print("Điểm toán: " + str(self.toan))
        print("Điểm văn: " + str(self.van))
        print("Điểm TB: " + ave)
        print("\n")


# khởi tạo đối tượng
students = []
s1 = Student("Tuấn", 19, 9, 10)  # học sinh 1
s2 = Student("Linh", 19, 10, 10)  # học sinh 2
s3 = Student("Hoàng", 19, 6, 7)  # học sinh 3

# thêm đối tượng vào list
students.append(s1)
students.append(s2)
students.append(s3)

# duyệt mảng là gọi hàm infor ra
for i in range(len(students)):
    students[i].infor()
