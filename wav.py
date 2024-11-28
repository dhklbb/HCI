import wave

# 打开 WAV 文件
with wave.open('test2.wav', 'rb') as wav_file:
    # 获取采样率
    sample_rate = wav_file.getframerate()
    # 获取采样宽度（字节数）
    sample_width = wav_file.getsampwidth()
    # 计算位深（位数）
    bit_depth = sample_width * 8

    print(f"采样率: {sample_rate} Hz")
    print(f"位深: {bit_depth} 位")

from pydub import AudioSegment

# 读取原始 WAV 文件
audio = AudioSegment.from_wav("test2.wav")

# 将采样率更改为 16kHz
audio_16k = audio.set_frame_rate(8000)

# 保存为新的 WAV 文件
audio_16k.export("test2_8khz.wav", format="wav")

print("重采样完成，已保存为 output_8khz.wav")

with wave.open('test2_8khz.wav', 'rb') as wav_file:
    # 获取采样率
    sample_rate = wav_file.getframerate()
    # 获取采样宽度（字节数）
    sample_width = wav_file.getsampwidth()
    # 计算位深（位数）
    bit_depth = sample_width * 8

    print(f"采样率: {sample_rate} Hz")
    print(f"位深: {bit_depth} 位")


# import wave
#
# # 打开 WAV 文件
# with wave.open("test2.wav", "rb") as wav_file:
#     # 获取声道数
#     channels = wav_file.getnchannels()
#
#     # 判断单声道还是双声道
#     if channels == 1:
#         print("该 WAV 文件是单声道（Mono）")
#     elif channels == 2:
#         print("该 WAV 文件是双声道（Stereo）")
#     else:
#         print(f"该 WAV 文件有 {channels} 个声道")
