import unicodedata
import re
from fetch_image import ocr

IMAGENAME = 'narrow_jantama_player.png'
COLUMN_NAME = '対戦数 和了率 平均和了 ツモ率 平均順位 放銃率 副露率 和了巡数 立直率 一位率 二位率 三位率 四位率'.split(' ')
PACENTAGES = '和了率 ツモ率 平均順位 放銃率 副露率 和了巡数 立直率 一位率 二位率 三位率 四位率'.split(' ')
NOT_PACENTAGES = list(set(COLUMN_NAME) - set(PACENTAGES))
stats = {name: 0 for name in COLUMN_NAME}

def convert(txt):
    circle_nums = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
    num_convert = {circle_num: str(idx + 1) for idx, circle_num in enumerate(circle_nums)}
    num_convert["．"] = "."
    num_convert[" "] = ""
    num_convert[" "] = ""
    num_convert[" "] = ""
    txt = txt.replace("  ", "")

    return " ".join([ num_convert[t].strip() if t in num_convert else t for t in txt ])


def jantama_ocr():
    txt = ocr(IMAGENAME)
    txt = unicodedata.normalize("NFKC", txt)
    txt = txt.replace(" ", "").replace("\n", "")
    keys = re.split("[.\d%]+", txt)
    values = re.split("[^(.\d%)]+", txt)

    keys = [k for k in keys if k]
    values = [v for v in values if v]

    orc_dict = {k: v for k, v in zip(keys, values)}
    for key in orc_dict:
        if key in stats:
            if key in PACENTAGES:
                stats[key] = float(orc_dict[key][:4])
            else:
                stats[key] = int(orc_dict[key])

    return stats


if __name__=='__main__':
    print(jantama_ocr())

