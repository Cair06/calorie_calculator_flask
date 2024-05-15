# Calorie Calculator Flask

A lightweight web application for calculating daily calorie needs based on weight, height, age, gender, activity level, and fitness goals. Built using Flask.

## Features

- Calculate daily calorie needs for weight loss, weight gain, or weight maintenance.
- User-friendly interface with input fields for weight, height, age, gender, activity level, and fitness goals.
- Real-time results displayed directly on the page.

## Screenshot

![Calorie Calculator Screenshot](static/mini_background) <!-- Replace this URL with the actual URL of your image -->

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/calorie_calculator_flask.git
    cd calorie_calculator_flask
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    flask run
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter your weight, height, age, select your gender, activity level, and goal.
3. Click the "Calculate" button to see your daily calorie needs.

## Code Structure

- `app.py`: Main Flask application.
- `templates/index.html`: HTML template for the web interface.
- `static/`: Directory for static files (CSS, images, etc.).

## Background Image

To set a background image for the web form, place your image in the `static` directory and update the `index.html` file:

```html
<style>
    body {
        background-image: url('/static/your-background-image.png'); /* Update the image name */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
</style>
