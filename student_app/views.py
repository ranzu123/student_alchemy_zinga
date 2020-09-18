from flask import render_template,request,redirect
from student_app import app,db
from student_app.models import Student

@app.route('/')
@app.route('/list')
def list():
    return  render_template('list.html', students=Student.query.all())

@app.route('/add')
def add_get():
    return render_template('add.html')


@app.route('/add', methods=["POST"])
def add_post():
    student_data={

        "name"       :  request.form["txtName"],
        "grade"      :  request.form["txtGrade"],
        "faculty"    :  request.form["txtFaculty"],
        "section"    :  request.form["btnSection"],
        "roll_no"    :  request.form["txtRoll"],
        "age"        :  request.form["txtAge"],
        "gender"     :  request.form["btnGender"],
        "address"    :  request.form["txtAddress"],
        "parent_name":  request.form["txtParent"]
    }
    student = Student(**student_data)
    db.session.add(student)
    db.session.commit()

    return redirect('/list')


@app.route('/edit/<id_>')
def edit_get(id_):
    student = Student.query.filter_by(id_=id_).first()
    print(student.section)
    print(student.gender)
    return render_template('edit.html',
                            student=student,
                            section=student.section,
                            gender=student.gender)




@app.route('/edit', methods=["POST"])
def edit_post():
    id_=int(request.form["id_"])
    update_data={

        "name"       :  request.form["txtName"],
        "grade"      :  request.form["txtGrade"],
        "faculty"    :  request.form["txtFaculty"],
        "section"    :  request.form["btnSection"],
        "roll_no"    :  request.form["txtRoll"],
        "age"        :  request.form["txtAge"],
        "gender"     :  request.form["btnGender"],
        "address"    :  request.form["txtAddress"],
        "parent_name":  request.form["txtParent"]
    }
    db.session.query(Student).filter_by(id_=id_).update(update_data)
    db.session.commit()

    return redirect('/list')


@app.route('/delete/<id_>')
def delete_get(id_):
    
    student = Student.query.filter_by(id_=id_).delete()
    db.session.commit()

    return redirect('/list')