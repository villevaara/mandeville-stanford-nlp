import json
from stanfordcorenlp import StanfordCoreNLP
import os
import unicodedata
from lib.common import create_dir_if_not_exists


def read_input_txt(txt_file):
    with open(txt_file, 'r') as txtfile:
        lines = txtfile.readlines()
        text = ""
        for line in lines:
            text = text + line
    text = unicodedata.normalize("NFKD", text)
    return text


def get_inputfiles(inputdir):
    fnames = os.listdir(inputdir)
    fpaths = []
    for fname in fnames:
        fpaths.append(inputdir + fname)
    return fpaths


def get_output_json_filepath(input_filename, outputdir):
    if outputdir[-1] != "/":
        outputdir = outputdir + "/"
    namepart = input_filename.split("/")[-1].split(".")[0]
    fpath = outputdir + namepart + "_result.json"
    return fpath


def process_file(inputfile, outputdir, nlp, props):
    print("   > reading input data: " + inputfile)
    text = read_input_txt(inputfile)

    print("   > running annotators: " + props['annotators'])
    jsontext = nlp.annotate(text, properties=props)
    jsondata = json.loads(jsontext)

    outputfile = get_output_json_filepath(inputfile, outputdir)
    print("   > writing json: " + outputfile)
    with open(outputfile, 'w') as jsonfile:
        json.dump(jsondata, jsonfile)
    print()


nlp_path = ('/home/local/vvaara/projects' +
            '/common-libs/stanford-nlp/stanford-corenlp-full-2018-02-27')

# this one points to the dataset
datasetdir = "fb2"
inputdir = 'input/' + datasetdir + "/"
outputdir = 'output/' + datasetdir + "/"
for path in [inputdir, outputdir]:
    create_dir_if_not_exists(path)

inputfiles = get_inputfiles(inputdir)

print("   > Setting up core NLP.")
# nlp = StanfordCoreNLP(nlp_path, memory='8g')
nlp = StanfordCoreNLP('http://localhost', port=8050)
props = {
    'annotators': 'tokenize,ssplit,pos,depparse',
    'pipelineLanguage': 'en',
    'outputFormat': 'json'
    }

for file in inputfiles:
    process_file(file, outputdir, nlp, props)

nlp.close()
print("   > Done.")
