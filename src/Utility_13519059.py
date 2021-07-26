def readFile(fileName):
    # Fungsi untuk membaca input dari file eksternal

    f_input = open(fileName, "r")
    line_input = f_input.read().splitlines()
    f_input.close()
    return line_input


def createCourseDict(lineArr):
    # Fungsi untuk membuat dictionary mata kuliah beserta list mata kuliah pre-requisitenya
    # Menerima input list of strings dimana tiap elemen list merupakan baris dalam input file .txt

    courseDict = {}

    # Looping di setiap baris
    for line in lineArr:
        courseCount = 0
        courseID = ""
        currCourse = ""
        currPrerequisite = []
        i = 0

        # Parsing string menjadi dictionary mata kuliah
        for i in range(len(line)):
            if(line[i] == ',' or line[i] == '.'):
                if(courseCount > 0):
                    currPrerequisite.append(courseID)
                else:
                    currCourse = courseID
                courseID = ""
                courseCount += 1
            elif(line[i] != ' '):
                courseID += line[i]
            i += 1

        courseDict.update({currCourse: currPrerequisite})

    return courseDict


def numToRoman(num):
    # Fungsi utilitas untuk mengubah angka arab menjadi angka romawi

    val = [10, 9, 5, 4, 1]
    roman_val = ["X", "IX", "V", "IV", "I"]
    ans = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            ans += roman_val[i]
            num -= val[i]
        i += 1
    return ans
