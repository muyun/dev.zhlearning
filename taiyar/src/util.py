"""
import spacy
from spacy.lang.zh.examples import sentences

nlp = spacy.load("zh_core_web_sm")
user_dict = []
nlp.tokenizer.pkuseg_update_user_dict(user_dict)
"""

# text preprocessing
import re


# Tokenize texts with ckip-transformers
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger

# word segmentation
ws_driver = CkipWordSegmenter()
# part-of-speech
pos_driver = CkipPosTagger()

# Then spaCy

text = """
嗒嗒的家人無不是棕色的,唯有嗒嗒例外。牠一身連帶鬃毛也是灰濛濛的,這種不一樣常常使牠難過,使牠不由得羨慕別人。

今天如常風和日麗,朋友們全都在翠綠的草原上奔馳,你追我逐,氣氛歡樂。
可是,嗒嗒從來沒有自信參與其中,牠總躲在森林裏。

嗒嗒的節目也很豐富呢!牠有時在旁觀看馬兒賽跑,有時乾脆走進森林裏欣賞
大自然。嗒嗒夢想擁有其他動物的優點,藉此獲得認同。

牠凝望着長頸鹿,心裏想:要是我也有那麼長的脖子,我肯定會把樹上青翠欲
滴的蘋果一個一個地摘下來吃。

牠繼續在森林行逛,這次看到知更鳥和孔雀。牠又羨慕知更鳥起來。嗒嗒心
想:我若擁有了那湛藍的翅膀,我肯定能一遍又一遍地飛越草原。

嗒嗒轉身看看孔雀,果然又使牠羨慕起來:要是我擁有孔雀迷人的尾巴,那麼
所有人都會欣賞我。
"""


def main():
    ws = ws_driver([text])
    pos = pos_driver(ws)
    tokens = ws[0]
    # print(tokens)
    # print(pos)
    for element in list(zip(tokens, pos[0])):
        print(element)


if __name__ == "__main__":
    main()
