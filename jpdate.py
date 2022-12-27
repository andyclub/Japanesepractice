import random
import calendar

# I asked ChatGPT a question:
# Python代码，随机生成一个日期，输出这个日期的年、月、日、星期几，另起一行输出这个日期的日本语罗马音
# But the code I got was so terrible.
# Thus, here's my Code refactoring.

from datetime import date, timedelta
# 随机生成一个日期
d1 = date.today()
d2 = d1 + timedelta(days=random.randint(-5650, 465))

# 输出日本语罗马音
year_romaji = ""
kana_dict = {
	0: "ぜろ（れい）",
	1: "いち",
	2: "に",
	3: "さん",
	4: "し",
	5: "ご",
	6: "ろく",
	7: "なな（しち）",
	8: "はち",
	9: "きゅう"
}
for digit in str(d2.year):
    year_romaji += kana_dict[int(digit)]

month_dict = {
		1:"いちがつ",
		2:"にがつ",
		3:"さんがつ",
		4:"しがつ",
		5:"ごがつ",
		6:"ろくがつ",
		7:"しちがつ",
		8:"はちがつ",
		9:"きゅうがつ",
		10:"じゅうがつ",
		11:"じゅういちがつ",
		12:"じゅうにがつ"
}
month_romaji = month_dict[d2.month]
day_dict = {
	1: "いちにち（いちにち）",
	2:"ふつか",
	3:"みっか",
	4:"よっか",
	5:"いつか",
	6:"むいか",
	7:"なのか",
	8:"ようか",
	9:"ここのか",
	10:"とおか",
	11:"じゅういちにち",
	12:"じゅうににち",
	13:"じゅうさんにち",
	14:"じゅうよっか",
	15:"じゅうごにち",
	16:"じゅうろくにち",
	17:"じゅうしちにち",
	18:"じゅうはちにち",
	19:"じゅうきゅうにち",
	20:"にじゅうにち",
	21:"にじゅういちにち",
	22:"にじゅうににち",
	23:"にじゅうさんにち",
	24:"にじゅうしにち（にじゅうよっか）",
	25:"にじゅうごにち",
	26:"にじゅうろくにち",
	27:"にじゅうしちにち",
	28:"にじゅうはちにち",
	29:"にじゅうきゅうにち",
	30:"さんじゅうにち（みそか）",
	31:"さんじゅういちにち"
}
day_romaji =day_dict[d2.day]
weekday_dict = {
    0: "日曜日　にちようび",
    1: "月曜日　げつようび",
    2: "火曜日　かようび",
    3: "水曜日　すいようび",
    4: "木曜日　もくようび",
    5: "金曜日　きんようび",
    6: "日曜日　にちようび"
}
weekday_romaji = weekday_dict[d2.weekday()]
print(year_romaji + "年(とし) " + month_romaji + " " + day_romaji + " " + weekday_romaji)

# 输出日期的年、月、日、星期几
str_year = ""
for n in range(0, len(year_romaji)):
	str_year = str_year + "  "
str_month = "   "
for n in range(0, len(month_romaji)):
	str_month = str_month + "  "
print(str_year, d2.year,"年 ", str_month , d2.month, "月" , d2.day , "日 星期" , calendar.day_name[d2.weekday()])
