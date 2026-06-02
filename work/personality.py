import streamlit as st

# 页面配置
st.set_page_config(page_title="元素人格测试仪", page_icon="✨", layout="centered")
st.title("✨ 元素人格测试仪")
st.caption("根据你的信息生成专属元素人格")

# 用户输入
with st.form("personality_form"):
    name = st.text_input("请输入你的名字")
    month = st.slider("出生月份", 1, 12, 6)
    style = st.radio("你更偏向", ["安静内敛", "勇敢冒险", "理性思考", "热情外向"], horizontal=True)
    submit = st.form_submit_button("生成人格")

# 人格计算
def generate_element(month, style):
    elements = ["水", "火", "风", "土"]
    base = elements[month % 4]
    suffix = {
        "安静内敛": "·静谧",
        "勇敢冒险": "·无畏",
        "理性思考": "·理性",
        "热情外向": "·炽热"
    }
    return base + suffix[style]

# 结果展示
if submit:
    if not name:
        st.warning("请先输入名字！")
    else:
        res = generate_element(month, style)
        st.success(f"{name}，你的专属人格：【{res}】")
        st.info(f"【{res}】特质：直觉敏锐、风格独特、气场稳定，自带治愈/吸引力～")

# 页脚
st.divider()
st.caption("课程期末作业 | Streamlit 交互应用")