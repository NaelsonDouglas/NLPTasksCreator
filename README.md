# NLPTasksCreator
Creates calendar tasks using Natural Language

# How to run locally
The system is docker-compose based
 * Just call docker-compose up
 * Then go to your browser and access 0.0.0.0:3000
 
 # Usage
 * The system atends to calls like 'do XXX on the next friday', 'on thursday, walk the dog', 'watch TV tomorrow moorning', 'for the next 10 days, sleep well'
 
 # Patterns
 The system uses [rule-base-matching](https://spacy.io/usage/rule-based-matching#matcher)
 The current patterns on the system are:
```python
days = ['sunday', 'monday', 'tuesday' ,'wednesday', 'thursday', 'friday', 'saturday']
recurrencies = ['on', 'on the next','next','on the following','this', 'on this']
range_recurrencies = ['next','for the next', 'on the next','on the following',]

single_day_pattern = [{'ORTH': {'IN':recurrencies}},{'LEMMA': {'IN':days}}] #NN or NNP
next_n_days_pattern = [{'ORTH':{'IN':range_recurrencies}},{'POS':'NUM'},{'ORTH': 'days'}] #NN or NNP
tomorrow_pattern = [{'ORTH':'tomorrow'}]
in_n_days_pattern = [{'ORTH':'in'},{'POS':'NUM'},{'ORTH':'days'}]
```
