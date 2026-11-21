"""Unit tests for EmotionDetection; Watson responses are mocked."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the output format, dominant emotion and invalid inputs."""

    def test_each_dominant_emotion(self):
        """Confirm that the greatest score determines the emotion."""
        for emotion in ("anger", "disgust", "fear", "joy", "sadness"):
            with self.subTest(emotion=emotion):
                scores = {name: 0.05 for name in (
                    "anger", "disgust", "fear", "joy", "sadness"
                )}
                scores[emotion] = 0.8
                response = Mock(status_code=200)
                response.json.return_value = {
                    "emotionPredictions": [{"emotion": scores}]
                }
                with patch(
                    "EmotionDetection.emotion_detection.requests.post",
                    return_value=response,
                ):
                    result = emotion_detector("Example text")
                self.assertEqual(result["dominant_emotion"], emotion)
                self.assertEqual(result[emotion], 0.8)
                self.assertEqual(len(result), 6)

    def test_blank_input(self):
        """Whitespace-only text must return None scores."""
        result = emotion_detector("  ")
        self.assertTrue(all(value is None for value in result.values()))

    def test_watson_http_400(self):
        """A Watson 400 response must return None scores."""
        response = Mock(status_code=400)
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=response,
        ):
            result = emotion_detector("Bad input")
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()
