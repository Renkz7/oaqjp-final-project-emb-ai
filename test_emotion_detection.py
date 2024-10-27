def test_sentiment(self):
    result_1 = sentiment_analyzer('I am glad this happened')
    self.assertEqual(result_1['label'], 'joy')
    
    result_2 = sentiment_analyzer('I am really mad about this')
    self.assertEqual(result_2['label'], 'anger')
    
    result_3 = sentiment_analyzer('I feel disgusted just hearing about this')
    self.assertEqual(result_3['label'], 'disgust')

    result_3 = sentiment_analyzer('I am so sad about this')
    self.assertEqual(result_4['label'], 'sadness')

    result_3 = sentiment_analyzer('I am really afraid that this will happen	')
    self.assertEqual(result_5['label'], 'fear')