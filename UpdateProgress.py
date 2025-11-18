import datetime
import re

# 计算十年进度
start = datetime.date(2025, 1, 1)
end = datetime.date(2035, 1, 1)
today = datetime.date.today()
total_days = (end - start).days
passed_days = (today - start).days
progress = min(max(passed_days / total_days, 0), 1)
percent = int(progress * 100)

# 生成 ASCII 进度条
def generate_progress_bar(length=30):
    # 使用粉色方块字符 ▓（GitHub 渲染偏粉色），未完成部分用 ░
    filled_length = int(progress * length)
    bar = '▓' * filled_length + '░' * (length - filled_length)
    return f'{{ {bar} }}'

progress_bar = generate_progress_bar()

# 生成 Markdown 内容
markdown_progress = f"""\
Progress: {progress_bar} {percent}%

Updated on {today.strftime('%Y-%m-%d')}
"""

# 更新 README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'<!--progress-->.*?<!--endprogress-->',
    f'<!--progress-->\n{markdown_progress}\n<!--endprogress-->',
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
