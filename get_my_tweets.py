import json, re

def get_my_tweets():
    # ファイルパス
    tweets_js_path = 'Tweets.js'
    json_output_path = 'tweets.json'

    # Tweets.jsファイルを読み込んでJSONに変換
    with open(tweets_js_path, 'r', encoding='utf-8') as tweets_js_file:
        # ファイルからJavaScriptのコードを読み込む
        js_code = tweets_js_file.read()

        # JavaScriptのコードからJSONデータを抽出
        start_index = js_code.find('[')
        end_index = js_code.rfind(']') + 1
        json_data = js_code[start_index:end_index]

        # JSONデータを読み込んでPythonオブジェクトに変換
        tweets = json.loads(json_data)

    # JSONデータをファイルに書き込む
    with open(json_output_path, 'w', encoding='utf-8') as json_output_file:
        json.dump(tweets, json_output_file, indent=2)

    # 消したい文字列の頭文字を入れる(それ以下の文字全消去)
    delete_list = ["http",
                            "@"
                            ]

    # 文字を整形してリストに入れる
    tweet_list = []
    for i in range(len(tweets)):
        tweet = tweets[i]["tweet"]["full_text"]
        tweet = tweet.replace("\n", "")

        # 消したい文字列を消す
        for i in range(len(delete_list)):
            delete_word = re.compile(f"{re.escape(delete_list[i])}.*")
            tweet = re.sub(delete_word, "", tweet)
            
        # 空文字とRT以外のツイートをリストに入れる
        if (tweet != "" and tweet[:2] != "RT"):
            tweet_list.append(tweet)
    return tweet_list