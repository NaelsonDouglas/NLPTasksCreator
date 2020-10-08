from datetime import datetime
from datetime import timedelta
import spacy
from spacy.matcher import Matcher
import re
import spacy

days = ['sunday', 'monday', 'tuesday' ,'wednesday', 'thursday', 'friday', 'saturday']
recurrencies = ['on', 'on the next','next','on the following','this', 'on this']

class ActivationRules:
        def __init__(self):
                self.nlp = spacy.load('en_core_web_sm')
                self.matcher = Matcher(self.nlp.vocab)
                single_day_pattern = [{'LEMMA': {'IN':recurrencies}},{'LEMMA': {'IN':days},'TAG':'NNP'}]
                self.matcher.add('single_day', None, single_day_pattern)
                self.queued_rules = []

        def is_specific_day(self, date, day_name):
                return date.strftime('%A') == day_name
        def is_sunday(self, date):
                return self.is_specific_day(date, 'sunday')
        def is_monday(self, date):
                return self.is_specific_day(date, 'monday')
        def is_tuesday(self, date):
                return self.is_specific_day(date, 'tuesday')
        def is_wednesday(self, date):
                return self.is_specific_day(date, 'wednesday')
        def is_thursday(self, date):
                return self.is_specific_day(date, 'thursday')
        def is_friday(self, date):
                return self.is_specific_day(date, 'friday')
        def is_saturday(self, date):
                return self.is_specific_day(date, 'saturday')

        def match_text(self,text):
                doc = self.nlp(str.lower(text))
                for token in doc:
                        print('------------')
                        print(token.text)
                        print(token.pos_)
                        print('tag: '+token.tag_)
                        print(token.lemma_)

                matches = self.matcher(doc)
                for match_id, start, end in matches:
                        string_id = self.nlp.vocab.strings[match_id]
                        span = doc[start:end]
                        print('Result:=======================')
                        print(string_id, start, end, span.text)




c = ActivationRules()
c.match_text('Do something on monday')