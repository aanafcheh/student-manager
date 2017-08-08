from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def student_page():
    # retrieves the student data from the request

    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_firstname = request.form.get("student-name", "")
        new_student_lastname = request.form.get("student-lastname", "")

        new_student = Student(first_name=new_student_firstname, last_name=new_student_lastname,
                              student_id=new_student_id)
        students.append(new_student)

        return redirect(url_for("student_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
