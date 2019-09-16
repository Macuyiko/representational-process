from lxml import etree
import gensim
import os
import re
from nltk.tokenize import RegexpTokenizer
from gensim.models.doc2vec import TaggedDocument

def get_doc_list(folder_name):
    doc_list = []
    file_list = ['input/'+folder_name+'/'+name for name in os.listdir('input/'+folder_name) if name.endswith('xes')]
    print ('Found %s documents under the dir %s .....'%(len(file_list),folder_name))
    return file_list

def get_tag(el):
    tag = el.tag
    if '}' in tag:
        tag = tag.split('}')[1]
    return tag

def get_trace(el):
    trace = []
    for childelement in el.iterchildren():
        ctag = get_tag(childelement)     
        if (ctag == "event"):
            for grandchildelement in childelement.iterchildren():
                if grandchildelement.get('key') == 'concept:name':
                    event_name = grandchildelement.get('value')
                    trace.append(event_name.replace(' ','').replace('+complete', ''))
    return trace
                

def get_doc_multiple_XES_tagged(foldername, docid_only=False, merge_traces=False):
    file_list = get_doc_list(foldername)
    taggeddocs = []
    loaded = {}
    traces = []
    for fn in file_list:
        loaded[fn] = []
        tree = etree.parse(fn)
        root = tree.getroot()
        for element in root.iter():
            tag = get_tag(element)
            if tag == "trace":
                trace = get_trace(element) #[:3]
                loaded[fn].append(trace)
                if trace not in traces:
                    traces.append(trace)
    for fn, log_traces in loaded.items():
        if merge_traces:
            tags = [str(fn)]
            doc = ' '.join([' '.join(trace) for trace in log_traces])
            td = TaggedDocument(gensim.utils.to_unicode(str.encode(doc)).split(), tags)
            taggeddocs.append(td)
        else:
            trace_index = 0
            for trace in log_traces:
                tags = [str(fn)]
                if not docid_only:
                    #tags += [str(fn) + str(trace_index)]
                    tags += [str(trace_index)]
                td = TaggedDocument(gensim.utils.to_unicode(str.encode(' '.join(trace))).split(), tags)
                taggeddocs.append(td)
                trace_index += 1
    return taggeddocs

def get_trace_names(filename):
    doc_names=[]
    tree = etree.parse('input/'+filename)
    root= tree.getroot()
    for element in root.iter():
        tag= element.tag.split('}')[1]
        if(tag== "trace"):
            for childelement in element.iterchildren():
                ctag= childelement.tag.split('}')[1]
                if(ctag== "string" and childelement.get('key')=='concept:name'):
                        doc_name=childelement.get('value')
                        doc_names.append(doc_name)
                        break
    return doc_names

def get_sentences_XES(filename):
    texts = []
    tree = etree.parse('input/'+filename)
    root= tree.getroot()
    for element in root.iter():
        tag= element.tag.split('}')[1]
        if(tag== "trace"):
            wordslist = []
            tagslist = []
            for childelement in element.iterchildren():
                ctag= childelement.tag.split('}')[1]
                if(ctag== "string" and childelement.get('key')=='concept:name'):
                    doc_name=childelement.get('value')
                elif (ctag=="event"):
                    for grandchildelement in childelement.iterchildren():
                        if(grandchildelement.get('key')=='concept:name'):
                            event_name=grandchildelement.get('value')
                            wordslist.append(event_name.replace(' ',''))
            texts.append(wordslist)
    return texts
