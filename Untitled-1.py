from wikipediaapi import Wikipedia

def get_wikipedia_summary(topic):
    wiki=Wikipedia(language='tr', user_agent="wikipediaBot/1.0")
    page=wiki.page(topic)
    if page.exits():
     return page.summary
    else:
     return f" '{topic}' hakkında bir bilgi bulunamadı."
topic=input("Aramak istediğiniz konuyu girin: ")
print(get_wikipedia_summary(topic))