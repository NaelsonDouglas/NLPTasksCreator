from datetime import datetime
from datetime import timedelta
from datetime import date
import spacy
from spacy.matcher import Matcher
import re
import spacy
import json

days = ['sunday', 'monday', 'tuesday' ,'wednesday', 'thursday', 'friday', 'saturday']
recurrencies = ['on', 'on the next','next','on the following','this', 'on this']
range_recurrencies = ['for the next', 'on the next','on the following',]

class System:
        def __init__(self):
                self.update_current_date()
                self.entries = []
                self.nlp = spacy.load('en_core_web_sm')
                self.matcher = Matcher(self.nlp.vocab)
                single_day_pattern = [{'LEMMA': {'IN':recurrencies}},{'LEMMA': {'IN':days},'TAG':'NN'}] #NN or NNP
                next_n_days_pattern = [{'ORTH':'next'},{'POS':'NUM'},{'ORTH': 'days'}] #NN or NNP
                tomorrow_pattern = [{'ORTH':'tomorrow'}]
                in_n_days_pattern = [{'ORTH':'in'},{'POS':'NUM'},{'ORTH':'days'}]
                self.matcher.add('single_day', None, single_day_pattern)
                self.matcher.add('next_n_days', None, next_n_days_pattern)
                self.matcher.add('tomorrow', None, tomorrow_pattern)
                self.matcher.add('in_n_days', None, in_n_days_pattern)
                self.generate_span_to_n_days('')
                self.queued_rules = []


        def update_current_date(self):
                self.now = datetime.now().date()

        def is_specific_day(self, date, day_name):
                waited = str.lower(date.strftime('%A'))
                print('waited: {} input: {}'.format(waited,day_name))
                return waited == day_name
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
                # for token in doc:
                #         print('------------')
                #         print(token.text)
                #         print(token.pos_)
                #         print('tag: '+token.tag_)
                #         print(token.lemma_)

                matches = self.matcher(doc)
                for token in doc:
                        print('Text: {}. Pos: {}, Lemma: {} '.format(token.text,token.pos_,token.lemma_))
                for match_id, start, end in matches:
                        string_id = self.nlp.vocab.strings[match_id]
                        if string_id == 'single_day':
                                self.single_day(text)
                        elif string_id == 'next_n_days':
                                self.next_n_days(text)
                        elif string_id == 'tomorrow':
                                self.tomorrow(text)
                        elif string_id == 'in_n_days':
                                self.in_n_days(text)

                        span = doc[start:end]
                        print('Result:=======================')
                        self.single_day(text)
                        print(string_id, start, end, span.text)
        def in_n_days(self,text):
                doc = self.nlp(text)
                amount = 0
                for token in doc:
                        if token.pos_ == 'NUM':
                                amount = int(token.text)
                if self.entries[amount]['notes'] == None:
                        self.entries[amount]['notes'] = [str(doc)+'---']
                else:
                        self.entries[amount]['notes'].append(str(doc)+'---')
        def next_n_days(self,text):
                doc = self.nlp(text)
                amount = 0
                for token in doc:
                        if token.pos_ == 'NUM':
                                amount = int(token.text)
                for d in range(0,amount):
                        if self.entries[d]['notes'] == None:
                                self.entries[d]['notes'] = [str(doc)+'---']
                        else:
                                self.entries[d]['notes'].append(str(doc)+'---')
        def tomorrow(self, text):
                if self.entries[1]['notes'] == None:
                        self.entries[1]['notes'] = [text+'---']
                else:
                        self.entries[1]['notes'].append(text+'---')

        def single_day(self,text):
                doc = self.nlp(text)
                day_pivot = self.now
                for token in doc:
                        print('token: '+token.text)
                        x = None
                        try:
                                x = days.index(token.lemma_)
                        except:
                                pass
                        day = ''
                        if x != None:
                                day = days[x]
                                days_diff = 0
                                while not self.is_specific_day(day_pivot,day):
                                        days_diff = days_diff + 1
                                        day_pivot = day_pivot+timedelta(days=1)
                                        print(day_pivot)
                                        print(day)
                                if self.entries[days_diff]['notes'] == None:
                                        self.entries[days_diff]['notes'] = [str(doc)+'---']
                                        return True
                                else:
                                        self.entries[days_diff]['notes'].append(str(doc)+'---')
                                        return True
                                print('~~~~~~~~~~~~~~~')
                                print(days_diff)


        def generate_span_to_n_days(self,text,n_days=365):
                self.update_current_date()
                #self.entries = []
                filtered_days = n_days
                if filtered_days > 365:
                        filtered_days = 365
                for i in range(0,n_days):
                        plus_day = timedelta(days=i)
                        pivot = self.now+plus_day
                        cell = {}
                        cell['date'] = str(pivot)
                        cell['day'] = str(pivot.strftime('%A'))
                        cell['notes'] = []
                        self.entries.append(cell)
                        #print(pivot)
                self.match_text(text)
                return self.entries
        def get(self):
                return self.entries
        def get_data(self):
                s = []
                for dt in self.entries:
                        s.append(str(dt))
                return s
