from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    weight = None
    height = None
    age = None
    gender = 'male'
    activity_level = '1.2'
    goal = 'lose'
    
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            age = int(request.form['age'])
            gender = request.form['gender']
            activity_level = request.form['activity_level']
            goal = request.form['goal']

            if gender == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            tdee = bmr * float(activity_level)
            
            if goal == 'lose':
                tdee -= 500
            elif goal == 'gain':
                tdee += 500

            result = f"Your Daily Calorie Needs: {round(tdee)} calories"
        except ValueError:
            result = "Please ensure all fields are filled correctly."

    return render_template('index.html', result=result, weight=weight, height=height, age=age, gender=gender, activity_level=activity_level, goal=goal)

if __name__ == '__main__':
    app.run(debug=True)
