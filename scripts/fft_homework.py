import numpy as np
import matplotlib.pyplot as plt
import os

fs = 1000       # 采样率（Hz）
duration = 1.0  # 信号时长（秒）
f0 = 20 + 37    # 把 37 换成你的学号后两位
noise = 0.8     # 噪声大小
t = np.arange(0, duration, 1 / fs)
x = np.sin(2 * np.pi * f0 * t) + noise * np.random.default_rng().normal(size=t.size)
spectrum = np.abs(np.fft.rfft(x))
freqs = np.fft.rfftfreq(t.size, 1 / fs)

peak_idx = np.argmax(spectrum)
print(f"Peak frequency: {freqs[peak_idx]:.1f}Hz")

fig, axes = plt.subplots(2, 1)

first_02s = t < 0.2
axes[0].plot(t[first_02s], x[first_02s])
axes[0].set_title(f"Waveform (first 0.2 s), f0 = {f0} Hz")
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Amplitude")

axes[1].plot(freqs, spectrum)
axes[1].set_title("Magnitude spectrum (rfft)")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Magnitude")
axes[1].set_xlim(0, fs / 2)

fig.tight_layout()
os.makedirs("output", exist_ok=True)
plt.savefig("output/fft.png", dpi=150)
plt.close(fig)
# 1. 生成时间轴 t：np.arange(0, duration, 1 / fs)
# 2. 生成信号 x：np.sin(2 * np.pi * f0 * t) 加上噪声
#    噪声写法：noise * np.random.default_rng().normal(size=t.size)
# 3. 算频谱：np.abs(np.fft.rfft(x))
# 4. 算每个点对应的频率：np.fft.rfftfreq(t.size, 1 / fs)
# 5. 用 np.argmax 找频谱最高点的下标，打印这个下标对应的频率
# 6. 用 plt.subplots(2, 1) 上下画两张图：
#    上图是前 0.2 秒的波形，下图是频谱，用 plt.savefig("output/fft.png") 保存
