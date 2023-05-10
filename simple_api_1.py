from flask import Flask


simple_api_1 = Flask("simple_api_1")


@simple_api_1.route("/")
def root():
    return "Simple API 1 Homepage :)", 200

@simple_api_1.route("/health")
def health():
    return "Simple API 1 is OK !", 200

if __name__ == '__main__':
    simple_api_1.run(host='0.0.0.0', port=5001)
