# 🔑 How to Add Your OpenAI API Key

## Quick Setup (3 Steps)

### Step 1: Create the `.env` file

Copy the example environment file:

```bash
cp app/example.env .env
```

Or create it manually in the root directory with this content:

```env
OPENAI_API_KEY=your-api-key-here

MY_EMAIL=your-email@gmail.com
APP_PASSWORD=your-gmail-app-password

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ai_news_aggregator
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Optional: Proxy for YouTube transcripts (leave empty if not needed)
PROXY_USERNAME=
PROXY_PASSWORD=
```

### Step 2: Get Your OpenAI API Key

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click **"Create new secret key"**
3. Copy the key (it starts with `sk-...`)
4. Paste it into your `.env` file:

```env
OPENAI_API_KEY=sk-proj-abc123...your-actual-key
```

### Step 3: Configure Email (Optional)

If you want to receive email digests:

**For Gmail:**
1. Enable 2-Factor Authentication on your Google account
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Generate an "App Password" for "Mail"
4. Add to `.env`:

```env
MY_EMAIL=youremail@gmail.com
APP_PASSWORD=abcd efgh ijkl mnop  # 16-character app password
```

---

## 📁 File Location

Your `.env` file should be in the **root directory**:

```
ai-news-aggregator/
├── .env                    ← Create this file here
├── app/
│   └── example.env         ← Template to copy from
├── docker/
├── main.py
└── pyproject.toml
```

---

## ✅ Verify It's Working

After creating `.env`, test the connection:

```bash
# Install dependencies
pip install uv
uv sync

# Test OpenAI connection
uv run python -c "from openai import OpenAI; import os; from dotenv import load_dotenv; load_dotenv(); client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')); print('✅ OpenAI API key is valid!')"
```

---

## 🔒 Security Notes

1. **Never commit `.env` to git** - It's already in `.gitignore`
2. **Keep your API key secret** - Don't share it publicly
3. **Use environment variables** - The code loads from `.env` automatically
4. **Rotate keys regularly** - Generate new keys periodically

---

## 🚀 Next Steps

Once your `.env` is configured:

```bash
# 1. Start PostgreSQL
cd docker
docker-compose up -d

# 2. Create database tables
cd ..
uv run python app/database/create_tables.py

# 3. Run the pipeline
uv run python main.py
```

---

## ❓ Troubleshooting

### "No API key found"
- Make sure `.env` is in the root directory (not in `app/`)
- Check that the line starts with `OPENAI_API_KEY=` (no spaces)
- Verify the key starts with `sk-`

### "Invalid API key"
- Double-check you copied the entire key
- Make sure there are no extra spaces or quotes
- Try generating a new key from OpenAI

### "Email not sending"
- Gmail requires an App Password (not your regular password)
- Make sure 2FA is enabled on your Google account
- Check that `MY_EMAIL` and `APP_PASSWORD` are set correctly

---

## 💡 Example `.env` File

Here's what a complete `.env` file looks like:

```env
# OpenAI API Key (required)
OPENAI_API_KEY=sk-proj-abc123def456ghi789...

# Email Configuration (optional, for receiving digests)
MY_EMAIL=john.doe@gmail.com
APP_PASSWORD=abcd efgh ijkl mnop

# PostgreSQL Database (defaults are fine for local development)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ai_news_aggregator
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Optional: YouTube Transcript Proxy (leave empty if not needed)
PROXY_USERNAME=
PROXY_PASSWORD=
```

---

## 🎯 That's It!

Your OpenAI API key is now configured and the project will automatically load it when running.
