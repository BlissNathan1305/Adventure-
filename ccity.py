# List of 10 Chinese provinces with English and Chinese names
chinese_provinces = [
    {"English": "Anhui", "Chinese": ""},
    {"English": "Fujian", "Chinese": ""},
    {"English": "Gansu", "Chinese": ""},
    {"English": "Guangdong", "Chinese": ""},
    {"English": "Guizhou", "Chinese": ""},
    {"English": "Hainan", "Chinese": ""},
    {"English": "Hebei", "Chinese": ""},
    {"English": "Heilongjiang", "Chinese": ""},
    {"English": "Henan", "Chinese": ""},
    {"English": "Hubei", "Chinese": ""}
]

# Print the list of provinces
for i, province in enumerate(chinese_provinces, start=1):
    print(f"{i}. {province['English']} ({province['Chinese']})")
