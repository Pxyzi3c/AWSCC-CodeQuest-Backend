from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/contact')
def contact():
    return 'You can contact me at @harvypontillas.developer@gmail.com'

@app.route('/user/<username>')
def user_profile(username):
    return f'Welcome aboard, {username}!'


if __name__ == '__main__':
    app.run()

########################## [LEARN] DECORATORS ##########################
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code to be executed before the original function
        result = original_function(*args, **kwargs)
        # Code to be executed after the original function
        return result
    return wrapper_function

@decorator_function
def some_function():
    # Original function code
    pass
########################## [LEARN] DECORATORS ##########################

########################## [PRACTICE] DECORATORS ##########################
def timing_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time();
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"{original_function.__name__} ran in {end_time - start_time} secs")
        return result
    return wrapper_function

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()
########################## [PRACTICE] DECORATORS ##########################