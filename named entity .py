import spacy

nlp = spacy.load("en_core_web_sm")

text= """Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, California in 1976. 
It is one of the world's largest technology companies and produces a range of products, 
including the iPhone, iPad, and MacBook. The company's headquarters is in Cupertino, 
but it has offices and stores worldwide, including in New York City, London, and Tokyo.
"""

doc = nlp(text)

for ent in doc.ents:
    print(f"text: {ent.text}")
    print(f"Label: {ent.label_}")
    print(f"Start: {ent.start} | End: {ent.end}")
    print(f"Root Text: {ent.root.text}")
    print(f"Root Dep: {ent.root.dep_}")
    print(f"Root Head Text: {ent.root.head.text}")
    print(f"Is in the company's headquarters sentence? {ent.sent.text.startswith('The company''s headquarters')}")


print("\nnOrganization:")

for ent in doc.ents:
    if ent.label_ == "ORG":
        print(ent.text)

highlighted_text = text
for ent in doc.ents:
    highlighted_text = highlighted_text.replace(ent.text, f"[{ent.text}]({ent.label_})", 1)

print("\nHIghlighted Test:")
print(highlighted_text)