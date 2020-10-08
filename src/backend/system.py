from datetime import datetime
from datetime import timedelta
from rules import ActivationRules

class System:
        def __init__(self):
                self.update_current_date()
                self.entries = []
                self.rules = ActivationRules()

        def update_current_date(self):
                self.now = datetime.now().date()

        def generate_span_to_n_days(self,n_days=7):
                self.update_current_date()
                self.entries = []
                filtered_days = n_days
                if filtered_days > 7200: #the maximum limit is 10 years
                        filtered_days = 7200
                for i in range(0,n_days):
                        plus_day = timedelta(days=i)
                        pivot = self.now+plus_day
                        cell = {}
                        cell['date'] = str(pivot)
                        self.entries.append(cell)
                        print(pivot)
                return self.entries

c = System()
c.generate_span_to_n_days()
print('aaa')