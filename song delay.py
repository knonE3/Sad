import time

print("SADBOY")
print("DAMM!")
print("SAD SAD SAD")

lyrics = [
    "เธอสบายดีไหม",
    "เป็นคำถามที่ยังคงวนอยู่ซ้ำๆ",
    "อยากรู้แค่เพียงเธออยู่ตรงนั้น ที่ไม่มีฉัน",
    "ชีวิตเธอเป็นไง",
    "คิดถึงกันบ้างไหม",
    "ส่วนฉันก็คิดถึงเธออยู่ซ้ำๆ",
    "ก็หวังแค่เพียงเธออยู่ตรงนั้น",
    "จะสุขใจกว่าฉัน",
    "อยากให้เธอยิ้มได้เหมือนเก่า",
    "เหมือนตอนเรารักกัน"
]

delays = [3, 4.5, 6, 2, 3.5, 3.7, 2.87, 3.2, 3, 4]

for line, delay in zip(lyrics, delays):
    print(line)
    time.sleep(delay)
