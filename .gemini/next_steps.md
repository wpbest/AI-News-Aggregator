# 🚀 AI News Aggregator - Setup Complete! Next Steps

## ✅ What's Done

- ✅ Python 3.12 installed
- ✅ Dependencies installed (134 packages via `uv`)
- ✅ API keys configured in `.env`
- ✅ Email credentials configured

## 🔧 What's Needed: Start Docker

### Issue
Docker is installed but **not running**. You need to start Docker Desktop.

### Solution

**Option 1: Start Docker Desktop (Recommended)**
1. Open **Docker Desktop** from Start Menu
2. Wait for it to fully start (whale icon in system tray)
3. Then continue with the steps below

**Option 2: Start Docker via Command**
```powershell
# Start Docker Desktop
Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
```

---

## 📋 Complete Setup Steps

Once Docker is running, follow these steps:

### Step 1: Start PostgreSQL Database

```bash
cd docker
docker-compose up -d
cd ..
```

**Expected output:**
```
Creating network "docker_default" with the default driver
Creating volume "docker_postgres_data" with default driver
Creating ai-news-aggregator-db ... done
```

### Step 2: Wait for Database to be Ready

```bash
# Wait ~10 seconds for PostgreSQL to start
timeout /t 10
```

### Step 3: Create Database Tables

```bash
python -m uv run python app/database/create_tables.py
```

**Expected output:**
```
Tables created successfully
```

### Step 4: Run the AI News Aggregator!

```bash
# Run with default settings (24 hours, top 10 articles)
python -m uv run python main.py

# Or customize the time range and number of articles
python -m uv run python main.py 48 15  # 48 hours, top 15 articles
```

---

## 🎯 What the Pipeline Will Do

```
[1/5] Scraping articles from sources
  ├─ YouTube videos from configured channels
  ├─ OpenAI blog articles
  └─ Anthropic blog articles (news, research, engineering)

[2/5] Processing Anthropic markdown
  └─ Converting article URLs to markdown

[3/5] Processing YouTube transcripts
  └─ Fetching video transcripts

[4/5] Creating digests for articles
  └─ AI-powered summaries using GPT-4o-mini

[5/5] Generating and sending email digest
  ├─ Ranking articles using GPT-4.1
  ├─ Selecting top N articles
  ├─ Generating personalized introduction
  └─ Sending HTML email to your inbox
```

---

## ⏱️ Expected Runtime

- **First run:** 5-15 minutes (depending on number of articles)
- **Subsequent runs:** 2-5 minutes (fewer new articles)

---

## 📧 Check Your Email!

After the pipeline completes successfully, check your email inbox for:

**Subject:** `Daily AI News Digest - [Date]`

The email will contain:
- Personalized greeting
- Overview of top articles
- Top 10 ranked articles with summaries
- Links to full articles

---

## 🐛 Troubleshooting

### Docker won't start
- **Solution:** Open Docker Desktop manually
- **Check:** Look for whale icon in system tray
- **Wait:** Give it 30-60 seconds to fully start

### "Connection refused" to PostgreSQL
- **Cause:** Database not ready yet
- **Solution:** Wait 10 seconds and try again
- **Check:** Run `docker ps` to see if container is running

### "No articles found"
- **Cause:** No new articles in the specified time range
- **Solution:** Increase hours: `python -m uv run python main.py 72 10`

### Email not sending
- **Check:** Verify `MY_EMAIL` and `APP_PASSWORD` in `.env`
- **Test:** Run the email test from the setup guide
- **Gmail:** Make sure App Password is correct (16 characters)

### API rate limits
- **Cause:** Too many OpenAI API calls
- **Solution:** Wait a few minutes and try again
- **Prevention:** Reduce number of articles or time range

---

## 🎨 Customization

### Change YouTube Channels

Edit `app/config.py`:

```python
YOUTUBE_CHANNELS = [
    "UCawZsQWqfGSbCI5yjkdVkTA",  # Matthew Berman
    "UCn8ujwUInbJkBhffxqAPBVQ",  # Dave Ebbelaar (uncomment)
    # Add more channel IDs here
]
```

### Modify User Profile

Edit `app/profiles/user_profile.py` to customize:
- Your name
- Interests
- Expertise level
- Content preferences

This affects how articles are ranked!

### Schedule Daily Runs

**Windows Task Scheduler:**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily at 8:00 AM
4. Action: Start a program
5. Program: `python`
6. Arguments: `-m uv run python main.py`
7. Start in: `C:\Users\willi\OneDrive\Documents\GitHub\ai-news-aggregator`

---

## 📊 Monitoring

### Check Database

```bash
# Connect to PostgreSQL
docker exec -it ai-news-aggregator-db psql -U postgres -d ai_news_aggregator

# View tables
\dt

# Count articles
SELECT COUNT(*) FROM youtube_videos;
SELECT COUNT(*) FROM openai_articles;
SELECT COUNT(*) FROM anthropic_articles;
SELECT COUNT(*) FROM digests;

# Exit
\q
```

### View Logs

The pipeline outputs detailed logs to console:
- ✓ Success messages in green
- ✗ Error messages in red
- Progress indicators for each step

---

## 🚀 Quick Start Commands

```bash
# 1. Start Docker Desktop (manually or via command)
Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"

# 2. Wait for Docker to start, then run:
cd c:\Users\willi\OneDrive\Documents\GitHub\ai-news-aggregator

# 3. Start PostgreSQL
cd docker
docker-compose up -d
cd ..

# 4. Create tables (first time only)
python -m uv run python app/database/create_tables.py

# 5. Run the pipeline!
python -m uv run python main.py
```

---

## 🎉 You're All Set!

Everything is configured and ready to go. Just need to:

1. **Start Docker Desktop**
2. **Run the setup commands above**
3. **Check your email for the digest!**

Let me know when Docker is running and I can help you complete the setup! 🚀
