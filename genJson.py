'''
@Description  : generate json files with chinese holiday
@Author       : Zexin Zheng
@Date         : 2020-06-15 14:35:28
@LastEditors  : Zexin Zheng
@LastEditTime : 2020-06-15 16:23:24
'''
import datetime
import os
import json


def main():
    with open('db/2020.json', 'r', encoding='utf-8') as f_holiday:
        data = json.load(f_holiday)
        # print(data)
    holidays = dict()
    for day in data['days']:
        holidays[day['date']] = day

    date_begin = datetime.date(2020, 1, 1)
    date_end = datetime.date(2020, 12, 31)

    delta = datetime.timedelta(days=1)
    d = date_begin
    while d < date_end:
        # print(d.strftime("%Y-%m-%d"))
        f1 = d.strftime("%Y-%m-%d")
        f2 = d.strftime("%Y/%m/%d.json")
        os.makedirs(os.path.join('holiday', os.path.dirname(f2)), 0o777, True)

        if f1 in holidays:
            # print(f1)
            tmp_dict = {
                "code": 0,
                "type": {
                    "type": 2,
                    "name": "周一",
                    "week": 1
                },
                "holiday": {
                    "holiday": False,
                    "name": "国庆前调休",
                    "wage": 1,
                    "after": False,
                    "target": '国庆节'
                }
            }
            if holidays[f1]['isOffDay'] is True:
                tmp_dict['type']['type'] = 2
                tmp_dict['holiday']['holiday'] = True
                tmp_dict['holiday']['name'] = holidays[f1]['name']
                tmp_dict['holiday']['target'] = holidays[f1]['name']
            else:
                tmp_dict['type']['type'] = 3
                tmp_dict['holiday']['holiday'] = False
                tmp_dict['holiday']['name'] = holidays[f1]['name']
                tmp_dict['holiday']['target'] = holidays[f1]['name']
                tmp_dict['holiday']['after'] = holidays[f1]['after']

            if 'desc' in holidays[f1]:
                tmp_dict['holiday']['name'] = holidays[f1]['desc']
            if 'wage' in holidays[f1]:
                tmp_dict['holiday']['wage'] = holidays[f1]['wage']
            weekday = d.isoweekday()

        else:
            tmp_dict = {
                "code": 0,
                "type": {
                    "type": 0,
                    "name": "周一",
                    "week": 1
                },
                "holiday": None
            }
            weekday = d.isoweekday()
            if weekday in [6, 7]:
                tmp_dict['type']['type'] = 1
            else:
                tmp_dict['type']['type'] = 0

        week_dict = {
            1: '周一',
            2: '周二',
            3: '周三',
            4: '周四',
            5: '周五',
            6: '周六',
            7: '周日'
        }
        tmp_dict['type']['week'] = weekday
        tmp_dict['type']['name'] = week_dict[weekday]

        fp = open(os.path.join('holiday', f2), "w", encoding='utf-8')
        json.dump(tmp_dict, fp, ensure_ascii=False)
        fp.close()

        d += delta


if __name__ == '__main__':
    main()