import requests
import translators as ts

def translate(text, target):
    """Can translate 1000 chars at a time."""
    langs = {'marathi':'mr', 'hindi':'hi', 'english':'en'}
    translation = ts.translate_text(query_text=text, to_language=langs[target])
    return translation

def manage_long_text(long_text, target):
    i=0
    texts = []
    text = ''
    start=0
    end = len(long_text)+1
    while True:
        i+=1
        index = long_text[start:end].find('.')
        if index ==-1:
            texts.append(text)
            break
        if (len(text) + index)<1000:
            index = index + len(text) + 1
            text+=long_text[start:index+1]
            start=index+1
        else:
            texts.append(text)
            long_text = long_text[start:end]
            text=''
            start=0
            end = len(long_text)+1        
        if i>1000:
            break
    translated_text = ''
    for text in texts:
        translated_text += translate(text, target)
    return translated_text

if __name__=='__main__':
    text = '''India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[25] is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world. Its population grew from 361 million in 1951 to 1.4 billion in 2022. It has a fast-growing economy and a hub for information technology. India is a nuclear-weapon state, which ranks high in military expenditure. It faces the socio-economic challenges of gender inequality, child malnutrition, and rising air pollution levels. The country has been a federal republic since 1950, governed through a democratic parliamentary system. It also has a space programme which includes several planned or completed extraterrestrial missions, which play an increasing role in global culture.'''
    
    translated_text = manage_long_text(text, 'marathi')
    print(len(translated_text))
    print(translated_text)