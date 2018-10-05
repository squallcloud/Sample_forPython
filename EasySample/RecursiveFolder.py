# 再帰的にファイル・ディレクトリを探索する
from pathlib import Path

rootPath = 'C:/Users/cloud/Desktop/Multipurpose/Programming'

p = Path(rootPath)

# list(p)

# dir_A直下のファイルとディレクトリを取得
# Path.glob(pattern)はジェネレータを返す。結果を明示するためlist化しているが、普段は不要。
# l = list(p.glob("*"))
# for x in l:
#   print(x)

# ファイル名の条件指定
# l = list(p.glob("*.txt"))
# for x in l:
#   print(x)

# 再帰的な検索
l = list(p.glob("**/*"))
for x in l:
  print(x)
