"""Flask web application for IBM Watson emotion detection."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Display the page for entering text to analyze."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze submitted text and show the dominant emotion."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text_to_analyze)
    except (RequestException, KeyError, ValueError, IndexError):
        return "Emotion detection service is unavailable. Please try again.", 503

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
