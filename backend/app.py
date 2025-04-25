from flask import Flask, jsonify
from flask_cors import CORS
import grabdata

app = Flask(__name__)
CORS(app)

@app.route("/api/top-artists")
def top_artists():
    try:
        artists = grabdata.search_track(grabdata.sp)
        return jsonify({"artists": artists})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)