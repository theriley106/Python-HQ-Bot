from rake_nltk import Rake
r = Rake()

def returnKeywords(question):
	r.extract_keywords_from_text(question)
	return r.extract_keywords_from_text()
