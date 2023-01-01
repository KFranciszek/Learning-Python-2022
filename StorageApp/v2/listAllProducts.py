import  json
def list_all():
    with open("prod_list.json", 'r') as f:
       data = f.read()
       json_object = json.loads(data)
       json_formatted_str = json.dumps(json_object, indent=0)
       print(json_formatted_str)


list_all()