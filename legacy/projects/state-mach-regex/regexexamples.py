import re
# find all propper nouns in a passage of text
txt = "Little Sally McCallister looked at the spotty kettle in her hands and felt cross. She walked over to the window and reflected on her picturesque surroundings. She had always loved idyllic Plymouth with its muddy, mouldy mountains. It was a place that encouraged her tendency to feel cross. Then she saw something in the distance, or rather someone. It was the figure of Doris Bogtrotter. Doris was an incredible lawyer with squat feet and curvaceous toes."

capitalized_re = r"(?<=[A-z]\s)[A-Z]{1}[A-z]+"
a = re.findall(capitalized_re, txt)
print(a)


# Example 2 - find the first match in a block of text, like CMD-F or CTRL-F

txt = "How much wood could a woodchuck chuck if a woodchuck could chuck wood? As much wood as a woodchuck could chuck, If a woodchuck could chuck wood."
# Here we use lookaheads, which are very similar to lookbehinds
b = re.search(r"(?<=[\s])wood(?=[\s])", txt)
print(b)


# Example 3 - parsing an inconsitently formatted list for emails

txt = "austen@lambdaschool.com,ashton@lambdaschool.com otherperson@lambdaschool.com"
email_ex = r"[\s,-]"
c = re.split(email_ex, txt)
print(c)

# Example 4 - AirBNB redacting emails, phone numbers in messages

txt = "If you have any questions, you can reach me at 555-555-5555!"
phone_ex = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
d = re.sub(phone_ex, "[phone number not shown]", txt)
print(d)