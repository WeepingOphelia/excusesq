import requests
import random
import json
import re


datamuse = "https://api.datamuse.com/words?"
with open("word_bank.json", "r") as f:
    word_bank = json.load(f)


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
    template = excuse.template
    template.format(
        noun=api_req(datamuse, "rel_jjb=big&rc=is"),
        nouns=api_req(datamuse, "lc=many&rc=are"),
        verb=api_req(datamuse, "rel_trg=run"),
        adj=api_req(datamuse, "rel_jja=cat"),
    )

def chadlibber(excuse):
    template = excuse.template
    placeholders = re.findall(r"\{(.*?)\}", template)
    template = re.sub(r"\{.*?\}", "{}", template).strip()
    libs = map(lambda x: random.choice(word_bank[x]), placeholders)
    new_excuse = template.format(*list(libs))
    return new_excuse


def dadlibber(excuse):
    diction = []
    for lib in excuse.libs:
        new_word = api_req(lib["api"], lib["affix"])
        diction.append(new_word["word"])
    template = excuse.template
    for i in range(len(diction)):
        template = template.replace("{" + str(i) + "}", diction[i])
    return template

# def nadlibber(excuse):
#     template = excuse.template
#     new_excuse = template.format(
#         noun=random.choice(all_nouns),
#         nouns=random.choice(all_nouns),
#         verb=random.choice(all_verbs),
#         adjective=random.choice(all_adj),
#     )
#     return new_excuse