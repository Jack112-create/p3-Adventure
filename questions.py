html_questions = [
    {
        'question': 'What does HTML stand for?:',
        'answers': ['Hyper Text Meta Language', 'Hyper Text Markup Language', 'Hyperlinks Mark-up Language'],
        'correct': 'Hyper Text Markup Language'
    },
    {
        'question': 'Is <img> a HTML element?:',
        'answers': ['Yes', 'No'],
        'correct': 'Yes'
    },
    {
        'question': 'Choose the correct HTML element for the largest heading:',
        'answers': ['<h1>', '<head>', '<h6>'],
        'correct': '<h1>'
    },
    {
        'question': 'What is the correct HTML element for inserting a line break?:',
        'answers': ['<br>', '<break>', '<b>'],
        'correct': '<br>'
    },
    {
        'question': 'What is the correct HTML for adding a font size?:',
        'answers': ['<body style="font-size: 20px;">', '<body style="font: 20px">', '<body style="font-size: 20px">'],
        'correct': '<body style="font-size: 20px;">'
    }
]

css_questions = [
    {
        'question': 'What does CSS stand for?:',
        'answers': ['Cascading Style Sheet', 'Computer Style Sheet', 'Creative Style Sheet'],
        'correct': 'Cascading Style Sheet'
    },
    {
        'question': 'Choose the correct way to link a CSS file to a HTML file:',
        'answers': ['<link rel="stylesheet" href="styles.css">', '<link to="stylesheet"', '<link rel="style.css"'],
        'correct': '<link rel="stylesheet" href="styles.css">'
    },
    {
        'question': 'Which of the following target a div element with an ID of "container":',
        'answers': ['#container{}', '.container{}', 'container{}'],
        'correct': '#container{}'
    },
    {
        'question': 'Which of the following target a div element with a class of "content":',
        'answers': ['.content{}', '#content{}', 'content{}'],
        'correct': '.content{}'
    },
    {
        'question': 'Which of the following are a CSS Preprocessor?:',
        'answers': ['SASS', 'Less', 'Stylus', 'All of the above'],
        'correct': 'All of the above'
    }
]

javascript_questions = [
    {
        'question': 'Which of the following is the syntax to define a function:',
        'answers': ['function myFunction(){}', 'myFunction(){}', 'function{}'],
        'correct': 'function myFunction(){}'
    },
    {
        'question': 'Inside which HTML element do we put the JavaScript?:',
        'answers': ['<script>', '<javascript>', '<js>'],
        'correct': '<script>'
    },
    {
        'question': 'Where is the correct place to insert a javascript file?:',
        'answers': ['<head>', '<body>', 'both the <head> and the <body> section are correct'],
        'correct': 'both the <head> and the <body> section are correct'
    },
    {
        'question': 'What is the correct method to target an element by its ID?:',
        'answers': ['document.getElementById()', 'document.getElementsByClassName()', 'document.getElement()'],
        'correct': 'document.getElementById()'
    },
    {
        'question': 'Select the JavaScript keyword:',
        'answers': ['let', 'const', 'var', 'All of the above'],
        'correct': 'All of the above'
    }
]

python_questions = [
    {
        'question': 'Which of the following is the correct syntax to define a function?:',
        'answers': ['def my_function():', 'function():', 'def my_function()'],
        'correct': 'def my_function():'
    },
    {
        'question':
            """
What will the output be for the code below:

def display_helloworld():
    print('Hello World!')
""",
        'answers': ['Hello World!', 'Nothing', 'Error'],
        'correct': 'Hello World!'
    },
    {
        'question':
            """
What arguments do you need to pass into the function for it to return 2:

def divide_numbers(num1, num2):
    num1 // num2
""",
        'answers': ['10, 5', '3, 1', '18, 6'],
        'correct': '10, 5'
    },
    {
        'question': 'Which one of the following is NOT a Python Arithmetic Operator?:',
        'answers': ['//', '/', '*', '~'],
        'correct': '~'
    },
    {
        'question': 'Which of the following is the correct syntax for creating a list?:',
        'answers': ['[]', '{}', '()', 'All of the above'],
        'correct': '[]'
    }
]
