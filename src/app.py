from flask import Flask

app = Flask(__name__)


@app.route('/')
def process_data():

    return "HELLO WORLD"


def main():
    pass


if __name__ == '__main__':
    main()
