from paddleocr import PaddleOCR,draw_ocr
import re
import genanki
import argparse


# 创建一个解析器对象
parser = argparse.ArgumentParser(description='Process some images.')
# 添加参数
parser.add_argument('-n', '--filename', type=str, default='3.jpg', help='the name of the image file')
parser.add_argument('-l', '--language', type=str, default='zh', help='the language of the text')
parser.add_argument('-c', '--count', type=int, default=1, help='the number to divide the Chinese list')

# 解析命令行参数
args = parser.parse_args()

# 使用解析后的参数
img_path = args.filename
language = args.language
count = args.count

ocr = PaddleOCR(use_angle_cls=True) # need to run only once to download and load model into memory
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
# 过滤掉包含数字的文本
#txts = [txt for txt in txts if not re.search(r'\d', txt)]
# 使用正则表达式将数字替换为空格
#txts = [re.sub(r'\d', ' ', txt) for txt in txts]

txts = [re.sub(r'[.\d]', '', txt) for txt in txts]
# 使用正则表达式分别提取中文和英文字符，保留英文中的标点符号和单词之间的空格
txts = [(re.findall(r'[\u4e00-\u9fff]+', txt), re.findall(r'[a-zA-Z.,!?]+(?:\s+[a-zA-Z.,!?]+)*', txt)) for txt in txts if txt]

cards = txts


# 创建一个模型
my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Chinese'},
        {'name': 'English'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Chinese}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{English}}',
        },
    ])

# 创建一个牌组
my_deck = genanki.Deck(
    2059400110,
    'Chinese-English Deck')

# 添加卡片到牌组
for chinese, english in cards:
    note = genanki.Note(
        model=my_model,
        fields=[''.join(chinese), ''.join(english)]
    )
    my_deck.add_note(note)
# 生成 .apkg 文件
genanki.Package(my_deck).write_to_file(img_path+'.apkg')

# 打印中英文对照
if language == 'zh':
    for i, (chinese, english) in enumerate(cards):
        print("中文: ", ''.join(chinese))
elif language == 'en':
    for i, (chinese, english) in enumerate(cards):
        print("English: ", ''.join(english))
else:
    for i, (chinese, english) in enumerate(cards):
        print("中文: ", ''.join(chinese))
        print("英文: ", ''.join(english))


# 打印比例
if count > 2:
    ratio = len(cards) / count
    print(f"识别比例: {len(cards)}/{count}, {ratio:.1%}")
#im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
#im_show = Image.fromarray(im_show)
#im_show.save('result.jpg')