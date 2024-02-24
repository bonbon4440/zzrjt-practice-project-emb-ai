from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Stores the results of this function call in "result_1"
        result_1 = sentiment_analyzer('I love working with Python')
        # Checks result_1['label'] because it is a dictionary
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        # Result 2
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        # Result 3
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()