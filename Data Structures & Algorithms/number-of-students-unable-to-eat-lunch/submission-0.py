class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a = True
        counter = 0
        while a == True:
            if (len(students) == 0):
                return(0)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
            elif counter == len(students):
                print(counter)
                return(len(students))
            else:
                students.append(students.pop(0))
                print(students)
                counter+=1 