import copy

from flask import Flask, render_template

from geometric import Parallelogram
from mydate import MyDate

app = Flask(__name__)


@app.route('/')
def index():
    # List of lists description structure
    # list = []
    # res = [[]]
    # res = [[list1], [list2], [listn]]

    # Defining of time and date class
    results = [[]]
    result1 = []
    custom_date = MyDate(30, 12, 1992)
    custom_date2 = MyDate(31, 12, 1992)
    custom_date3 = MyDate(31, 12, 1992)

    custom_date.day = 31
    # print to console on the server
    print(custom_date.day)
    result1.append(custom_date)

    custom_date.add_day()
    # print to console on the server
    print(custom_date)
    result1.append(custom_date)

    result1.append(str(custom_date2.compare_dates(custom_date3)))
    result1.append(str(custom_date.compare_dates(custom_date2)))

    # Adding all results into general list
    results.append(result1)

    # Defining of Parallelogram figure and printing results
    result2 = []

    # Creating objects
    p1 = Parallelogram(2, 4, 6)
    p2 = copy.deepcopy(p1)
    p3 = Parallelogram(7, 8, 9)

    # print to console on the server
    print(p1)
    print(p2)
    print(p3)

    # Prepare data to output
    result2.append(p1)
    result2.append(p2)
    result2.append(p3)

    # print to console on the server
    print("Perimeter p1 = ", p1.get_perimeter(), "Area p1 = ", p1.get_area())
    print("Perimeter p3 = ", p3.get_perimeter(), "Area p3 = ", p3.get_area())

    # Prepare data to output
    result2.append("Perimeter p1 = " + str(p1.get_perimeter()) + "Area p1 = " + str(p1.get_area()))
    result2.append("Perimeter p3 = " + str(p3.get_perimeter()) + "Area p3 = " + str(p3.get_area()))

    # print to console on the server
    print("p1 is equal to p2 ", p1.is_equal(p2))
    print("p1 is equal to p3 ", p1.is_equal(p3))

    # Prepare data to output
    result2.append("p1 is equal to p2 " + str(p1.is_equal(p2)))
    result2.append("p1 is equal to p3 " + str(p1.is_equal(p3)))

    results.append(result2)

    # Call of Jinja framework (Work)
    # !!! Template must be in "templates" directory !!!
    return render_template("base.html", results=results)


if __name__ == '__main__':
    app.run(debug=True)
