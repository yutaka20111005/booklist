import streamlit as st
import pandas as pd

st.write("Book list by Streamlit\n")
st.markdown("### 書籍一覧")

st.write(pd.DataFrame({
  '書籍名': ['日経Linux（リナックス） 2024年1月号','Kubernetes完全ガイド 第2版','フロントエンドの知識地図―― 一冊でHTML/CSS/JavaScriptの開発技術が学べる本','独習 Pythonバイオ情報解析?Jupyter、NumPy、pandas、Matplotlibを理解し、実装して学ぶシングルセル、RNA-Seqデータ解析 (実験医学別冊)'],
  '価格': [2000,4400,2860,6600],
  '内容': ["2024年1月号が最後となりました。Linux最新の話題をまとめた雑誌はこれだけだったので残念。バックナンバーをま とめたのを１冊買って、過去から一気に手を動かして動作させるのはおススメです。","Kubernetesに関わる人のバイブルです。","非常によくまとまってます","バイオインフォマティクスかつ、シングルセル、RNA-Seq解析を実装しつつ学べます。"],
}))
