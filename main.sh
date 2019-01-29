# Some of the texts are too long for the default values on the server through the API. Need to start the server independently then ...
source venv/bin/activate
java -mx4g -cp "/home/local/vvaara/projects/common-libs/stanford-nlp/stanford-corenlp-full-2018-02-27/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 8050 -timeout 30000 -maxCharLength 200000 -memory "8g" &
python main.py
deactivate
