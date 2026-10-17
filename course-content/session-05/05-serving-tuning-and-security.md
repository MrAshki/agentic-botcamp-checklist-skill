# Serving، Fine-tune، هم‌ترازی و امنیت

## Serving

Serving مدل باید API سازگار، Health Check، محدودیت درخواست، Queue، Timeout و مشاهده‌پذیری داشته باشد. روش‌هایی مانند Continuous Batching، PagedAttention و Prefix Cache می‌توانند Throughput را بهتر کنند.

برای Production باید این موارد اندازه‌گیری شوند:

- زمان تا اولین Token
- Token بر ثانیه
- Latency در صدک‌های P50 و P95
- Throughput در بار هم‌زمان
- مصرف RAM یا VRAM
- نرخ خطا و OOM
- هزینه هر وظیفه

## Fine-tune

روش‌های مطرح:

- Full Fine-tune
- LoRA و QLoRA
- SFT
- روش‌های ترجیحی مانند DPO

Fine-tune زمانی مناسب است که تغییر رفتاری پایدار، سبک یا مهارت خاص با داده کافی لازم باشد. برای دانش تازه یا سند متغیر، RAG اغلب مناسب‌تر است. آموزش مدل فقط به‌دلیل در دسترس‌بودن GPU توجیه ندارد.

## RLHF و روش‌های هم‌ترازی

مسیرهای مطرح شامل SFT، Reward Model، RLHF با PPO، DPO، GRPO، RLVR و Constitutional AI هستند. این حوزه سریع تغییر می‌کند. انتخاب روش به داده ترجیحی، معیار، بودجه و توان پژوهشی نیاز دارد.

Reward Hacking و افت قابلیت‌های پایه باید ارزیابی شوند.

## Harness

Harness لایه‌ای پیرامون مدل است که آن را به Agent قابل‌کنترل تبدیل می‌کند. این لایه می‌تواند شامل موارد زیر باشد:

- قالب Prompt و خروجی ساختاریافته
- Context، حافظه و RAG
- Tool Calling و MCP
- Guardrail و Hook
- Sandbox و مجوزها
- Trace، هزینه و بودجه
- Retry، Timeout و شرط توقف
- Eval و Golden Set

کیفیت Agent فقط کیفیت مدل نیست. Harness ضعیف می‌تواند مدل قوی را به سامانه نامطمئن تبدیل کند.

## امنیت مدل محلی

- فایل مدل را از منبع معتبر دریافت کنید.
- Hash و نسخه را ثبت کنید.
- قالب امن مانند `safetensors` یا GGUF را به قالب‌های اجرایی ناشناس ترجیح دهید.
- `trust_remote_code=True` را فقط برای منبع بررسی‌شده فعال کنید.
- Runtime و درایور را به‌روز نگه دارید.
- سرویس Ollama یا vLLM را بدون احراز هویت روی اینترنت باز نکنید.
- مدل و ابزار را در Sandbox و با کمترین مجوز اجرا کنید.
- Prompt Injection، خروجی ابزار و نشت PII را آزمایش کنید.
- مجوز مدل و داده Fine-tune را بررسی کنید.

