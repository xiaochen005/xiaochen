# 导入库
import streamlit as st
import math

# 页面标题与说明
st.title("元素人格测试仪-最终版")
st.caption("基于火/水属性分数，匹配最接近的元素模板")

# 1. 用户输入模块
name = st.text_input("输入你的代号:", "见习炼金术士")
fire_score = st.slider("火属性", 0, 10, 5)
water_score = st.slider("水属性", 0, 10, 5)
user = [fire_score, water_score]  # 用户属性坐标
st.write(f"你的元素坐标：**{user}**")

# 2. 元素模板库（字典存储）
element_templates = {
    "火型·烈焰炼金术士": [10, 4],
    "水型·潮汐观察者": [4, 10],
    "风型·疾风游侠": [8, 7],
    "土型·大地守卫者": [3, 3],
    "雷型·惊雷审判官": [9, 6],
    "平衡型·元素使者": [7, 7]
}

# 3. 打擂台法初始化
min_dist = 999999.0
best_match = ""

# 4. 匹配逻辑（按钮触发）
if st.button("开始智能匹配", type="primary"):
    st.write("### 各模板距离计算结果")
    # 遍历所有模板
    for template_name, template_coords in element_templates.items():
        # 勾股定理计算距离
        distance = math.sqrt((user[0] - template_coords[0])**2 + (user[1] - template_coords[1])**2)
        st.write(f"{template_name}：{distance:.2f}")
        
        # 打擂台更新最优匹配
        if distance < min_dist:
            min_dist = distance
            best_match = template_name

    # 结果展示（AI优化部分：分隔线+高亮成功框）
    st.divider()
    st.success(f"🎉 {name}，你最匹配的元素身份是：【{best_match}】")
    st.info(f"匹配距离：{min_dist:.2f}（距离越小越匹配）")
    st.balloons()
    st.toast("匹配完成！")