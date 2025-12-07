# 🔐 How to Get a Google App Password

## Quick Steps

### 1. Enable 2-Factor Authentication (2FA)

**You MUST have 2FA enabled to create App Passwords.**

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Under "How you sign in to Google", click **"2-Step Verification"**
3. Follow the prompts to set up 2FA (usually via phone)
4. Complete the setup

### 2. Generate an App Password

1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Or: Google Account → Security → 2-Step Verification → App passwords

2. You may need to sign in again

3. Under "Select app", choose **"Mail"** (or "Other")

4. Under "Select device", choose **"Other (Custom name)"**
   - Type: `AI News Aggregator` or any name you want

5. Click **"Generate"**

6. Google will show a 16-character password like:
   ```
   abcd efgh ijkl mnop
   ```

7. **Copy this password immediately** (you won't see it again!)

### 3. Add to Your `.env` File

Paste the app password into your `.env` file:

```env
MY_EMAIL=your-email@gmail.com
APP_PASSWORD=abcdefghijklmnop
```

**Note:** You can include or remove the spaces - both work:
```env
# Both formats work:
APP_PASSWORD=abcd efgh ijkl mnop
APP_PASSWORD=abcdefghijklmnop
```

---

## 📸 Visual Guide

### Step-by-Step with Screenshots

**Step 1: Go to Google Account Security**
```
https://myaccount.google.com/security
```

**Step 2: Enable 2-Step Verification**
- Look for "How you sign in to Google"
- Click "2-Step Verification"
- Follow the setup wizard

**Step 3: Access App Passwords**
```
https://myaccount.google.com/apppasswords
```
- This link only works if 2FA is enabled
- If you see "This setting is not available for your account", you need to enable 2FA first

**Step 4: Create App Password**
- Select app: **Mail**
- Select device: **Other (Custom name)**
- Enter name: `AI News Aggregator`
- Click **Generate**

**Step 5: Copy the Password**
- You'll see a 16-character password
- Copy it immediately
- Click **Done**

---

## ⚠️ Troubleshooting

### "App passwords" option is not available

**Cause:** 2-Step Verification is not enabled

**Solution:**
1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable 2-Step Verification first
3. Then try accessing App Passwords again

### "This setting is not available for your account"

**Possible causes:**
1. **2FA not enabled** - Enable 2-Step Verification
2. **Work/School account** - Your admin may have disabled App Passwords
3. **Advanced Protection Program** - App Passwords are disabled for security

**Solutions:**
- For personal accounts: Enable 2FA
- For work/school accounts: Contact your IT admin
- For Advanced Protection: Use OAuth instead (requires code changes)

### Can't find "App passwords" in settings

**Direct link:**
```
https://myaccount.google.com/apppasswords
```

Or navigate manually:
1. Google Account → Security
2. Scroll to "How you sign in to Google"
3. Click "2-Step Verification"
4. Scroll down to "App passwords"

### The app password doesn't work

**Common issues:**
1. **Spaces in password** - Try removing all spaces
2. **Wrong email** - Make sure `MY_EMAIL` matches the Google account
3. **Copied incorrectly** - Regenerate and copy again
4. **Gmail security** - Check if Gmail blocked the sign-in attempt

---

## 🔒 Security Notes

### Is this safe?

**Yes!** App Passwords are designed for this purpose:
- ✅ More secure than using your actual password
- ✅ Can be revoked anytime without changing your main password
- ✅ Limited to specific apps/services
- ✅ Doesn't give access to your full Google account

### Best practices:

1. **Use unique names** - Name each app password clearly
2. **Revoke unused passwords** - Remove old app passwords you don't use
3. **Don't share** - Keep app passwords private (like API keys)
4. **Regenerate if compromised** - Easy to revoke and create new ones

### How to revoke an App Password:

1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Find the app password you want to remove
3. Click the **trash icon** next to it
4. Confirm removal

---

## 📧 Alternative: Using OAuth (Advanced)

If you can't use App Passwords (work account, etc.), you can modify the code to use OAuth:

**Pros:**
- More secure
- Works with work/school accounts
- No app password needed

**Cons:**
- Requires code changes
- More complex setup
- Need to handle token refresh

**Not recommended unless App Passwords don't work for you.**

---

## ✅ Testing Your App Password

Once you've added it to `.env`, test it:

```bash
# Test email configuration
uv run python -c "
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('MY_EMAIL')
password = os.getenv('APP_PASSWORD')

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.quit()
    print('✅ Email credentials are valid!')
except Exception as e:
    print(f'❌ Error: {e}')
"
```

---

## 📝 Complete `.env` Example

Here's what your `.env` should look like:

```env
# OpenAI API Key
OPENAI_API_KEY=sk-proj-abc123...

# Gmail Configuration
MY_EMAIL=john.doe@gmail.com
APP_PASSWORD=abcdefghijklmnop

# Database (defaults are fine)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ai_news_aggregator
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

## 🎯 Quick Checklist

- [ ] 2-Step Verification is enabled on Google account
- [ ] Generated App Password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
- [ ] Copied the 16-character password
- [ ] Added to `.env` file as `APP_PASSWORD=...`
- [ ] Added your email as `MY_EMAIL=...`
- [ ] Tested the connection (optional but recommended)

---

## 🚀 Next Steps

Once your App Password is configured:

1. **Start PostgreSQL:**
   ```bash
   cd docker
   docker-compose up -d
   ```

2. **Create database tables:**
   ```bash
   cd ..
   uv run python app/database/create_tables.py
   ```

3. **Run the pipeline:**
   ```bash
   uv run python main.py
   ```

You should receive an email digest with the top AI news articles! 📧

---

## ❓ Still Having Issues?

Common problems and solutions:

| Problem | Solution |
|---------|----------|
| Can't find App Passwords | Enable 2FA first |
| App Password doesn't work | Remove spaces, check email matches |
| "Less secure app" error | Use App Password, not regular password |
| Work/school account | Contact IT admin or use OAuth |
| Password was revoked | Generate a new one |

Need more help? Check the [Gmail SMTP documentation](https://support.google.com/mail/answer/7126229).
