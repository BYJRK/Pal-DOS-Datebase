import json
from rich import print

with open('enemies.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    """
    每项数据形如：
    {
        'name': 怪物名称,
        'lv': 等级,
        'hp': 血量,
        'exp': 经验值,
        'money': 金钱,
        'item': [ 偷取物, 数量 ],
        'gourd': 灵壶值,
        'resis': [ 毒、风、雷、水、火、土、物、巫抗 ]
    }
    """
    print('偷取金钱排名：')
    for line in sorted(
        filter(lambda r: r['item'][0] == '金钱', res),
        key=lambda r: r['item'][1],
        reverse=True,
    ):
        print({key: line[key] for key in ['name', 'item']})

    print('血量排名 (top 10)：')
    for line in sorted(res, key=lambda r: r['exp'], reverse=True)[:10]:
        print({key: line[key] for key in list(line.keys())[:5]})
