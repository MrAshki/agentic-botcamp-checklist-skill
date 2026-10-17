# محتوای اصلی جلسه ۱

## ۱. پیام اصلی

مدل و Agent فقط عدد می‌بینند. کیفیت تبدیل واقعیت به عدد، سقف کیفیت سیستم بعدی را تعیین می‌کند.

مسیر جلسه چنین است:

`منبع داده -> ذخیره‌سازی -> تمیزکاری -> کاوش -> پیش‌پردازش -> اعتبارسنجی -> نمودار و گزارش -> استقرار`

## ۲. پنج ویژگی داده بزرگ

- Volume: حجم داده
- Velocity: سرعت تولید و دریافت داده
- Variety: تنوع قالب‌ها
- Veracity: میزان صحت و عدم قطعیت
- Value: ارزش قابل تبدیل به تصمیم

تمرکز جلسه بیشتر بر Veracity است. چهار مورد اول هزینه و پیچیدگی ایجاد می‌کنند. Value دلیل تحمل این هزینه است.

## ۳. طیف ساختار داده

- Structured: جدول دارای Schema ثابت، مانند سفارش و تراکنش
- Semi-structured: ساختار منعطف، مانند JSON، XML و Log
- Unstructured: متن، تصویر، صدا، ویدیو و PDF

ساختار داده انتخاب ابزار را تغییر می‌دهد. SQL و pandas برای جدول مناسب‌اند. `json_normalize` برای JSON تو در تو کاربرد دارد. مدل‌های زبانی، Embedding و Deep Learning برای داده بدون ساختار مهم‌اند.

## ۴. هشت چهره داده

| نوع | نمایش | کارهای رایج |
|---|---|---|
| Tabular | سطر و ستون | Classification و Regression |
| Text | دنباله Token | Sentiment، Summarization و RAG |
| Image | آرایه Pixel | Classification و Object Detection |
| Audio | دامنه صدا در زمان | Speech-to-Text و Speaker ID |
| Video | دنباله Frame همراه صدا | Action Recognition و Tracking |
| Time Series | مقدار در زمان‌های پی‌درپی | Forecasting و Anomaly Detection |
| Spatial | مختصات جغرافیایی | Route Optimization و Land Use |
| Network | Node و Edge | Link Prediction و Recommendation |

## ۵. واژگان پایه

در داده جدولی:

- Row می‌تواند Observation، Record یا Sample نامیده شود.
- Column می‌تواند Variable، Field، Attribute یا Feature نامیده شود.
- ستونی که پیش‌بینی می‌شود Target، Label یا `y` است.
- سایر ویژگی‌ها معمولا در ماتریس `X` قرار می‌گیرند.

در داده متنی:

- Token: کوچک‌ترین واحدی که مدل می‌بیند.
- Document: یک واحد متنی مستقل.
- Corpus: مجموعه Documentها.
- Corpora: چند Corpus مستقل.

## ۶. قالب فایل و انتخاب آن

- CSV: ساده، انسان‌خوان و سازگار؛ برای داده بزرگ کند و حجیم
- JSON: مناسب API، داده تو در تو و خروجی Agent
- Parquet: مناسب تحلیل ستونی و داده بزرگ
- Feather: مناسب جابه‌جایی سریع و موقت بین برنامه‌های پایتون
- Pickle: فقط برای شیئی که منبع آن قابل اعتماد است
- Safetensors: ذخیره امن‌تر و سریع وزن مدل

هشدار دوره: `pickle.load` روی فایل ناشناس می‌تواند کد اجرا کند.

Container با Codec فرق دارد. MP4 و MKV ظرف‌اند. H.264 و H.265 روش فشرده‌سازی هستند. Lossy بخشی از اطلاعات را حذف می‌کند. Lossless اطلاعات را حفظ می‌کند.

## ۷. منابع داده

خانواده‌های اصلی:

- پورتال‌های داده باز دولتی و بین‌المللی
- مخازن Dataset برای آموزش و Benchmark
- داده داخلی سازمان مانند پایگاه داده، Warehouse، Lake و Log
- منابع علمی، تخصصی، تجاری و APIها

برای پروژه واقعی، داده داخلی سازمان اغلب ارزشمندترین منبع است.

نردبان دریافت داده از ساده به پیچیده:

1. دانلود فایل
2. خواندن مستقیم از URL
3. API
4. Web Scraping
5. اتصال مستقیم به پایگاه داده

اگر API وجود دارد، از Scraping استفاده نکنید. پیش از Scraping، `robots.txt` و شرایط استفاده را بررسی کنید و سرعت درخواست را محدود کنید.

## ۸. JSON، Metadata و Data Dictionary

JSON قالب رایج API و Tool Call است. خروجی باید خوانده، اعتبارسنجی و در صورت نیاز تخت شود.

Metadata داده درباره داده است:

- Descriptive: عنوان، سازنده، تاریخ و کلیدواژه
- Structural: Schema، نوع ستون و رابطه جدول‌ها
- Administrative: مالک، مجوز، سطح دسترسی و تاریخ ایجاد

Metadata می‌تواند حساس‌تر از محتوای اصلی باشد. EXIF عکس می‌تواند زمان، دستگاه و موقعیت GPS را افشا کند.

Data Dictionary برای هر ستون این موارد را ثبت می‌کند:

- نام
- نوع
- معنا
- بازه یا مقدارهای مجاز
- مالک، مجوز یا محدودیت در صورت نیاز

این سند از تفسیر غلط جلوگیری می‌کند و Context لازم را به Text-to-SQL Agent می‌دهد.

## ۹. Data Pipeline

مرحله‌های اصلی:

1. Collection
2. Storage
3. Cleaning
4. Exploration
5. Preprocessing
6. Validation
7. Visualization
8. Deployment

پیش از تمیزکاری بپرسید:

- چه کسی داده را جمع کرده است؟
- با چه ابزار و فرایندی جمع شده است؟
- برای چه هدفی ثبت شده است؟

## ۱۰. EDR و EDA

EDR بررسی سریع ساختار و محتوای داده است. ابزارهای اصلی pandas:

- `shape`
- `head`، `tail` و `sample`
- `columns`
- `info`
- `describe`
- `nunique`
- `value_counts`

EDA عمیق‌تر است و با نمودار و آزمون آماری دنبال الگو می‌گردد.

پرچم‌های قرمز EDR:

- تاریخ با نوع متن
- عدد ذخیره‌شده به‌شکل متن
- مقدار غیرممکن
- ستون تک‌مقداری
- شناسه‌ای که اشتباه به‌عنوان Feature استفاده می‌شود
- اختلاف زیاد mean و median

## ۱۱. Missing Value

نمایش‌های رایج: `NaN`، `None`، `NaT` و `pd.NA`. رشته‌های `""`، `"NA"`، `"NULL"` و `"?"` باید در صورت درست‌بودن معنا به Missing واقعی تبدیل شوند.

سه سازوکار:

- MCAR: گم‌شدن کاملا تصادفی
- MAR: گم‌شدن با ستون‌های دیگر قابل توضیح است
- MNAR: گم‌شدن به خود مقدار گم‌شده وابسته است

راه‌های برخورد:

- حذف سطر یا ستون
- median یا mean برای عدد
- mode یا دسته `Unknown` برای دسته‌ای
- Forward Fill یا Backward Fill برای سری زمانی، اگر منطق مسئله اجازه دهد
- KNN یا مدل پیش‌بینی برای روش پیشرفته‌تر
- افزودن Missing Indicator وقتی گم‌بودن خود اطلاعات دارد

## ۱۲. تکراری و Outlier

تکراری دقیق با `duplicated` پیدا می‌شود. Near-duplicate به نرمال‌سازی متن یا روش تطبیق نیاز دارد.

Outlier می‌تواند خطا یا رخداد واقعی مهم باشد. دو روش تشخیص معرفی‌شده:

- IQR و Box Plot
- Z-score برای توزیع تقریبا نرمال

اقدام ممکن:

- اعتبارسنجی با منبع
- حذف فقط در صورت خطای تأییدشده
- Clip یا Winsorize
- تبدیل مانند log یا sqrt
- Robust Scaler

در کشف تقلب یا خرابی، Outlier ممکن است خود پاسخ باشد.

## ۱۳. شکل توزیع

Skewness میزان نامتقارن‌بودن توزیع است. اختلاف mean، median و mode می‌تواند نشانه آن باشد.

تبدیل‌های معرفی‌شده:

- `log1p` برای داده نامنفی با چولگی شدید راست
- `sqrt` برای چولگی متوسط و داده نامنفی
- Box-Cox برای مقدار مثبت
- Yeo-Johnson برای مقدارهای مثبت، صفر و منفی

## ۱۴. همبستگی

- Pearson: رابطه خطی دو متغیر عددی
- Spearman: رابطه یکنوا و داده رتبه‌ای؛ مقاوم‌تر به Outlier
- Kendall's tau: داده رتبه‌ای یا نمونه کوچک
- Point-biserial: متغیر دودویی و عددی
- Cramér's V: دو متغیر دسته‌ای

همبستگی صفر فقط نبود رابطه خطی را نشان می‌دهد. نبود رابطه را ثابت نمی‌کند. همبستگی نیز علیت را ثابت نمی‌کند.

## ۱۵. Encoding

ابتدا مشخص کنید دسته Nominal است یا Ordinal.

- One-hot: دسته Nominal با تعداد کم
- Dummy: نسخه One-hot با حذف دسته مرجع
- Effect: بیشتر برای تحلیل آماری
- Label: می‌تواند ترتیب کاذب ایجاد کند
- Ordinal: دسته دارای ترتیب واقعی
- Count: دسته با Cardinality بالا
- Binary: کاهش تعداد ستون با تفسیرپذیری کمتر
- Target: فقط داخل Cross-validation برای جلوگیری از Leakage

## ۱۶. Scaling

قاعده اصلی: Scaler فقط روی Train فیت می‌شود و روی Validation و Test فقط Transform انجام می‌شود.

- Min-Max: نگاشت به بازه مشخص؛ حساس به Outlier
- Standardization: میانگین صفر و انحراف معیار یک
- Robust: استفاده از median و IQR؛ مقاوم‌تر به Outlier

معمولا Scaling برای KNN، K-Means، SVM، مدل خطی، شبکه عصبی و PCA مهم است. درخت تصمیم، Random Forest و مدل‌های Boosting درختی معمولا به آن نیاز ندارند.

## ۱۷. Feature Engineering

چهار ستون:

- Transformation: Scaling، log و Encoding
- Selection: Correlation و Feature Importance
- Creation: Ratio، Aggregation و اجزای تاریخ
- Extraction: PCA و Embedding

Feature خوب از سؤال کسب‌وکار می‌آید. نمونه‌ها:

- روز هفته، ماه و تعطیلات از تاریخ
- `days_to_ship`
- `profit_margin`
- `is_returned`
- RFM مشتری
- sin و cos برای متغیر زمان چرخه‌ای

ابتدا Baseline بسازید. سپس اثر هر Feature را جدا بسنجید. Feature دارای اطلاعات آینده یا Target باعث Leakage می‌شود.

## ۱۸. تقسیم داده و Leakage

تقسیم نمونه جلسه:

- Train: ۷۰٪
- Validation: ۱۵٪
- Test: ۱۵٪

Test فقط یک‌بار و در پایان استفاده می‌شود. برای داده طبقه‌بندی، Stratify نسبت کلاس‌ها را حفظ می‌کند. برای سری زمانی، گذشته برای Train و آینده برای Test است؛ Shuffle تصادفی مناسب نیست.

انواع Leakage:

- فیت پیش‌پردازش روی کل داده پیش از Split
- Feature ساخته‌شده پس از رخداد هدف
- تکراری میان Train و Test
- استفاده از آینده برای پیش‌بینی گذشته یا حال

راه اصلی کاهش ریسک، قرار دادن پیش‌پردازش و مدل در Pipeline است.

## ۱۹. پیوند داده با Agent

- RAG یک Data Pipeline برای متن دارد: پاک‌سازی، حذف تکراری، Chunking، Metadata و Embedding.
- Tool Call معمولا JSON می‌دهد و به خواندن، اعتبارسنجی و تخت‌سازی نیاز دارد.
- Text-to-SQL به Schema تمیز و Data Dictionary نیاز دارد.
- Evaluation به Dataset پاسخ درست و Split سالم نیاز دارد.

قانون جلسه:

`Garbage In, Garbage Out`

نسخه Agentic:

`Garbage In, Confident Garbage Out`

