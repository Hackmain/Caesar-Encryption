# Caesar-Encryption
This a simple code for beginners  to learn how write code to apply the Caesar Cipher encryption
دعني أشرح لك هذا الكود البسيط لتشفير النصوص باستخدام تشفيرة قيصر (Caesar Cipher).

المبدأ العام:
تشفيرة قيصر هي تقنية تشفير بسيطة تستند إلى استبدال حروف النص الواضح بحروف أخرى بناءً على قيمة مفتاح (الانتقال) المحددة.
يتم تحديد مفتاح الانتقال بشكل يدوي، وهو عدد يحدد مقدار الانتقال بين الحروف.
الكود المعطى:
هذا الكود يحتوي على دالة caesar_cipher_encrypt التي تقوم بتشفير النص الواضح.
الخطوات الرئيسية في الكود:
يتم تمرير النص الواضح وقيمة المفتاح إلى الدالة.
يتم تحديد ما إذا كان الحرف حرفًا أبجديًا باستخدام char.isalpha().
يتم حساب الحرف المشفر باستخدام ord(char) + shift.
يتم التحقق من حدود الحروف الكبيرة والصغيرة (A-Z و a-z) وضبط القيمة إذا كانت أكبر من حدود الحروف.
يتم إضافة الحرف المشفر إلى النص المشفر.
الاستخدام:
يمكنك تشغيل البرنامج عن طريق تشغيل الدالة main().
سيطلب منك إدخال النص الواضح وقيمة المفتاح.
سيتم عرض النص المشفر.
مثال توضيحي:
إذا كان لدينا النص الواضح “Hello, World!” واستخدمنا مفتاحًا بقيمة 3، سيتم تشفيره إلى “Khoor, Zruog!”.
ملاحظة:
تشفيرة قيصر غير آمنة من الناحية الأمانية ويمكن فك تشفيرها بسهولة.
يُفضل استخدامها لأغراض تعليمية وتجريبية.
