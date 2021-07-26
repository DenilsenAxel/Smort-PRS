import Utility_13519059

solution = {}
semester = 1


def findAndDelete(courseDict, delCourse):
    # Fungsi untuk mencari mata kuliah yang merupakan pre-requisite suatu mata kuliah
    # lalu menghapusnya dari list pre-requisite mata kuliah tersebut

    # Looping di setiap mata kuliah
    for course in courseDict:
        # Jika delCourse ada dalam list pre-requisite, hapus dari list
        if(delCourse in courseDict[course]):
            courseDict[course].remove(delCourse)


def topoSort(courseDict):
    # Algoritma Topological Sort untuk memperoleh solusi

    global solution
    global semester
    selectedCourse = []

    # Berhenti jika semua mata kuliah sudah masuk ke dalam himpunan solusi
    if(len(courseDict) == 0):
        return

    # Mencari mata kuliah yang semua pre-requisitenya sudah diambil
    for course in courseDict:
        if(len(courseDict[course]) == 0):
            selectedCourse.append(course)

    # Menghapus mata kuliah tersebut dari list pre-requisite mata kuliah lain
    for course in selectedCourse:
        findAndDelete(courseDict, course)
        courseDict.pop(course)

    # Memasukkan mata kuliah tersebut ke dalam himpunan solusi
    solution.update({semester: selectedCourse})
    semester += 1

    topoSort(courseDict)


def printSolution():
    # Fungsi Utilitas untuk mencetak himpunan solusi yang berisi urutan pengambilan mata kuliah

    global solution
    for semester in solution:
        print("Semester " + Utility_13519059.numToRoman(semester) + "\t: ", end="")
        for course in solution[semester]:
            print(course + " ", end="")
        print()


def run(fileName):
    # Fungsi yang digunakan di GUI untuk memproses solusi sebelum ditampilkan ke GUI

    lineArr = Utility_13519059.readFile(fileName)
    courseDict = Utility_13519059.createCourseDict(lineArr)
    topoSort(courseDict)


def clear():
    # Fungsi untuk meng-clear solusi untuk menunggu input berikutnya dari GUI

    global solution
    global semester
    solution.clear()
    semester = 1


# path = "../test/"
# fileName = input("Masukkan Nama File: ")
# run(path + fileName)
# printSolution()
