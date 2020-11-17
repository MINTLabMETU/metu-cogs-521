# from turkishnlp import detector
import string
from pathlib import Path
import re
from spellchecker import SpellChecker
spell = SpellChecker()
import spacy
nlp = spacy.load('en_core_web_sm')

def correct_spelling(corp):
    sentences = corp.split('. ')
    res = []
    for st in sentences:
        words = st.split()
        for word in words:
            corrected = spell.correction(word)
            words[words.index(word)] = corrected
        res.append(' '.join(words))
    return '. '.join(res)


def remove_punct(corp):
    # remove punctuation other than ones marking sentence boundary
    punctuation = ''.join([i for i in string.punctuation if i not in '.?!'])
    corp = corp.translate(str.maketrans('', '', punctuation))
    #replacing ?,!,... with . to make things easier
    corp = corp.replace("!",".");
    corp = corp.replace("?",".");
    corp = re.sub('\.+', '.', corp)
    return ' '.join(corp.split())

def remove_dates(corp):
    # remove numbers & dates
    corp = re.sub('[0-9]?[0-9][/-][0-9]?[0-9][/-][0-9][0-9][0-9]?[0-9]?', '', corp) #matches dd/dd/dddd, dd/dd/dd, dd-dd-dddd, dd-dd-dd
    corp = re.sub('[0-9]+[,.]?[0-9]+', '', corp)
    corp = re.sub('[0-9].', '', corp)
    corp = re.sub('[0-9]*', '', corp)

    check_str = 'januaryfebruarymarchaprilmayjunejulyaugustseptemberoctoberdecembermondaytuesdaywednesdaythursdayfridaysaturdaysunday'
    sentences = corp.split('. ')
    res = []
    for st in sentences:
        words = st.split()
        new_words = []
        for word in words:
            if len(words) > 0:
                if word.lower() not in check_str: 
                    new_words.append(word)
        res.append(' '.join(new_words))
    return '. '.join(res)

    return corp

def lowercase(corp):
    sentences = corp.split('. ')
    res = []
    for st in sentences:
        words = st.split()
        if len(words) > 0:
            words[0] = words[0].lower()
        res.append(' '.join(words))
    return '. '.join(res)

def dependency_parsing(corp):
    sentences = corp.split('. ')
    res = []
    for st in sentences:
        pt = nlp(st)
        ns = []
        for token in pt:
            ns.append(f'{token.text}')
            ns.append(f'({token.dep_})')
        res.append(' '.join(ns))
    return '. '.join(res)

def main():
    in_dir = Path.cwd() / 'in'
    out_dir = Path.cwd() / 'out'
    out_dir.mkdir(parents=True, exist_ok=True)
    for fn in in_dir.iterdir():
        in_file = open(fn, "r")
        corp = in_file.read()
        in_file.close()
        # corp = remove_punct(corp)
        # corp = remove_dates(corp)
        # corp = lowercase(corp)
        # corp = correct_spelling(corp)
        corp = dependency_parsing(corp)
        out_file = open(str(out_dir / f'{fn.stem}.txt'),'w')
        out_file.write(corp)
        out_file.close()
        
if __name__ == '__main__':
    main()