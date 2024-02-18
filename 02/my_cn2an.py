"""
将一个大写中文数字转换成阿拉伯数字
"""

# 数字映射
number_map = {
    "零": 0,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9
}

# 单位映射
unit_map = {
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10000,
    "亿": 100000000
}


def backward_cn2an_three(inputs):
    output = 0
    unit = 1
    # 万、亿的单位
    ten_thousand_unit = 1
    num = 0
    for index, cn_num in enumerate(reversed(inputs)):
        if cn_num in number_map:
            # 数字
            num = number_map[cn_num]
            # 累加
            output = output + num * unit
        elif cn_num in unit_map:
            # 单位
            unit = unit_map[cn_num]
            # 判断出万、亿
            if unit % 10000 == 0:
                # 万、亿
                if unit > ten_thousand_unit:
                    ten_thousand_unit = unit
                # 万亿
                else:
                    ten_thousand_unit = unit * ten_thousand_unit
                    unit = ten_thousand_unit

            if unit < ten_thousand_unit:
                unit = ten_thousand_unit * unit
        else:
            raise ValueError(f"{cn_num} 不在转化范围内")

    return output


if __name__ == '__main__':
    chinese_numerals = input("输入:")
    output = backward_cn2an_three(chinese_numerals)
    print(f"输出：{output}")
