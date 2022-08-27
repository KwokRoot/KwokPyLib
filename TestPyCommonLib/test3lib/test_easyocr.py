import easyocr

reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)  # this needs to run only once to load the model into memory
result = reader.readtext(r"\opt\ocr.png", detail=0)
print(result)



