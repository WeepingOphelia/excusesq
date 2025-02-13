import requests
import random

datamuse = "https://api.datamuse.com/words?"
affix = "lc=my&rc=is&ml=hovercraft&pos=n"


def api_req(prefix, affix):
    try:
        response = requests.get(prefix + affix)
    
        if response.status_code == 200:
            words = response.json()
            weights = [x["score"] for x in words]
            random.seed()
            rand_list = random.choices(words, weights=weights, k=1)
            return rand_list[0]
        else:
            print('Error', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
    
def adlibber(excuse):
    diction = []
    for lib in excuse.libs:
        new_word = api_req(lib["api"], lib["affix"])
        diction.append(new_word["word"])
    template_split = excuse.template.split("?")
    i = 0
    start = template_split[0]
    end = ""
    while i < len(diction):
        end += (diction[i] + template_split[i + 1])
        i += 1
    return start + end
