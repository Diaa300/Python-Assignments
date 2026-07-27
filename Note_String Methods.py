# =================================================================
# 🐍 مرجع ميثودز النصوص الأسطوري (String Methods Reference) 🐍
# مجمع من دروس "Elzero Web School" بالتفصيل والتطبيق
# =================================================================

# -----------------------------------------------------------------
# 📁 الجزء الأول: التحكم في الحروف وحواف النصوص (Part 1)
# -----------------------------------------------------------------

# 1. strip() / lstrip() / rstrip()
# بتشيل المسافات الزايدة (أو حروف معينة) من الأطراف.
# strip: من الطرفين | lstrip: من الشمال بس | rstrip: من اليمين بس.
name = "   Diaa   "
print(name.strip())    # الناتج: "Diaa"
print(name.lstrip())   # الناتج: "Diaa   " (شال الفراغ اللي عالشمال بس)

# 2. title()
# بيخلي أول حرف من كل كلمة كابيتال (Capital)، والباقي سمول.
# ملحوظة: الحرف اللي بيجي بعد أي رقم أو رمز بيتحول لكابيتال برضه.
title_text = "welcome 2 egypt"
print(title_text.title())  # الناتج: "Welcome 2 Egypt"

# 3. capitalize()
# بيخلي أول حرف في الجملة كلها كابيتال، وباقي الجملة كلها سمول.
cap_text = "welcome to egypt"
print(cap_text.capitalize())  # الناتج: "Welcome to egypt"

# 4. zfill(Width)
# بيحط أصفار على الشمال عشان يخلي طول النص مساوي للرقم اللي حددته (مفيد لتنسيق الأرقام).
num = "15"
print(num.zfill(5))  # الناتج: "00015" (بيكمل الطول لـ 5 خانات)

# 5. upper()
# بيحول كل حروف النص لحروف كبيرة (Capital).
print("diaa".upper())  # الناتج: "DIAA"

# 6. lower()
# بيحول كل حروف النص لحروف صغيرة (Small).
print("DIAA".lower())  # الناتج: "diaa"


# -----------------------------------------------------------------
# 📁 الجزء الثاني: التقسيم، البحث، والعدّ (Part 2)
# -----------------------------------------------------------------

# 1. split() / rsplit()
# بيقسم النص لـ قائمة (List) بناءً على فاصل معين (الديفولت هو المسافة).
# وممكن تحدد في المعامل الثاني أقصى عدد مرات للتقسيم.
skills = "Python-HTML-CSS-JS"
print(skills.split("-"))       # الناتج: ['Python', 'HTML', 'CSS', 'JS']
print(skills.rsplit("-", 2))   # الناتج: ['Python-HTML', 'CSS', 'JS'] (بيقسم من اليمين مرتين بس)

# 2. center(Width, Fill_Char)
# بيخلي النص في النص وبيحط حشو يمين وشمال بالرمز والطول اللي بتحدده.
center_name = "Diaa"
print(center_name.center(10, "#"))  # الناتج: "###Diaa###" (إجمالي الطول 10 والحشو #)

# 3. count(Sub, Start, End)
# بيعد الكلمة أو الحرف اتكرر كام مرة في النص (وممكن تحدد بداية ونهاية البحث).
msg = "I love Python and Python is easy"
print(msg.count("Python"))  # الناتج: 2

# 4. swapcase()
# بيعكس حالة الحروف (الكابيتال بيبقى سمول، والسمول بيبقى كابيتال).
print("PyThOn".swapcase())  # الناتج: "pYtHoN"

# 5. startswith(Prefix, Start, End)
# بيتأكد: هل النص بيبدأ بكلمة أو حرف معين؟ وبيرجع True أو False.
hello_msg = "Hello Diaa"
print(hello_msg.startswith("Hello"))  # الناتج: True

# 6. endswith(Suffix, Start, End)
# بيتأكد: هل النص بينتهي بكلمة أو حرف معين؟ وبيرجع True أو False.
print(hello_msg.endswith("Diaa"))  # الناتج: True


# -----------------------------------------------------------------
# 📁 الجزء الثالث: التنسيق والبحث المتقدم (Part 3)
# -----------------------------------------------------------------

# 1. index(Sub, Start, End)
# بيبحث عن مكان الكلمة وبيرجع مكان أول حرف (مكان الـ Index).
# ⚠️ تحذير: لو الكلمة مش موجودة بيطلع خطأ (ValueError) ويوقف البرنامج!
search_text = "Learn Python with Elzero"
print(search_text.index("Python"))  # الناتج: 6

# 2. find(Sub, Start, End)
# نفس الـ index بالظبط، لكن لو الكلمة مش موجودة بيرجع -1 (ومش بيوقف البرنامج).
print(search_text.find("C++"))  # الناتج: -1

# 3. rjust(Width, Fill_Char) / ljust(Width, Fill_Char)
# بيعمل محاذاة للنص لليمين أو الشمال، وبيملى الفراغ بالرمز اللي بتحدده.
name_adjust = "Diaa"
print(name_adjust.rjust(10, "@"))  # الناتج: "@@@@@@Diaa" (محاذاة لليمين)
print(name_adjust.ljust(10, "#"))  # الناتج: "Diaa######" (محاذاة للشمال)

# 4. splitlines()
# بيقسم النص لـ قائمة (List) بناءً على السطور الجديدة (الـ New Lines).
multi_lines = """Frist Line
Second Line
Third Line"""
print(multi_lines.splitlines())  # الناتج: ['Frist Line', 'Second Line', 'Third Line']


# -----------------------------------------------------------------
# 📁 الجزء الرابع: التجميع، الاستبدال، والتحقق (Part 4)
# -----------------------------------------------------------------

# 1. join(Iterable)
# بيجمع عناصر القائمة (List) ويحولها لنص واحد، وبيربط بينهم بالفاصل اللي بتحدده.
words_list = ["Diaa", "studies", "Python"]
print(" ".join(words_list))  # الناتج: "Diaa studies Python" (الفاصل هنا مسافة)

# 2. replace(Old, New, Count)
# بيستبدل جزء من النص بكلمة تانية، وممكن تحدد عدد مرات الاستبدال كحد أقصى.
counting = "One Two One Two"
print(counting.replace("One", "Three", 1))  # الناتج: "Three Two One Two" (استبدل أول "One" بس)

# 3. دوال التحقق (is-methods)
# دوال بتسألها عن حالة النص وبترجعلك دايماً True أو False:
print("diaa".islower())      # True  (هل النص كله حروف صغيرة؟)
print("DIAA".isupper())      # True  (هل النص كله حروف كبيرة؟)
print("Diaa".istitle())      # True  (هل الكلمة منسقة كعنوان؟ أول حرف كابيتال)
print("   ".isspace())       # True  (هل النص عبارة عن مسافات فارغة فقط؟)
print("Python3".isalnum())   # True  (هل النص حروف وأرقام فقط؟ بدون رموز أو مسافات)
print("Python".isalpha())    # True  (هل النص حروف فقط؟)
print("12345".isdigit())     # True  (هل النص أرقام فقط؟)