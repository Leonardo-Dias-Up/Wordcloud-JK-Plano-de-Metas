# importar os pacotes necessários
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import nltk
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# importar o arquivo csv em um df
df = pd.read_csv(r"D:\01. Python\Diversos\Nuvem Texto\O governo JK e seu Plano de Metas.csv", sep =';')
df = df.T.reset_index(drop=True).T

# eliminar as colunas com valores ausentes
summary = df.dropna(subset=[0], axis=0)[0]
# exemplos de descrições para os imóveis no Airbnb
display(summary.iloc[100])
display(summary.iloc[120])
display(summary.iloc[133])

# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(nltk.corpus.stopwords.words('portuguese'))
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="black",
                      width=1600, height=800).generate(all_summary)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud);
wordcloud.to_file("airbnb_summary_wordcloud.png")

# endereço LOCAL da SUA imagem
rio_mask = np.array(Image.open(r"D:\01. Python\Diversos\Nuvem Texto\24585310_l-2.jpg"))
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="black",
                      width=1000, height=1000, max_words=2000,
                      mask=rio_mask, max_font_size=200,
                      min_font_size=1).generate(all_summary)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("airbnb_summary_wordcloud.png")










