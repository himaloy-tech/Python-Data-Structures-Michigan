text = "X-DSPAM-Confidence:0.8475"
index = text.find(':')
extracted_text = text[index+1:]
print(float(extracted_text))