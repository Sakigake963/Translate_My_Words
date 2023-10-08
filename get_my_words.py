from janome.tokenizer import Tokenizer
from collections import Counter
import get_my_tweets as gmt
from mtranslate import translate

"""
単語は二文字以上を対象としてある。
品詞は名詞、形容詞、副詞、動詞を対象としてある。

Twitterのアーカイブダウンロードから得られるTweets.jsファイルを
同じファイル内に移動させてから実行すること。
"""

def translate_words(words, dest_language='en'):
    # 単語をスペースで結合して一度に翻訳
    text_to_translate = ' '.join(words)
    translated_text = translate(text_to_translate, dest_language)

    # 翻訳されたテキストを単語に戻す
    translated_words = translated_text.split()
    return translated_words

def count_words(sentences):
    # 形態素解析器の初期化
    tokenizer = Tokenizer()

    # 全文章の形態素を格納するリスト
    all_tokens = []

    # 各文章ごとに形態素解析を行い、リストに追加
    for sentence in sentences:
        tokens = tokenizer.tokenize(sentence)
        all_tokens.extend(token.base_form for token in tokens if token.part_of_speech.startswith(('名詞', '形容詞', '副詞', '動詞', '連体詞', '感動詞', '接続詞', '助詞', '助動詞')))

    # 各単語の出現回数を数える
    word_counts = Counter(all_tokens)

    # 出現回数の降順でソート
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))

    return sorted_word_counts

# サンプルの文章のリスト
sample_sentences = gmt.get_my_tweets()

# 各単語の出現回数を数える
sorted_word_counts = count_words(sample_sentences)

# 結果の表示
for word, count in sorted_word_counts.items():
    translated = translate_words(word)
    if (len(word) > 1):
      print(f'{word}: 出現回数 = {count} 翻訳 = {translated}')
