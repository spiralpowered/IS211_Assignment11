from flask import Flask, render_template, request, redirect

app = Flask(__name__)
todo_list = []

@app.route('/')
def home():
    return render_template('index4.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def add_task():
    todo_item = ()
    task = (request.form['task'],)
    todo_item += task
    email = (request.form['email'],)
    todo_item += email
    priority = (request.form['priority'],)
    todo_item += priority
    if todo_item[0] == "" or todo_item[1] == "":
        return redirect('/')
    else:
        todo_list.append(todo_item)
        print(todo_list)
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run()
