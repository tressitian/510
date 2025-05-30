import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import calendar
import os, json
import random

def show_analyze():
    st.header("Analyze Your Outfit Style and Use Frequency")
    
    # --- Style & Color Analysis ---
    st.subheader("Your Style & Color Analysis")
    col_style, col_color = st.columns(2)

    # --- Style Pie ---
    with col_style:
        # Example style distribution chart (replace with real data if available)
        style_data = {
            'Style': ['Casual', 'Formal', 'Sports', 'Party'],
            'Count': [45, 15, 20, 10]
        }
        fig = px.pie(style_data, values='Count', names='Style', title='Style Distribution')
        st.plotly_chart(fig)

    # --- Color Pie ---
    with col_color:
        SAVE_DIR = "captured_images"
        color_count = {}
        for fname in os.listdir(SAVE_DIR):
            if fname.endswith('.json'):
                with open(os.path.join(SAVE_DIR, fname), 'r') as f:
                    try:
                        meta = json.load(f)
                        color = meta.get('color', '').strip().lower()
                        if color:
                            color_count[color] = color_count.get(color, 0) + 1
                    except Exception:
                        pass
        if color_count:
            color_df = pd.DataFrame({
                'Color': list(color_count.keys()),
                'Count': list(color_count.values())
            })
            # 颜色映射：常见色用标准色，否则用默认
            color_map = {
                'black': '#222222', 'white': '#eeeeee', 'gray': '#888888', 'grey': '#888888',
                'blue': '#3b6ea5', 'red': '#e74c3c', 'green': '#27ae60', 'yellow': '#f7d358',
                'brown': '#a0522d', 'beige': '#f5f5dc', 'pink': '#ffb6c1', 'purple': '#8e44ad',
                'orange': '#ffa500', 'navy': '#001f3f', 'gold': '#ffd700', 'silver': '#c0c0c0'
            }
            color_seq = [color_map.get(c, None) for c in color_df['Color']]
            fig_color = px.pie(color_df, values='Count', names='Color', title='Color Distribution', color_discrete_sequence=color_seq)
            st.plotly_chart(fig_color)
        else:
            st.info("No color data available yet.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Insights ---
    style_insight = "• Your wardrobe is predominantly casual (50%)\n" \
                    "+ You might want to add more formal pieces\n" \
                    "+ Good balance of sportswear"
    if color_count:
        most_color = color_df.loc[color_df['Count'].idxmax(), 'Color']
        color_insight = f"• Your most common color is: {most_color.capitalize()}\n" \
                        f"+ Try to add more variety if you want a more colorful closet!"
    else:
        color_insight = "• No color data available yet."
    st.markdown("#### Insights")
    st.info(f"**Style:**\n{style_insight}\n\n**Color:**\n{color_insight}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    # Monthly calendar view
    st.subheader("Monthly Outfit Calendar")
    current_date = datetime.now()
    month_calendar = calendar.monthcalendar(current_date.year, current_date.month)

    # 获取所有衣服图片路径
    image_dir = "captured_images"
    all_imgs = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # 星期标题
    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    week_cols = st.columns(7)
    for i, wd in enumerate(week_days):
        with week_cols[i]:
            st.markdown(f"**{wd}**")
    # Create calendar grid
    for week in month_calendar:
        cols = st.columns(7)
        for i, day in enumerate(week):
            with cols[i]:
                if day != 0:
                    st.write(f"{day}")
                    if all_imgs:
                        img_path = os.path.join(image_dir, random.choice(all_imgs))
                        st.image(img_path, width=50)
                    else:
                        st.image("https://via.placeholder.com/100", width=50)
                else:
                    st.write("")

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    # Most worn items analysis
    st.subheader("Most Worn Items")
    # 统计所有衣服的穿着次数
    worn_stats = []
    for fname in os.listdir(image_dir):
        if fname.endswith(('.jpg', '.jpeg', '.png')):
            json_path = os.path.join(image_dir, fname + '.json') if not fname.endswith('.json') else fname
            if not fname.endswith('.json'):
                json_path = os.path.join(image_dir, fname + '.json')
            else:
                continue
            if os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    try:
                        meta = json.load(f)
                        times_worn = len(meta.get('date_wore', []))
                        worn_stats.append({
                            'img': os.path.join(image_dir, fname),
                            'type': meta.get('type', ''),
                            'style': meta.get('style', ''),
                            'color': meta.get('color', ''),
                            'times': times_worn
                        })
                    except Exception:
                        pass
    # 排序并取前3
    worn_stats = sorted(worn_stats, key=lambda x: x['times'], reverse=True)[:3]
    if worn_stats:
        trophy_svgs = [
            '<svg width="32" height="32" viewBox="0 0 24 24" fill="#FFD700" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C10.8954 2 10 2.89543 10 4V5H7C6.44772 5 6 5.44772 6 6V8C6 10.7614 8.23858 13 11 13H13C15.7614 13 18 10.7614 18 8V6C18 5.44772 17.5523 5 17 5H14V4C14 2.89543 13.1046 2 12 2ZM8 7H16V8C16 10.2091 14.2091 12 12 12C9.79086 12 8 10.2091 8 8V7ZM4 8C4 12.4183 7.58172 16 12 16C16.4183 16 20 12.4183 20 8H18C18 11.3137 15.3137 14 12 14C8.68629 14 6 11.3137 6 8H4ZM12 18C10.3431 18 9 19.3431 9 21H15C15 19.3431 13.6569 18 12 18Z"/></svg>',
            '<svg width="32" height="32" viewBox="0 0 24 24" fill="#C0C0C0" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C10.8954 2 10 2.89543 10 4V5H7C6.44772 5 6 5.44772 6 6V8C6 10.7614 8.23858 13 11 13H13C15.7614 13 18 10.7614 18 8V6C18 5.44772 17.5523 5 17 5H14V4C14 2.89543 13.1046 2 12 2ZM8 7H16V8C16 10.2091 14.2091 12 12 12C9.79086 12 8 10.2091 8 8V7ZM4 8C4 12.4183 7.58172 16 12 16C16.4183 16 20 12.4183 20 8H18C18 11.3137 15.3137 14 12 14C8.68629 14 6 11.3137 6 8H4ZM12 18C10.3431 18 9 19.3431 9 21H15C15 19.3431 13.6569 18 12 18Z"/></svg>',
            '<svg width="32" height="32" viewBox="0 0 24 24" fill="#CD7F32" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C10.8954 2 10 2.89543 10 4V5H7C6.44772 5 6 5.44772 6 6V8C6 10.7614 8.23858 13 11 13H13C15.7614 13 18 10.7614 18 8V6C18 5.44772 17.5523 5 17 5H14V4C14 2.89543 13.1046 2 12 2ZM8 7H16V8C16 10.2091 14.2091 12 12 12C9.79086 12 8 10.2091 8 8V7ZM4 8C4 12.4183 7.58172 16 12 16C16.4183 16 20 12.4183 20 8H18C18 11.3137 15.3137 14 12 14C8.68629 14 6 11.3137 6 8H4ZM12 18C10.3431 18 9 19.3431 9 21H15C15 19.3431 13.6569 18 12 18Z"/></svg>'
        ]
        for idx, item in enumerate(worn_stats, 1):
            cols = st.columns([1, 2, 6])
            with cols[0]:
                st.markdown(f"<div style='display:flex;align-items:center;gap:2px;'>"
                            f"<span style='font-size:2rem;font-weight:bold;'>{idx}</span>"
                            f"{trophy_svgs[idx-1] if idx<=3 else ''}</div>", unsafe_allow_html=True)
            with cols[1]:
                st.image(item['img'], width=100)
            with cols[2]:
                st.markdown(
                    f"<div style='display:flex;gap:2.5em;align-items:center;font-size:1.1rem;'>"
                    f"<span><b>Type:</b> {item['type'].capitalize()}</span>"
                    f"<span><b>Style:</b> {item['style'].capitalize()}</span>"
                    f"<span><b>Color:</b> {item['color'].capitalize()}</span>"
                    f"<span><b>Times Worn:</b> {item['times']}</span>"
                    f"</div>", unsafe_allow_html=True)
    else:
        st.info("No worn item data available yet.")
