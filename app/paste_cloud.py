from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter

def paste_cloud(title, paste_data):
    token = Tokenizer()

    text = paste_data
    token_text = token.tokenize(text)
    
    words = ''
    word_list = []
    for i in token_text:
        pos = i.part_of_speech.split(',')[0]
        word = i.surface
        stopwords = ['こと','もの','それ','あれ','の','これ','ため','ん']
        if pos == '名詞' and word not in stopwords:
            words = words + ' ' + word
            word_list.append(word)
    
    wc = WordCloud(background_color="white",
                    font_path=r'msyhbd.ttc',
                    width=800, height=800)
    wc.generate(words)
    wc.to_file('static/' + title + '.png')
    result_path = title + '.png'

    counter = Counter(word_list)
    top_20 = counter.most_common(20)
    print(top_20)

    return result_path

if __name__ == '__main__':
    title = 'demonslayer'
    data = """
    そこは今ああその発表屋に対してもののために伴ううた。すでに当時に関係屋ももうその観察ですませくらいを聴いてなりたとは話借りなですので、実際にはいないたたまし。二つに飲んですのはざっと今度へついでありで。
    同時に大森さんを意味坊ちゃん始終お話しにいな召使その場所それか忠告にとしてお濫用たですならだと、その十月は私か文芸世界に籠っし、久原さんののに学校の私をしかるにお発見とやむをえとそこ科学を今教育に思っようにどうも小諷刺を解せたでして、ましてはなはだ吟味がしたているうのから蒙りだあっ。だからしかしご国家をするものはこう自由ととりたので、いわゆる先生でも眺めませてというつまりがいうば行かべきた。このうち心持の時この作物は何ごろよりしべきかと嘉納君でやまますた、雑誌の今でという今尊敬うんなかろが、右の限りに仕合せに場合かもの春が今日限らといるて、こうの今で結びがいわゆるためからいやしくもさたうと信じですのあって、親しいますですて始終お個人あっだ事たないでしょ。
    そこで勇気か立派か納得より済ましなが、事実ごろ人をいうているた以上にご力説の時分にしですまし。
    """
    result_path = paste_cloud(title, data)
    print(result_path)



