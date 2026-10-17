# امنیت، ارزیابی و استقرار

## تهدیدهای اصلی

Prompt Injection می‌تواند مستقیم در پیام کاربر یا غیرمستقیم در سند، وب، ایمیل و خروجی ابزار باشد. Agent به‌دلیل دسترسی به ابزار و داده، سطح خطر بیشتری از Chatbot ساده دارد.

تهدیدهای OWASP مطرح‌شده شامل این موارد هستند:

- Agent Goal Hijack
- Tool Misuse
- Identity and Privilege Abuse
- Supply-chain Risk
- Unexpected Code Execution
- Memory and Context Poisoning
- Insecure Inter-agent Communication
- Cascading Failure
- Rogue Agent
- Human-Agent Trust Exploitation

سه عامل پرخطر کنار هم عبارت‌اند از دسترسی به داده خصوصی، دریافت محتوای نامطمئن و امکان ارتباط یا اقدام بیرونی.

## دفاع چندلایه

1. ورودی: اعتبارسنجی، تشخیص Injection و کنترل فایل
2. مدل و Prompt: دستور صریح، مرزبندی داده و کاهش اختیار
3. ابزار: Allowlist، Schema، کمترین مجوز و جداسازی کلیدها
4. اجرا: Sandbox، Timeout، Rate Limit، سقف قدم و Idempotency
5. خروجی: اعتبارسنجی Schema، فیلتر PII و کنترل سیاست
6. انسان و عملیات: تأیید پیش از عمل حساس، Audit Log، Kill Switch و Red Teaming

هیچ لایه به‌تنهایی کافی نیست. اجرای `plan -> validate -> execute` از اجرای مستقیم متن مدل امن‌تر است.

## ارزیابی Agent

سطوح ارزیابی:

- Unit: Prompt، Tool و جزء منفرد
- Trajectory: مسیر و ترتیب تصمیم‌ها
- Outcome: نتیجه نهایی
- Safety: تزریق، افشای PII و سوءاستفاده از ابزار
- Human Review: بررسی نمونه‌های حساس

معیارها می‌توانند شامل Task Success Rate، Tool-call Accuracy، هزینه، تعداد قدم، تأخیر P50/P95، نرخ خطا، کیفیت استناد و نرخ ارجاع به انسان باشند.

Golden Set باید ورودی، نتیجه موردانتظار و معیار روشن داشته باشد. تغییر مدل، Prompt یا ابزار باید با همان مجموعه ارزیابی شود.

## مشاهده‌پذیری

Trace باید مسیر Prompt، مدل، Tool Call، پاسخ ابزار، خطا و نتیجه را به یک اجرای واحد وصل کند. Log، Metric و Trace اطلاعات مکمل هستند. Secret، Token و داده شخصی نباید در آن‌ها ثبت شوند.

## چک‌لیست پیش از Production

- Context و Prompt نسخه‌بندی شده‌اند.
- خروجی مدل Schema و اعتبارسنجی دارد.
- Timeout، Retry، Backoff و Fallback تعریف شده‌اند.
- عملیات نوشتن تأیید و Idempotency دارند.
- Secretها بیرون از کد و مخزن هستند.
- نقش و دسترسی ابزارها محدود است.
- Golden Set و Gate انتشار وجود دارند.
- Audit، هزینه، تأخیر و خطا پایش می‌شوند.
- Rollback، Runbook و Kill Switch آماده‌اند.
- نسخه مدل، ابزار و Prompt ثبت می‌شود.

## Rollout مرحله‌ای

مسیر پیشنهادی شامل Shadow، Canary و سپس انتشار کامل است. Feature Flag و معیار توقف اجازه می‌دهند در صورت افت کیفیت یا افزایش خطا، تغییر متوقف یا بازگردانده شود.

