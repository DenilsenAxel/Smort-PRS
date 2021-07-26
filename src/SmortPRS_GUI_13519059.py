import SmortPRS_13519059
import Utility_13519059
import PySimpleGUI as sg
import os.path

# Pengaturan layout window dalam 2 kolom

file_list_column = [
    [
        sg.Text("Silahkan pilih folder tempat file disimpan!!"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(), ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(30, 20), key="-FILE LIST-"
        )
    ],
]

solution_viewer_column = [
    [sg.Text("Silahkan pilih file .txt yang berisi list mata kuliah dan pre-requisitenya")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Listbox(values=[], enable_events=True,
                size=(150, 20), key="-SOLUTION-")],
    [sg.Button("Clear")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(solution_viewer_column),
    ]
]

window = sg.Window("SmortPRS", layout)

# Array untuk menyimpan list kuliah
output = []

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Nama folder sudah dimasukkan, selanjutnya akan menampilkan list file yang bisa dipilih
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Mengambil list file dari folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".txt"))
        ]
        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":  # Sebuah file dipilih oleh user
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )

            window["-TOUT-"].update(filename)

            SmortPRS_13519059.run(filename)

            # Memasukkan solution ke dalam list output
            for semester in SmortPRS_13519059.solution:
                currSemester = "Semester "
                currSemester += Utility_13519059.numToRoman(semester)
                currSemester += "\t: "
                for course in SmortPRS_13519059.solution[semester]:
                    currSemester += course
                    currSemester += " "
                output.append(currSemester)

            window["-SOLUTION-"].update(output)
        except:
            pass

    elif event == "Clear":  # Akan mereset dict solution dan list output untuk menampung solusi lain
        SmortPRS_13519059.clear()
        output.clear()
        window["-SOLUTION-"].update(output)

window.close()
