# 💳 How to Add Credits to Your OpenAI Account

## Quick Links

- **Billing Page:** [platform.openai.com/settings/organization/billing](https://platform.openai.com/settings/organization/billing)
- **Usage Dashboard:** [platform.openai.com/usage](https://platform.openai.com/usage)
- **API Keys:** [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

---

## 🚀 Step-by-Step Guide

### **Step 1: Go to Billing Settings**

1. Visit: [platform.openai.com/settings/organization/billing](https://platform.openai.com/settings/organization/billing)
2. Sign in with your OpenAI account if prompted

### **Step 2: Choose Your Payment Method**

You have two options:

#### **Option A: Auto-Recharge (Recommended)**

This automatically adds credits when your balance gets low.

1. Click **"Add payment method"** or **"Set up paid account"**
2. Enter your credit card details:
   - Card number
   - Expiration date
   - CVC/CVV
   - Billing address
3. Set up auto-recharge:
   - **Recharge amount:** $10 (or your preferred amount)
   - **Trigger threshold:** $5 (recharges when balance drops below this)
4. Click **"Continue"** or **"Save"**

#### **Option B: Manual Credit Purchase**

Buy credits one time without auto-recharge.

1. Click **"Add to credit balance"**
2. Enter amount (minimum $5)
3. Enter payment details
4. Click **"Purchase"**

---

## 💰 Pricing & Recommendations

### **How Much Should You Add?**

**For AI News Aggregator:**
- **Per run cost:** ~$0.15 - $0.35
- **Daily use:** ~$5-10/month (if run daily)
- **Weekly use:** ~$1-3/month (if run weekly)

**Recommendations:**
- **Start with:** $10-20
- **Auto-recharge:** $10 when balance < $5
- **This gives you:** 30-100 runs

### **What You're Paying For:**

1. **GPT-4o-mini** (digest generation): $0.150 per 1M input tokens, $0.600 per 1M output tokens
2. **GPT-4.1** (article ranking): ~$2-5 per 1M tokens (varies by model)

---

## 🔍 Check Your Current Balance

### **View Usage Dashboard**

1. Go to: [platform.openai.com/usage](https://platform.openai.com/usage)
2. You'll see:
   - **Current balance**
   - **Usage this month**
   - **Cost breakdown by model**
   - **Rate limits**

### **Free Credits**

- **New accounts:** Get $5 free credits
- **Expiration:** 3 months from account creation
- **Check if expired:** Look at "Free trial credits" on usage page

---

## ✅ Payment Methods Accepted

OpenAI accepts:
- ✅ Credit cards (Visa, Mastercard, Amex, Discover)
- ✅ Debit cards
- ❌ PayPal (not currently supported)
- ❌ Cryptocurrency (not currently supported)

---

## 🛡️ Security & Billing

### **Is It Safe?**

- ✅ OpenAI uses Stripe for payment processing
- ✅ PCI-DSS compliant
- ✅ Credit card details are encrypted
- ✅ You can remove payment method anytime

### **Billing Cycle**

- **Pay as you go:** Charged monthly for usage
- **Auto-recharge:** Immediate charge when threshold is hit
- **No subscription:** Only pay for what you use

### **Set Spending Limits**

1. Go to billing settings
2. Click **"Usage limits"**
3. Set:
   - **Hard limit:** Maximum you want to spend per month
   - **Soft limit:** Get notified when you hit this amount

**Recommended limits for this project:**
- Soft limit: $5/month
- Hard limit: $10/month

---

## 🔧 After Adding Credits

### **1. Verify Payment**

Check that your payment went through:
1. Go to [platform.openai.com/usage](https://platform.openai.com/usage)
2. Look for your new balance
3. Should show: "$X.XX available"

### **2. Test the API**

Run a quick test:

```bash
cd c:\Users\willi\OneDrive\Documents\GitHub\ai-news-aggregator

# Test with a small number of articles
python -m uv run python main.py 24 5
```

### **3. Run Full Pipeline**

Once confirmed working:

```bash
# Full run with 7 days of articles
python -m uv run python main.py 168 10
```

---

## 📧 You Should Receive

After successful payment:
1. **Email confirmation** from OpenAI/Stripe
2. **Receipt** for your purchase
3. **Updated balance** in your dashboard

---

## ❓ Troubleshooting

### **Payment Declined**

**Possible reasons:**
- Insufficient funds
- Card blocked for international transactions
- Bank flagged as suspicious

**Solutions:**
1. Contact your bank
2. Try a different card
3. Enable international transactions
4. Wait 24 hours and try again

### **Can't Find Billing Page**

**Direct link:** [platform.openai.com/settings/organization/billing](https://platform.openai.com/settings/organization/billing)

Or navigate manually:
1. Go to [platform.openai.com](https://platform.openai.com)
2. Click your profile (top right)
3. Click **"Settings"**
4. Click **"Billing"** in left sidebar

### **"Organization Required" Error**

If you see this:
1. You need to create an organization first
2. Go to [platform.openai.com/settings/organization](https://platform.openai.com/settings/organization)
3. Click **"Create organization"**
4. Then go back to billing

---

## 💡 Pro Tips

### **Save Money:**

1. **Use GPT-4o-mini** instead of GPT-4 for digests (already configured)
2. **Reduce time range:** Run with fewer hours to process fewer articles
3. **Limit articles:** Use smaller `top_n` value (e.g., 5 instead of 10)
4. **Run less frequently:** Weekly instead of daily

### **Monitor Usage:**

1. Check usage dashboard weekly
2. Set up email alerts for spending limits
3. Review cost breakdown by model

### **Optimize Costs:**

The current setup is already optimized:
- ✅ Uses GPT-4o-mini for summaries (cheapest)
- ✅ Uses GPT-4.1 only for ranking (once per run)
- ✅ Batches API calls efficiently

---

## 🎯 Quick Summary

**To add credits:**
1. Go to [platform.openai.com/settings/organization/billing](https://platform.openai.com/settings/organization/billing)
2. Click **"Add payment method"** or **"Add to credit balance"**
3. Enter card details
4. Add $10-20 to start
5. Set up auto-recharge (optional but recommended)

**Then run:**
```bash
python -m uv run python main.py 168 10
```

**You'll get:**
- ✅ AI-generated summaries
- ✅ Personalized ranking
- ✅ Beautiful HTML email digest
- ✅ Delivered to your inbox!

---

## 🆘 Need Help?

- **OpenAI Support:** [help.openai.com](https://help.openai.com)
- **Billing Questions:** [help.openai.com/en/collections/3742473-billing](https://help.openai.com/en/collections/3742473-billing)
- **API Documentation:** [platform.openai.com/docs](https://platform.openai.com/docs)

---

**Ready to add credits? The billing page should be open in your browser!** 🚀
