from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
#text = r'F:\春江花月夜.txt'
text = r'F:\明鹏大殿.txt'
f = open(text, 'r').read()
cut_text = ' '.join(jieba.cut(f, cut_all=True))
bg_pic = imread(r'D:\python\词云\1.png')
wordcloud = WordCloud(
    background_color='white', #设置背景颜色
    mask=bg_pic,  #设置背景图片
    max_words=2000, #设置最大显示的字数
    scale=1,
    #stopwords="", #设置停用词
    font_path="C:/Windows/Fonts/simhei.ttf",
    #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
    max_font_size=40,  #设置字体最大值
    random_state=30, #设置有多少种随机生成状态，即有多少种配色方案
    width=800,
    height=400,
).generate(cut_text)
image_color = ImageColorGenerator(bg_pic) # 提取图片的色彩分布。
a = wordcloud.recolor(color_func=image_color)
plt.imshow(a, interpolation='bilinear') #
#plt.imshow(wordcloud)
plt.axis("off")
plt.show()
f.close()
