from flask import Flask, render_template, request, redirect

app = Flask(__name__)

budget_entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=budget_entries)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        budget_entries.append({
            'amount': amount,
            'category': category,
            'description': description
        })
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
