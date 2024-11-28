import streamlit as st
from audio_recorder_streamlit import audio_recorder
import os

from streamlit import session_state, columns

from utils.recognition import rasr_example
from utils.recognition_file import recognize_file, recognize_file_mutilrole
from utils.summarize import langchain, conservation

# 设置页面标题和布局，必须放在第一行
st.set_page_config(page_title="AI伴学助手", initial_sidebar_state="collapsed")

# 假设您提供的函数
def recognize_audio(audio_file_path):
    """识别音频的函数，接收音频文件路径，返回识别的文本"""
    # res = rasr_example(audio_file_path)
    res = recognize_file(audio_file_path)
    if res:
        return res
    else:
        return '识别失败'

def recognize_audio_mutilrole(audio_file_path):
    roles,texts = recognize_file_mutilrole(audio_file_path)
    if roles and texts:
        return roles,texts
    else:
        return '识别失败'


def summarize_text(text):
    """总结文本的函数，返回总结结果"""
    res = langchain(text)
    if res:
        return res
    else:
        return '总结失败'
def summarize_text_mutilrole(text):
    """总结文本的函数，返回总结结果"""
    res = conservation(text)
    if res:
        return res
    else:
        return '总结失败'
# 初始化会话状态
if 'recognize' not in session_state:
    st.session_state.recognize = False
if 'transcription' not in session_state:
    st.session_state.transcription = ''
if 'recognize_mutil' not in session_state:
    st.session_state.recognize_mutil = False
if 'transcription_mutil_roles' not in session_state:
    st.session_state.transcription_mutil_roles = []
    st.session_state.transcription_mutil_texts = []
if 'path' not in session_state:
    st.session_state.path=False

st.title("📚 AI伴学助手")
st.write("智能录音与文本总结工具，帮助您更高效地记录和整理知识点。")

# 侧边栏选择功能模式
mode = st.sidebar.radio("选择功能模式", ("单人对话总结", "多人对话总结"))

# 录音文件保存路径
SAVE_DIR = "recordings"
os.makedirs(SAVE_DIR, exist_ok=True)

# 单人模式

if mode == "单人对话总结":
    st.subheader("🎤 单人对话总结")

    # 整体左右布局分区
    col1, col2 = st.columns(2)

    with col1:
        st.write("🎙️ **录音区域**")
        col3,col4,col5=st.columns([2, 7, 1])
        with col3:
            st.write("")
        with col4:
            audio_bytes = audio_recorder(pause_threshold=1.0, sample_rate=16000,text="",icon_size="10x")

        with col5:
            st.write("")

        audio_file_path = os.path.join(SAVE_DIR, "single_user_audio.wav")

        if audio_bytes and st.session_state.recognize == False:
            # 保存录音为文件
            with open(audio_file_path, "wb") as f:
                f.write(audio_bytes)
            # st.audio(audio_file_path, format="audio/wav")
            # st.success("录音已保存，正在识别文本...")

        if audio_bytes:
            st.audio(audio_file_path, format="audio/wav")
            st.success("文本识别完成！")
        if audio_bytes and st.session_state.recognize == False:
            # 自动调用音频识别
            try:
                st.session_state.transcription = recognize_audio(f'./output_16khz.wav')
                # st.session_state.transcription = '好，今天来。 讲一些独立与互斥。 到底有什么区？ 那么给大家。 一个非常经典的例子。 Ab护士。 与ab独立，我们可以理解为说。 两个男生共同去追。 追求一。 那么这两个男生呢？互看不顺眼。 正巧这个女生要过生日。 那么男生a说要是那个男生去的话，那我就不去了。 男生必说。 要是。 去的话那。 就不去了。 那么这个时候a和b。 他就是胡吃的这。 翅指的是互相排斥。 但是对于女。 当然来说，我又不喜欢你们两个，你们两个爱。 不来。 反正对。 对我没有影响。 这虽然是一个。 护士，但是这个时候。 他就是独立的。 因为。 你们两个来与不来，跟我没有任何的关系。 那么我们再从这个理论的角度去推。 推导一遍p a。 是大于零的。 大一点，那么假如说。 是独立的那。 卑鄙就等于。 A乘上。 那也就是说。 Maybe。 还是零的是推不出。 是互吃的，因为如果。 B，要是互斥的话。 Ab式空气。 那么pa。 就会等于零，那么现在。 大家是矛盾的，所以。 独立。 推不出。 你是互吃的。 那么假如。 A。 是互斥的。 那么。 就是空。 那所以。 Tab它就等于。 那pa。 它就不等于pa。 因为p和p。 其他都是大于零了，但是又矛盾了。 它是等于样的，那也就是说不会存在。 这个关系p a b。 就等于。 A乘上。 那也就是说。 Ab护士也是推不出ab。 是独立的。 那我们来做一个总结。 A b独立。 与互斥，他没有什么联系，也没有什么。 关系。 他们两个的出现。 是为了更好的区分事件。 如果说真的。 什么联系的话。 那么。 就是说独立的。 要。 乘法。 更简单。 因为可以。 拍成两个东西。 去相城嘛。 等于。 P a乘上。 那么互斥的出现它其实。 是让概率。 加法变得更简单了，那么希望同学们在以后的学习的过程当中要注意到这个。 不要混淆。 那么好，我们下期再见。'
                st.session_state.recognize = True
                # st.success("文本识别完成！")
            except Exception as e:
                st.error(f"音频识别过程中出现错误: {e}")

    with col2:
        st.write("📄 **识别结果**")
        st.text_area("⬇ 识别结果", value=st.session_state.transcription, height=250)
    if st.session_state.path== True:
        st.success("录音已保存，正在识别文本...")

    # 提交总结请求
    if st.button("📝 总结文本"):
        if len(st.session_state.transcription) > 0:
            try:
                st.subheader("总结结果")
                summary = summarize_text(st.session_state.transcription)
                for idx, (key, question) in enumerate(summary.items(), start=1):
                    with st.expander(f"知识点 {idx}"):
                        st.markdown(f"**知识点**: {question['知识点名']}")
                        st.markdown(f"**知识点讲解**: {question['知识点讲解']}")
                        st.markdown(f"**知识点例题**: {question['知识点例题']}")
                        st.success(f"正确答案: {question['例题答案']}")
                st.success("文本总结完成！")
            except Exception as e:
                st.error(f"文本总结过程中出现错误: {e}")
        else:
            st.warning("请先录音并完成文本识别后再总结。")

# 多人模式
elif mode == "多人对话总结":
    st.subheader("👥 多人对话总结")

    # 单一录音入口
    st.write("🎙️ **录音区域**")
    # col6,col7=columns([1,9])
    # with col6:
    audio_bytes = audio_recorder(pause_threshold=1.0, sample_rate=16000, key="mutilrole_recorder",text="",icon_size="6x")
    # with col7:
    # st.write("请录入你与学生的对话录音")
    st.markdown("<h5 style='color: black;'>💡请录入你与学生的对话录音</h5>", unsafe_allow_html=True)
    if audio_bytes and st.session_state.recognize_mutil == False:
        # 保存录音文件
        audio_file_path = os.path.join(SAVE_DIR, "mutilrole_audio.wav")
        with open(audio_file_path, "wb") as f:
            f.write(audio_bytes)
        st.audio(audio_file_path, format="audio/wav")
        st.success("录音已保存，正在识别文本...")

        # 调用多角色识别函数
        try:
            st.session_state.transcription_mutil_roles,st.session_state.transcription_mutil_texts = recognize_audio_mutilrole("mutilrole_course.wav")
            st.session_state.recognize_mutil = True
            st.success("文本识别完成！")
        except Exception as e:
            st.error(f"音频识别过程中出现错误: {e}")
    if len(st.session_state.transcription_mutil_roles)>0 :
        # 展示识别结果以左右对齐的对话形式
        st.markdown("### 识别结果")
        messages = st.container(height=450)

        # with messages:
        #     for message in st.session_state.messages:
        #         if message["role"] == "user":
        #             messages.chat_message("user").write(message["text"].replace("\\\\", "\\"))  # 修复LaTeX转义问题
        #         if message["role"] == "assistant":
        #             messages.chat_message("assistant").write(message["text"])
        for role, text in zip(st.session_state.transcription_mutil_roles, st.session_state.transcription_mutil_texts):
            if role == "USER":
                messages.chat_message("user").write(text)
                # # 左对齐样式
                # st.markdown(
                #     f"""
                #     <div style="text-align: left; background-color: #f0f8ff; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                #         <strong>{role}:</strong> {text}
                #     </div>
                #     """,
                #     unsafe_allow_html=True,
                # )
            elif role == "AGENT":
                messages.chat_message("assistant").write(text)
                # # 右对齐样式
                # st.markdown(
                #     f"""
                #     <div style="text-align: right; background-color: #fffacd; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                #         </strong> {text}:<strong>{role}
                #     </div>
                #     """,
                #     unsafe_allow_html=True,
                # )
    # 提交总结请求
        if st.button("📝 总结多人对话"):
            if st.session_state.transcription_mutil_roles and st.session_state.transcription_mutil_texts:
                try:
                    # 构建文本格式
                    combined_text = "\n".join([f"{role}: {text}" for role, text in zip(st.session_state.transcription_mutil_roles, st.session_state.transcription_mutil_texts)])

                    # 调用总结函数
                    summary = summarize_text_mutilrole(combined_text)
                    for idx, (key, question) in enumerate(summary.items(), start=1):
                        with st.expander(f"知识点 {idx}"):
                            st.markdown(f"**知识点**: {question['知识点名']}")
                            st.markdown(f"**知识点讲解**: {question['知识点讲解']}")
                            st.markdown(f"**知识点例题**: {question['知识点例题']}")
                            st.success(f"正确答案: {question['例题答案']}")
                    st.success("文本总结完成！")
                except Exception as e:
                    st.error(f"总结过程中出现错误: {e}")
            else:
                st.warning("请先完成文本识别后再总结。")