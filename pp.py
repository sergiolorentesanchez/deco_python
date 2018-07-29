import json
import os
import oso

la macarena duerme

def translate_output(func):
    def wrap(self, *args, **kwargs):
        return translate(func(self, *args, **kwargs))
    return wrap

def translate(items):
    if isinstance(items, list):
        translated_items = []
        for item in items:
            translated_items.append(translate(item))
        return translated_items
    else:
        translated_item = dict()
        translated_item['id'] = int(items['id'])
        translated_item['title'] = items['titulo']
        return translated_item


dict1=dict()
dict2=dict()
dict1["id"]=1
dict1["titulo"] = 'PAPA'
dict2["id"]=2
dict2["titulo"] = 'MAMA'
list1 = [dict1, dict2]

#print (list1)

@translate_output
def data(self):
    return dict2

a=data(data)
