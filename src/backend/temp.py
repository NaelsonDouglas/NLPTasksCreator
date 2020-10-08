import spacy
from spacy.matcher import Matcher
import spacy
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

text = 'do Something on sundays'
doc = nlp(str.lower(text))
days = ['sunday', 'monday', 'tuesday' ,'wednesday', 'thursday', 'friday', 'saturday']

def on_match(self, matcher, doc, id, matches):
        print('ok')
        for m in matches:
                matched_text = doc[m[1]:m[2]]
                print(matched_text)

#pattern = [{"ORTH": {"IN": ["sundays", "something"]}}]
#pattern = [{"ORTH": {'IN':['something','sundays']}}]
pattern = [{'TEXT': {'REGEX': '\w*'}},{"LEMMA": {'IN':days}}]

matcher.add('axxxx', None, pattern)
matches = matcher(doc)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
for token in doc:
        print('------------')
        print(token.text)
        print(token.pos_)
        print(token.lemma_)

