import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

# ======================================================
# プレグレスバー
st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

# ======================================================
st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40],
# })
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# 表形式
# st.write(df)
# st.dataframe(df, width = 100, height = 100)  # オプションでサイズを設定できる
# st.dataframe(df.style.highlight_max(axis=0))  # 列や行にハイライト付与できる（今回は列の最大値）
# st.table(df.style.highlight_max(axis=0))       # 静的な表（ソート不可）

# 折れ線グラフ
# st.line_chart(df)
# st.area_chart(df)
# 棒グラフ
st.bar_chart(df)

# マークダウン
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# ======================================================
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
# 地図表示
st.map(df)

# ======================================================
st.write('Interactive Widgets')

# チェックボックス
if st.checkbox('Show Image'):
    # 画像表示
    img = Image.open('sample.jpg')
    st.image(img, caption='BIG', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11)),
)

'あなたの好きな数字は、', option, 'です。'

# テキスト入力
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は、', text, 'です。'

# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition

# ======================================================
# サイドバー
text2 = st.sidebar.text_input('サイドバーテキスト')
st.sidebar.write('テキスト： ' + text2)

condition2 = st.sidebar.slider('サイドスライダー', 0, 100, 50)
st.sidebar.write('スライダー： ' + str(condition2))


# ======================================================
# ２カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

# ======================================================
# エクスパンダー
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
