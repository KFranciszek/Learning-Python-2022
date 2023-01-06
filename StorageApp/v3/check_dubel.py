import  json
import  sys
def dubel():
    try:
        with open("prod_list.json", 'r') as f:
            data_open = f.read()
            data_search = json.loads(data_open)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    except  ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')


    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    count_dic = {}
    count = 0

    for i in data_search:
        if i["name"] in count_dic:
            count_dic[i["name"]] += 1
        else:
            count_dic[i["name"]] = 1

    for i, count in count_dic.items():
        if count >1:
            print(f"{i} appears {count} times.")


dubel()

