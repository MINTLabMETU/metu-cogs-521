 
# Cogs 520 - Advanced Research on Linguistics in Cognitive Science

Fall 2020, Department of Cognitive Science, METU

## Preliminaries

**Medium**: `odtüclass` for course material, `github` for progressive assignments (a single [repo](https://github.com/foter/metu-cogs-520), students in distinct folders), `googlegroups` for communication

**Requirements**: basic programming skills (preferably in one that's commonly utilized for nlp applications, e.g. python); basic linguistics knowledge (e.g. an introductory course taken before)

**Bootstrapping**:

- **\[python\]** interactive tutorials from [codecademy](https://www.codecademy.com/learn/learn-python) (tutorial is for version 2.x, nearly all knowledge is directly transferable to the current version 3.x), [learnpython](https://www.learnpython.org/), [w3schools](https://www.w3schools.com/python/) and [geeksforgeeks](https://www.geeksforgeeks.org/python-programming-language/python-tutorial/); video lectures from [mitopen](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) and [edx](https://www.edx.org/course/programming-for-everybody-getting-started-with-pyt); guided projects from [coursera](https://www.coursera.org/search?query=python&index=prod_all_products_term_optimization&entityTypeDescription=Rhyme%20Projects) (free for student memberships)

- **\[git\]** guides for git and github [here](https://guides.github.com/), [here](https://try.github.io/) and [here](https://git-scm.com/docs/gittutorial)  

- **\[linguistics and nlp\]** introductory (i.e. first) chapters of *Introduction to theoretical linguistics* (John Lyons) and *Speech and language processing* (Daniel Jurafsky & James Martin); first three chapters of *Foundations of statistical NLP* by Christopher Manning & Hinrich Schütze

**Resources:**

- **\[books\]**
    - **\[linguistics\]** *Introduction to theoretical linguistics* by John Lyons
    - **\[natural language processing (nlp)\]** *Speech and language processing* by Daniel Jurafsky & James Martin; *NLP with python* by Steven Bird et al.; *Foundations of statistical NLP* by Christopher Manning & Hinrich Schütze; *NLP in action* by Hobson Lane et al.
    - **\[machine learning (ml)\]** *ML for text* by Charu Aggarwal; *ML with python cookbook* by Chris Albon
    - **\[python\]** *Learn python the hard way* by Zed Shaw
    - **\[common lisp\]** *ANSI common lisp* by Paul Graham

- **\[lectures\]**
    - **\[common lisp\]** [algorithms for ai and nlp](https://www.uio.no/studier/emner/matnat/ifi/nedlagte-emner/INF4820/index-eng.html) (pick a year, click 'slides' on the left)

- **\[tutorials\]**
    - **\[python\]** text processing from [tutorialspoint](https://www.tutorialspoint.com/python_text_processing/index.htm), [nanyang techonological uni.](https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html) and [geeksforgeeks](https://www.geeksforgeeks.org/text-preprocessing-in-python-set-1/)   

- **\[documentation\]**
    - **\[python\]** [stable version 3.9.0](https://docs.python.org/3/) 
    - **\[common lisp\]** [cliki](https://www.cliki.net/): common lisp wiki; [common lisp foundation](https://www.common-lisp.net/); [lisp-lang](https://lisp-lang.org/)

- **\[guides\]**
    - **\[regular expressions\]** [regxr](https://regexr.com/)
    - **\[annotation\]** PDTP [v. 2.0](https://www.seas.upenn.edu/~pdtb/PDTBAPI/pdtb-annotation-manual.pdf) & [v. 3.0](https://catalog.ldc.upenn.edu/docs/LDC2019T05/PDTB3-Annotation-Manual.pdf); Penn Treebank II style [bracketing guidelines](https://repository.upenn.edu/cgi/viewcontent.cgi?article=2068&context=cis_reports), [addendum](https://www.cis.upenn.edu/~bies/bioie/TBguidelines-addendum.pdf) and [constituent tags](http://surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html)
    - **\[common lisp\]** [vencouver island uni.](http://www.csci.viu.ca/~wesselsd/courses/csci330/code/lisp/)

- **\[data\]**
    - **\[multi-language\]** [LDC](https://www.ldc.upenn.edu/): Linguistic Data Consortium; [google n-gram](https://storage.googleapis.com/books/ngrams/books/datasetsv3.html); [TalkBank](https://www.talkbank.org/); [CHILDES](https://childes.talkbank.org/); a list of multi-lingual semantic networks [here](https://wordnet.princeton.edu/related-projects)
    - **\[turkish\]** METU Turkish Corpus (provided upon request); Turkish Discourse Bank (provided upon request); [TUD](https://www.tnc.org.tr/tr/): Türkçe Ulusal Derlemi; [tscorpus](https://tscorpus.com/); some other Turkish datasets are listed [here](http://tools.nlp.itu.edu.tr/Datasets)
    - **\[english\]** [CoRD](http://www.helsinki.fi/varieng/CoRD/index.html): Corpus Resource Database; [BNC](http://www.natcorp.ox.ac.uk/): British National Corpus; [Brown Corpus](http://icame.uib.no/brown/bcm.html); [Coca](http://icame.uib.no/brown/bcm.html): Corpus of Contemporary American English; [WordNet](https://wordnet.princeton.edu/); [FrameNet](https://framenet.icsi.berkeley.edu/fndrupal/); [PDTP](https://www.seas.upenn.edu/~pdtb/index.shtml): Penn Discourse Treebank; some other English corpora listed [here](https://www.english-corpora.org/)

- **\[libraries & tools\]**
    - **\[python\]** [nltk](https://www.nltk.org/) (natural language toolkit); [numpy](https://numpy.org/)  (scientific computing); [scikit-learn](https://scikit-learn.org/stable/) (ml in python); [pytorch](https://pytorch.org/) (ml); [pandas](https://pandas.pydata.org/) (data analysis); [keras](https://keras.io/) (deep learning); [matplotlib](https://matplotlib.org/) (visualization); [bokeh](https://bokeh.org/)  (visualization); [networkx](https://networkx.org/) (network analysis); [requests](https://requests.readthedocs.io/en/master/) (fetching internet resources); [urllib](https://docs.python.org/3/howto/urllib2.html) (fetching internet resources); [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/) (html parsing)
    - **\[common lisp\]** cl-nlp: nlp for common lisp [1](https://www.nicklevine.org/els2013/vsevolod-domkin-paper.pdf), [2](https://github.com/kraison/cl-nlp) & [3](https://github.com/vseloved/cl-nlp); [nlp in common lisp](https://www.cliki.net/Natural%20Language%20Processing)
    - **\[nlp\]** [Standford NLP](https://nlp.stanford.edu/) for English; [ITU NLP Pipeline](http://tools.nlp.itu.edu.tr/) for Turkish (and a Python wrapper [here](https://github.com/ferittuncer/ITU-Turkish-NLP-Pipeline-Caller)); [Zemberek NLP](https://github.com/ahmetaa/zemberek-nlp) for Turkish (and two Python wrappers [here](https://github.com/ozturkberkay/Zemberek-Python-Examples) and [here](https://github.com/kemalcanbora/zemberek_parser)); [TRmorph](http://coltekin.net/cagri/trmorph/) for analyzing Turkish morphology
    - **\[ml\]** [weka](https://www.cs.waikato.ac.nz/ml/weka/); [tensorflow](https://www.tensorflow.org/); [openAI](https://openai.com/)
    - **\[visualization\]** [gephi](https://gephi.org/) (graph visualization and analysis); [flourish](https://texample.net/tikz/); [d3](https://d3js.org/); [observable](https://observablehq.com/); [R graph gallery](https://www.r-graph-gallery.com/index.html) 

- **\[development environments\]**
    - **\[text editors\]** [visual studio code](https://code.visualstudio.com/); [atom](https://atom.io/); [sublime text](https://www.sublimetext.com/)
    - **\[python\]** [pycharm](https://www.jetbrains.com/pycharm/); [spyder](https://www.spyder-ide.org/); [anaconda](https://www.anaconda.com/products/individual)
    - **\[online editors\]** [jupyter](https://jupyter.org/); [datalore](https://datalore.jetbrains.com/); [azure](https://notebooks.azure.com/); [kaggle](https://www.kaggle.com/); [cocalc](https://cocalc.com/index.html)

- **\[communities\]**
    - **\[programming\]** [stackoverflow](https://stackoverflow.com/)
    - **\[linguistics\]** [stackexchange linguistics](https://linguistics.stackexchange.com/)
    - **\[data science\]** [stackexchange datascience](https://datascience.stackexchange.com/)

- **\[misc\]**
    - [pythex](https://pythex.org/): check your python/re expressions if working   

## Program

### Week 3 - Preprocessing

This week we will get familiar with how to approach any kind of text as data and common requirements for getting that data ready for further analysis, including (but not limited to) stripping, extraction, spelling and diacritic correction, elimination and normalization (case, number, proper names etc.). At this level the aim is to obtain a standardized chunk of information purged from both noise and irrelevant bits that will most efficiently yield itself to formal analysis, congruous with the problem in mind.

- **\[sync.\]** online tutorial, part I 
    - **\[programming language\]** Python
    - **\[input language\]** Turkish
    - **\[tasks\]** (i) read from a text file, (ii) store data in intermediate structures, (iii) traverse chunks of input, (iv) utilize third party processes (e.g. ITU NLP pipeline) and (v) simplistic approaches (for the sake of demonstration) to certain preprocessing problems such as proper name recognition and stop word elimination, and (vi) finally write the processed data to an output file 

- **\[async.\]** on language processing with python (ch. 1, Bird et al.); on preprocessing with python (ch. 3, Bird et al.)

- **\[supplementary\]** lecture slides; content included in the preliminaries, but not explicitly mentioned in the program

- **\[exercises\]** you can take a look at ch. 3.12 from Bird et al.

- **\[assignments\]** part I
    - **\[programming language\]** any
    - **\[input language\]** any
    - **\[tasks\]** code a basic preprocesser with a similar scope examplified in the online tutorial, which utilizes third party processes (e.g. Stanford NLP pipeline) when necessary

### Week 4 - Tagging

After the language data is purged from noise (both as disturbance and redundancy) various layers of linguistic analysis might be necessary, such as part of speech tagging, morphological analysis and disambiguation, mapping syntactic dependencies, recognizing multi word expressions and/or annotating discourse relations.   

- **\[sync.\]** online tutorial, part II 
    - **\[programming language\]** Python
    - **\[input language\]** Turkish
    - **\[tasks\]** (i) analyze the output of part I morphologically and (ii) output the results where the associated linguistic analysis is encoded explicitly.

- **\[async.\]** on word level analysis (ch. 3, Jurafsky & Martin); on syntactic analysis, (ch. 12, Jurafsky & Martin); on tagged data (ch. 5.2, Bird et al. and ch. 4.3, Manning & Schütze)

- **\[supplementary\]** lecture slides; on in-depth parsing see ch.s 13 & 14 from Jurafsky & Martin; for parsing in python see ch. 8 from Bird et al.; content included in the preliminaries, but not explicitly mentioned in the program

- **\[exercises\]** you can take a look at ch. 5 from Bird et al.

- **\[assignments\]** part II
    - **\[programming language\]** any
    - **\[input language\]** same as part I
    - **\[tasks\]** (i) apply dependency parsing on the output of part II and (ii) output the results where dependency relations are encoded explicitly.

### Week 5 - Structuring

Processing data (be it textual or otherwise) means structuring it according to a predefined agenda, and such a structure is usually manifold. In order to deal with a complicated data structure efficiently various aspects of parsing (e.g. delimiters, tokenization and segmentation) and data storage (e.g. flat file databases, data structures and database formats) becomes relevant.

- **\[sync.\]** online tutorial, part III 
    - **\[programming language\]** Python
    - **\[input language\]** Turkish
    - **\[tasks\]** (i) read the output of part II into a dictionary and (ii) export the dictionary to a csv file while preserving the original structure of the data

- **\[async.\]** on tokenization and segmentation (ch. 4.2, Manning & Schütze); on storing structured data in python (ch. 5.3, Steven Bird et al.)

- **\[supplementary\]** lecture slides; content included in the preliminaries, but not explicitly mentioned in the program

- **\[exercises\]** TBA

- **\[assignments\]** part III
    - **\[programming language\]** any
    - **\[input language\]** English
    - **\[tasks\]** (i) read the output of part II into an appropriate data structure and (ii) export the dictionary to a json file while preserving the original structure of the data

### Week 6 - Analysis

Testing hypotheses on structured data requires means of controlled access, formal analysis and representation of results. This week we will look at search by regular expressions, explore implicit statistical properties via frequencies, collocative relations, n-grams and moving windows and consider basic visualization techniques.

- **\[sync.\]** online tutorial, part IV
    - **\[programming language\]** Python
    - **\[input language\]** Turkish
    - **\[tasks\]** TBA

- **\[async.\]** on regular expressions, (ch. 2.1, Jurafsky & Martin); on collocations (ch. 5, Manning & Schütze); on n-gram models (ch.s 4.1-4.5, Jurafsky & Martin; ch. 6, Manning & Schütze) 

- **\[supplementary\]** lecture slides; for data management in python see ch. 11 from Steven Bird et al.; content included in the preliminaries, but not explicitly mentioned in the program

- **\[exercises\]**  you can take a look at ch. 6.6 from Manning & Schütze

- **\[assignments\]** part IV
    - **\[programming language\]** any
    - **\[input language\]** English
    - **\[tasks\]** TBA

### Week 7 - Modeling

Now it is time moving on to the project proposals, defining central problems, engineering hypotheses and choosing appropriate data sources. 

- **\[sync.\]** in-class discussion on project proposals

- **\[async.\]** accesing text corpora and lexical resources (ch. 2, Steven Bird et al.)

- **\[supplementary\]** *Markup systems and the furue of scholarly text processing* by Coombs et al. (1987); *An overview of empirical NLP* by Brill & Mooney (1997); *Data preprocessing and intelligent data analysis* by Famili et al. (1997); *Data preprocessing for supervised learning* by Kotsiantis et al. (2006); *Overview and semantic issues of text mining* by Stavrianou et al. (2007)

- **\[exercises\]** you can take a look at ch. 4.5. from Manning & Schütze

- **\[assignments\]** none

### Other (optional)

When you need data in the wild one way of getting it is scraping from web.

- **\[sync.\]** online tutorial, part V
    - **\[programming language\]** Python
    - **\[tasks\]** scrape from X (TBA, with regular urls) where X is a well-structured and preferably small web page: (i) fetch html sources, (ii) parse them, (iii) download coexisting files (e.g. images) and (iv) generate a database from scratch 

- **\[async.\]** TBA

- **\[supplementary\]** TBA

- **\[exercises\]** TBA

- **\[assignments\]** part V
    - **\[programming language\]** any
    - **\[tasks\]** code a periodic scraper that fetches from Wikipedia main-page everyday at 10:00 am

## Notes

Semantics and advanced modeling approaches are left out of scope; but project specific guidance will be provided if necessary. For weekly tutorials, exercises and assignments additional resources will be announced if necessary. Chapter numbers are taken from Lyons ed. 1, Jurafsky & Martin ed. 2, Bird ed. 1, and Manning & Schütze ed. 1.