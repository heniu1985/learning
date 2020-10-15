dict_list = [{'<TICKER>': 'HDR', '<DATE>': '19980317', '<CLOSE>': '11.633', '<VOL>': '67931'}, {'<TICKER>': 'HDR', '<DATE>': '19980318', '<CLOSE>': '10.481', '<VOL>': '115169'}, {'<TICKER>': 'HDR', '<DATE>': '19980319', '<CLOSE>': '10.131', '<VOL>': '75305'}, {'<TICKER>': 'HDR', '<DATE>': '19980320', '<CLOSE>': '10.481', '<VOL>': '53504'}, {'<TICKER>': 'HDR', '<DATE>': '19980323', '<CLOSE>': '10.379', '<VOL>': '27581'}, {'<TICKER>': 'HDR', '<DATE>': '19980324', '<CLOSE>': '10.228', '<VOL>': '37328'}, {'<TICKER>': 'HDR', '<DATE>': '19980325', '<CLOSE>': '10.131', '<VOL>': '28739'}, {'<TICKER>': 'HDR', '<DATE>': '19980326', '<CLOSE>': '10.131', '<VOL>': '45352'}, {'<TICKER>': 'HDR', '<DATE>': '19980327', '<CLOSE>': '10.027', '<VOL>': '42585'}, {'<TICKER>': 'HDR', '<DATE>': '19980330', '<CLOSE>': '10.027', '<VOL>': '21260'}]

for dictionary in dict_list:
    date = dictionary["<DATE>"]
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    date = f"{year}-{month}-{day}"
    dictionary["<DATE>"] = date

print(dict_list)