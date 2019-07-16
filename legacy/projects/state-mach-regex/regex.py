import re

# find all propper nouns in a passage of text
txt = "Little Sally McCallister looked at the spotty kettle in her hands and felt cross. She walked over to the window and reflected on her picturesque surroundings. She had always loved idyllic Plymouth with its muddy, mouldy mountains. It was a place that encouraged her tendency to feel cross. Then she saw something in the distance, or rather someone. It was the figure of Doris Bogtrotter. Doris was an incredible lawyer with squat feet and curvaceous toes."

capitalized_re = r"(?<=[A-z]\s)[A-Z]{1}[A-z]+"
a = re.findall(capitalized_re, txt)
print(a)

