from flask import Flask


simple_api_2 = Flask("simple_api_2")


@simple_api_2.route("/")
def root():
    return "Simple API 2 Homepage :)", 200

@simple_api_2.route("/health")
def health():
    return "Simple API 2 is OK !", 200

if __name__ == '__main__':
    simple_api_2.run(host='0.0.0.0', port=5002)
