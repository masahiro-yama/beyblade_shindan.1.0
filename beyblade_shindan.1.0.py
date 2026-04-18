import streamlit as st
import random

# ------------------------
# 初期化
# ------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.questions = []

# ------------------------
# 質問データ
# ------------------------
base_questions = [
    ("やすみじかん、なにしてる？", ["A はしってあそぶ", "B みんなをみながらあそぶ", "C しずかにあそぶ", "D そのときでかえる"]),
    ("ともだちとぶつかったら？", ["A すぐいいかえす", "B いちどきいてからこたえる", "C あまりきにしない", "D そのときでかえる"]),
    ("ゲームでだいじなのは？", ["A はやくかつ", "B まけない", "C さいごまでつづける", "D あいてにあわせる"]),
    ("しゅくだんはどうする？", ["A いっきにやる", "B ていねいにやる", "C すこしずつやる", "D ようすでかえる"]),
    ("あたらしいあそびは？", ["A すぐやる", "B ルールをみる", "C ゆっくりなれる", "D あわせる"]),
]

extra_questions = [
    ("ヒーローになるなら？", ["A こうげきでたたかう", "B まもりながらたたかう", "C ずっとがんばる", "D なんでもできる"]),
    ("すきなどうぶつは？", ["A ライオン", "B ゾウ", "C カメ", "D サル"]),
    ("ちからをもらうなら？", ["A いっしゅんでつよい", "B なんでもまもる", "C ずっとつづく", "D なんでもできる"]),
]

# ------------------------
# 質問生成
# ------------------------
def generate_questions():
    q = base_questions.copy()
    q.append(random.choice(extra_questions))
    random.shuffle(q)
    return q

# ------------------------
# 判定
# ------------------------
def get_result(answers):
    count = {"A":0, "B":0, "C":0, "D":0}
    for a in answers:
        count[a] += 1

    result = max(count, key=count.get)

    if result == "A":
        return "アタック"
    elif result == "B":
        return "ディフェンス"
    elif result == "C":
        return "スタミナ"
    else:
        return "バランス"

# ------------------------
# トップ画面
# ------------------------
if st.session_state.step == 0:
    st.title("🌀 ベイブレードしんだん")
    st.write("キミにぴったりのタイプをみつけよう！")

    if st.button("▶ スタート！"):
        st.session_state.questions = generate_questions()
        st.session_state.answers = []
        st.session_state.step = 1

# ------------------------
# 質問画面
# ------------------------
elif st.session_state.step <= len(st.session_state.questions):

    q_index = st.session_state.step - 1
    question, options = st.session_state.questions[q_index]

    st.write(f"Q{st.session_state.step} / {len(st.session_state.questions)}")
    st.subheader(question)

    choice = st.radio("", options)

    if st.button("つぎへ"):
        st.session_state.answers.append(choice[0])  # A/B/C/Dだけ保存
        st.session_state.step += 1

# ------------------------
# 結果画面
# ------------------------
else:
    result = get_result(st.session_state.answers)

    st.title("🎉 けっか！")

    if result == "アタック":
        st.header("💥 アタックタイプ！")
        st.write("ドカンと決める！はやくうごいて勝つ！")

        st.image("https://m.media-amazon.com/images/I/61MpAh-qOsL._AC_SY450_.jpg", width=200)
        st.write("ドランソード")
        st.link_button("これほしい！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-BEYBLADE-BX-01/dp/B0C52R16P1/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1S7751JY65DTB&dib=eyJ2IjoiMSJ9.pQ365hsYiqIE9suuCA2NUQhCvnfEa9NcHgq-1ibW5UAv5zaDalxLMfzq5i6GQAE5xwsCUocXU7gaGZguFWHrD2KKzjfdiVk76qDotoIFByE2h4Au3SxE4uher1wjkTN--9KS2d6j8tsjGu7UNcGFme8D5KGO2bYlyuKOf67mPkF7rNM3eXsdy6HLMOG7HEJ4Rx-jeKoIGWdRYXbAqe16NwcDfkzKjqG01hqCNanAhu_21C8lcPCAKQmPzTi9jPlUY0B3mrJ-mB7INQUDMT5HE-frkT2xzchig2fGgQsMICQ.rNG60mmHa9BE0SuxHYUHD6Ak1kUMSoEI7TBNGj68J30&dib_tag=se&keywords=%E3%83%89%E3%83%A9%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%89&qid=1776520504&sprefix=%E3%83%89%E3%83%A9%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%89%2Caps%2C510&sr=8-2&th=1")

        st.image("https://m.media-amazon.com/images/I/715NtHVPy-L._AC_SY450_.jpg", width=200)
        st.write("フェニックスウイング")
        st.link_button("これほしい！", "https://www.amazon.co.jp/BEYBLADE-%E3%83%99%E3%82%A4%E3%83%96%E3%83%AC%E3%83%BC%E3%83%89X-BX-23-%E3%83%95%E3%82%A7%E3%83%8B%E3%83%83%E3%82%AF%E3%82%B9%E3%82%A6%E3%82%A4%E3%83%B3%E3%82%B0-9-60GF/dp/B0CMZSRJ3Q?ref_=ast_sto_dp")

    elif result == "ディフェンス":
        st.header("🛡 ディフェンスタイプ！")
        st.write("まもってチャンス！あいてのこうげきをうける！")

        st.image("https://m.media-amazon.com/images/I/61N7ksTpjhL._AC_SY450_.jpg", width=200)
        st.write("ナイトフォートレス")
        st.link_button("これほしい！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-CX-14-%E3%83%8A%E3%82%A4%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%88%E3%83%AC%E3%82%B9GV8-70UN/dp/B0GMDYS21K?ref_=ast_sto_dp")

        st.image("https://m.media-amazon.com/images/I/71AMNY-FmqL._AC_SY450_.jpg", width=200)
        st.write("レオンクレスト")
        st.link_button("これほしい！", "https://www.amazon.co.jp/BEYBLADE-%E3%83%99%E3%82%A4%E3%83%96%E3%83%AC%E3%83%BC%E3%83%89X-UX-06-%E3%83%AC%E3%82%AA%E3%83%B3%E3%82%AF%E3%83%AC%E3%82%B9%E3%83%88-7-60GN/dp/B0D91K2WMS?ref_=ast_sto_dp&th=1")

    elif result == "スタミナ":
        st.header("🔄 スタミナタイプ！")
        st.write("さいごまでぐるぐる！ながくがんばる！")

        st.image("https://m.media-amazon.com/images/I/61qO6OBNzBL._AC_SY450_.jpg", width=200)
        st.write("ウィザードアーク")
        st.link_button("これほしい！", "https://www.amazon.co.jp/BEYBLADE-%E3%83%99%E3%82%A4%E3%83%96%E3%83%AC%E3%83%BC%E3%83%89X-CX-02-%E3%82%A6%E3%82%A3%E3%82%B6%E3%83%BC%E3%83%89%E3%82%A2%E3%83%BC%E3%82%AF-R4-55LO/dp/B0DWSRHP7J?ref_=ast_sto_dp&th=1")

        st.image("https://m.media-amazon.com/images/I/61aJExH96+L._AC_SY450_.jpg", width=200)
        st.write("ヘルズサイズ")
        st.link_button("これほしい！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-BEYBLADE-BX-02/dp/B0C52C4L3T?ref_=ast_sto_dp&th=1")

    else:
        st.header("⚡ バランスタイプ！")
        st.write("なんでもできる！あいてにあわせる！")

        st.image("https://m.media-amazon.com/images/I/61WEAT7WNKL._AC_SY450_.jpg", width=200)
        st.write("エンペラーマイト")
        st.link_button("これほしい！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-BEYBLADE-%E3%82%A8%E3%83%B3%E3%83%9A%E3%83%A9%E3%83%BC%E3%83%9E%E3%82%A4%E3%83%88%E3%83%87%E3%83%83%E3%82%AD%E3%82%BB%E3%83%83%E3%83%88/dp/B0FV6Y4MH4?ref_=ast_sto_dp&th=1")

        st.image("https://m.media-amazon.com/images/I/712keT+tMML._AC_SY450_.jpg", width=200)
        st.write("スコーピオスピア")
        st.link_button("これほしい！", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-UX-14-%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%94%E3%82%AA%E3%82%B9%E3%83%94%E3%82%A20-70Z/dp/B0F47G3QJT?ref_=ast_sto_dp")

    if st.button("🔁 もういちどやる"):
        st.session_state.step = 0