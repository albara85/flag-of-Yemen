import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# إنشاء شكل ورسم
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('skyblue')

# ألوان علم اليمن
yemen_colors = ['red', 'white', 'black']

# إضافة المستطيلات التي تمثل ألوان العلم
bars = [ax.add_patch(plt.Rectangle((-2, 0.33*i), 4, 0.33, color=color)) for i, color in enumerate(yemen_colors)]

# تحديد حدود المحاور
ax.set_xlim(-2, 2)
ax.set_ylim(0, 1)

# إخفاء المحاور
ax.axis('off')

def init():
    """تهيئة الرسم التوضيحي"""
    for bar in bars:
        bar.set_width(0)  # بدء المستطيلات بعرض 0
    return bars

def animate(i):
    """تحديث العرض المتحرك"""
    for j, bar in enumerate(bars):
        bar.set_width(4 * (i / 100))  # زيادة عرض المستطيلات تدريجياً
    return bars

# إنشاء الرسوم المتحركة
anim = FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# عرض الرسوم المتحركة مباشرة
plt.show()
