from flask import Flask, jsonify

apps = Flask(__name__)


@apps.route("/")
def details():
    return jsonify({"developer_details": {"name": "nduvho", "surname": "mukwevho", "title": "developer"},
                    "work_details": {"work": "freelancer", "experience": "intermediate"},
                    "work-readiness": {"employment": "open to work", "notice period": "30 days"}})


if __name__ == '__main__':
    apps.run(debug=True)
