import yaml


def get_data(yml_name, case_data_name):
    with open("./Data/data_"+yml_name+".yml", "r", encoding="utf8") as f:

        data = yaml.load(f)["test_"+ case_data_name]

        data_list = list()

        for key in data.values():

            tmp_list = list()

            for val in key.values():
                tmp_list.append(val)

            data_list.append(tmp_list)

    return data_list


# [(张三，33), (李四, 22)]
if __name__ == '__main__':
    print(get_data("myself", "login_no_num"))






