import json
from stanfordcorenlp import StanfordCoreNLP


def read_input_txt(txt_file):
    with open(txt_file, 'r') as txtfile:
        lines = txtfile.readlines()
        text = ""
        for line in lines:
            text = text + line
    return text


nlp_path = ('/home/local/vvaara/projects' +
            '/common-libs/stanford-nlp/stanford-corenlp-full-2018-02-27')

inputfile = "input/fable_test.txt"
outputfile = 'output/fable_jsonout_test.json'

print("   > Setting up core NLP.")
nlp = StanfordCoreNLP(nlp_path, memory='8g')
props = {
    'annotators': 'tokenize,ssplit,pos,depparse',
    'pipelineLanguage': 'en',
    'outputFormat': 'json'
    }

print("   > reading input data: " + inputfile)
sample_list = []

text = read_input_txt(inputfile)

print("   > running annotators: " + props['annotators'])
jsontext = nlp.annotate(text, properties=props)
jsondata = json.loads(jsontext)

print("   > writing json: " + outputfile)
with open(outputfile, 'w') as jsonfile:
    json.dump(jsondata, jsonfile)

nlp.close()

print("   > Done.")
