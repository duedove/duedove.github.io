"""Tiny static generator: shared header/footer for every page. Run: python3 build.py"""
import pathlib,os
APP=os.environ.get("APP","https://app.duedove.com");OUT=pathlib.Path(os.environ.get("OUT","."))
LOGO='<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#0f766e"/><path d="M8 18c3-1 5-4 6-8 1 3 3 5 7 5l3-2-1 4c-1 4-5 7-10 7-2 0-4-1-5-2l3-1c-1-1-2-2-3-3z" fill="#fff"/></svg>'
FAV="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='9' fill='%230f766e'/%3E%3Cpath d='M8 18c3-1 5-4 6-8 1 3 3 5 7 5l3-2-1 4c-1 4-5 7-10 7-2 0-4-1-5-2l3-1c-1-1-2-2-3-3z' fill='%23fff'/%3E%3C/svg%3E"
def page(fn,title,desc,body,cur=""):
    nav=lambda h,t:f'<a class="hide-sm" href="{h}"{" aria-current=page" if cur==h else ""}>{t}</a>'
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; form-action {APP}; base-uri 'none'; object-src 'none'"><meta name="referrer" content="no-referrer">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#ffffff"><link rel="icon" href="{FAV}"><link rel="stylesheet" href="/style.css"></head><body>
<header class="top"><div class="wrap"><a class="logo" href="/">{LOGO}DueDove</a><nav class="nav">{nav("/#how","How it works")}{nav("/pricing.html","Pricing")}<a href="{APP}/login">Log in</a><a class="btn sm" href="/signup.html">Start free trial</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><div>© 2026 DJ Solutions LLC · <a href="mailto:support@duedove.com">support@duedove.com</a></div><nav><a href="/pricing.html">Pricing</a><a href="/signup.html">Sign up</a><a href="{APP}/login">Log in</a><a href="/terms.html">Terms</a><a href="/privacy.html">Privacy</a></nav></div></footer></body></html>'''
    OUT.mkdir(parents=True,exist_ok=True);(OUT/fn).write_text(html)

FAQ='''<div class="grid g2 faq" style="margin-top:32px">
<div><h3>Will my customers know it's automated?</h3><p>Emails come from your business name and sound like you wrote them. Replies go straight to your inbox. You can edit every word.</p></div>
<div><h3>What if someone already paid?</h3><p>We check with Stripe or QuickBooks right before every email. Paid, voided and canceled invoices never get a reminder.</p></div>
<div><h3>Do you take a cut of what I collect?</h3><p>No. One flat price. Your customers pay you through Stripe or QuickBooks, the same way they do now.</p></div>
<div><h3>Can you change anything in my account?</h3><p>No. We only read invoices and customers. We never charge, refund, edit or move money in Stripe or QuickBooks.</p></div>
<div><h3>Do I need a card for the trial?</h3><p>No. Try it free for 14 days. Add a card only if you want to keep going.</p></div>
<div><h3>Which invoices does it remind about?</h3><p>Open invoices with a due date and a customer email: Stripe invoices sent by email, or QuickBooks Online invoices. Card-on-file subscriptions are left alone.</p></div>
<div><h3>Do you support Xero?</h3><p>Not yet. Xero is coming next. Email <a href="mailto:support@duedove.com">support@duedove.com</a> and we'll tell you when it's ready.</p></div>
<div><h3>Can I use Stripe and QuickBooks together?</h3><p>Yes. Connect either or both. Your dashboard combines them.</p></div>
</div>'''

page("index.html","DueDove: polite reminders for overdue Stripe and QuickBooks invoices","DueDove connects to Stripe or QuickBooks Online and sends friendly, scheduled reminders for overdue invoices, in your name. Stops the moment they pay. $59/month, 14-day free trial.",f'''
<section class="hero center"><div class="wrap">
<div class="eyebrow">For businesses that invoice with Stripe or QuickBooks</div>
<h1>Get paid on time without chasing anyone</h1>
<p class="lead">DueDove sends friendly, well-timed reminders for your unpaid Stripe and QuickBooks invoices, in your name. It stops the moment they pay.</p>
<div class="actions"><a class="btn lg" href="/signup.html">Start your 14-day free trial</a><a class="btn link" href="#how">See how it works →</a></div>
<p class="small" style="margin-top:14px">No card needed · Set up in 2 minutes · $59/month after</p>
<p class="works small">Works with <b>Stripe</b> · <b>QuickBooks Online</b> · <span>Xero coming soon</span></p>
<div class="mock"><div class="mail"><div class="hd"><b>Acme Plumbing</b> &lt;via DueDove&gt;<br>Subject: <b>Following up on invoice INV-0042</b></div>
<div class="bd"><p>Hi Jordan,</p><p>I wanted to follow up on invoice INV-0042 for <b>$1,250.00</b>, which was due on November 2.</p><span class="pay">Pay invoice</span><p>If something's holding it up, just reply and let me know. Happy to help.</p><p>Thank you,<br>Acme Plumbing</p></div>
<div class="ft">Replies go to Acme Plumbing · Unsubscribe link included</div></div>
<div class="dash"><div class="k"><span>Overdue now</span><b>$4,820</b></div><div class="k"><span>Reminders sent</span><b>37</b></div><div class="k good"><span>Recovered after a reminder</span><b>$11,460</b></div>
<div class="timeline"><span>3 days before</span><span>Due date</span><span>+3 days</span><span class="paid">Paid ✓ reminders stop</span></div></div></div>
</div></section>
<section class="soft" id="how"><div class="wrap"><h2 class="center" style="margin-bottom:32px">How it works</h2><div class="grid g3">
<div class="card step"><div class="n">1</div><h3>Connect Stripe or QuickBooks</h3><p>One click. We see your open invoices. We never change anything or move money.</p></div>
<div class="card step"><div class="n">2</div><h3>Pick your schedule</h3><p>Start with ours: 3 days before, on the due date, then 3, 7 and 14 days after. Change it anytime.</p></div>
<div class="card step"><div class="n">3</div><h3>Get paid</h3><p>Customers get a polite note with a pay link. When they pay, reminders stop.</p></div></div></div></section>
<section><div class="wrap"><div class="grid g4">
<div><h3>Sounds like you</h3><p class="small">Sent in your business name with three friendly templates you can edit.</p></div>
<div><h3>Never awkward</h3><p class="small">A live balance check before every email means paid customers aren't bothered.</p></div>
<div><h3>Respectful</h3><p class="small">An unsubscribe link in every email, and a do-not-email list you control.</p></div>
<div><h3>See the results</h3><p class="small">Your dashboard shows what's overdue and how much came back after a reminder.</p></div></div></div></section>
<section class="soft"><div class="wrap center"><h2>One simple price</h2><p class="lead">No percentage of your invoices. No setup fees.</p>
<div class="card plan pop price-hero" style="text-align:left"><h3>DueDove</h3><div class="price">$59<small>/month</small></div><ul><li>Unlimited invoices and reminders</li><li>Your schedule and your wording</li><li>Instant stop on payment</li><li>Dashboard with recovered $</li></ul><a class="btn" href="/signup.html">Start 14-day free trial</a></div>
<p class="small" style="margin-top:16px"><a href="/pricing.html">Questions? See the FAQ</a></p></div></section>
''')

page("pricing.html","Pricing · DueDove","DueDove is $59/month with a 14-day free trial. No percentage of your invoices.",f'''
<section class="hero center" style="padding-bottom:24px"><div class="wrap"><h1>Simple, flat pricing</h1><p class="lead">One plan with everything in it. Try it free for 14 days.</p>
<div class="card plan pop price-hero" style="text-align:left"><h3>DueDove</h3><div class="price">$59<small>/month</small></div><ul><li>Unlimited invoices and reminders</li><li>Editable schedule and email templates</li><li>Sent in your business name, replies to you</li><li>Live payment check before every email</li><li>Unsubscribe handling and do-not-email list</li><li>Dashboard: overdue, sent and recovered</li></ul><a class="btn" href="/signup.html">Start 14-day free trial</a><p class="small" style="margin:12px 0 0;text-align:center">No card needed to start · Cancel anytime</p></div>
</div></section>
<section style="padding-top:24px"><div class="wrap narrow" style="max-width:860px"><h2 class="center">Questions</h2>{FAQ}</div></section>''',"/pricing.html")

page("signup.html","Start your free trial · DueDove","Create your DueDove account. 14 days free, no card needed.",f'''
<section><div class="wrap" style="max-width:480px"><div class="center"><h1 style="font-size:34px">Start your free trial</h1><p class="lead">14 days free. No card needed.</p></div>
<form class="panel" method="post" action="{APP}/auth/magic" style="margin-top:24px">
<label for="email">Your work email</label><input id="email" type="email" name="email" required autocomplete="email" placeholder="you@yourbusiness.com">
<div class="hp" aria-hidden="true"><label for="website">Website</label><input id="website" type="text" name="website" tabindex="-1" autocomplete="off"></div>
<button class="btn lg" style="width:100%;margin-top:16px">Email me a sign-in link</button>
<p class="small" style="margin:14px 0 0">We'll email you a link to sign in. No password to remember. Then connect Stripe or QuickBooks and you're done.</p></form>
<ul class="checks small" style="margin:24px auto 0;max-width:360px"><li>Set up in about 2 minutes</li><li>Reminders go out in your name</li><li>Cancel anytime, in one click</li></ul>
<p class="small center" style="margin-top:20px">By signing up you agree to our <a href="/terms.html">Terms</a> and <a href="/privacy.html">Privacy Policy</a>.</p></div></section>''',"/signup.html")

DRAFT=''
page("terms.html","Terms of Service · DueDove","DueDove terms of service.",f'''<div class="wrap legal">{DRAFT}<h1>Terms of Service</h1><p class="small">Last updated: October 16, 2026</p>
<p>These terms govern your use of DueDove (the “Service”), operated by DJ Solutions LLC, a Colorado limited liability company (“we”, “us”). By creating an account you agree to them. If you use DueDove for a business, you confirm you can accept these terms for it.</p>
<h2>1. What DueDove does</h2><p>DueDove connects to your Stripe account or QuickBooks Online company with read access to your invoices and customers, and sends payment reminder emails to your customers on a schedule you control. We do not collect debts, hold funds, or create, change, or move anything in your Stripe or QuickBooks account.</p>
<h2>2. Reminders sent on your behalf</h2><p>Reminders are sent in your business's name, through our email provider, with replies going to the address you choose. You authorize us to send them to the customer email addresses on your open invoices. Every reminder includes an unsubscribe link; we honor unsubscribes immediately and you may not work around them.</p>
<h2>3. Acceptable use</h2><ul><li>Only send reminders for genuine invoices you issued to your own customers. No spam, marketing, or unsolicited email.</li><li>You are responsible for your relationships with your customers, the accuracy of your invoices, the content of your templates, and complying with laws that apply to you, including anti-spam (such as CAN-SPAM), privacy, and consumer-protection laws.</li><li>DueDove is not a debt collector. Do not use it to threaten, harass, or misstate legal consequences.</li><li>Don't misuse, probe, overload, or try to break the Service, and keep access to your login email secure.</li></ul><p>We may suspend accounts that break these rules, generate complaints, or harm our sending reputation.</p>
<h2>4. Price, trial and billing</h2><p>DueDove costs a flat $59 per month (plus any applicable taxes) after a 14-day free trial. No card is needed for the trial; if you don't add one, reminders stop when it ends. Paid subscriptions are billed monthly through Stripe and renew until canceled. You can cancel anytime from Settings; you keep access until the end of the period you paid for and won't be charged again. Fees already paid are non-refundable except where the law requires. We'll give at least 30 days' email notice before any price change.</p>
<h2>5. Connections and disconnecting</h2><p>You can disconnect Stripe or QuickBooks at any time, from DueDove or from inside Stripe or QuickBooks. When you do, reminders for that source stop and we delete its open-invoice data, as described in our <a href="/privacy.html">Privacy Policy</a>.</p>
<h2>6. Availability</h2><p>We aim for reliable service but don't guarantee that every reminder will be sent or delivered at a particular time, or that any invoice will be paid. Reminders are a courtesy, not a legal notice.</p>
<h2>7. Disclaimer and liability</h2><p>To the maximum extent permitted by law, the Service is provided “as is” without warranties, we are not liable for indirect or consequential damages or lost revenue, and our total liability is limited to the amounts you paid us in the 12 months before the claim.</p>
<h2>8. Indemnity</h2><p>You agree to cover claims against us arising from your invoices, your templates, your dealings with your customers, or your breach of these terms.</p>
<h2>9. Termination</h2><p>You can close your account at any time. We may suspend or end the Service for breach of these terms, or end it for everyone with 30 days' notice and a prorated refund of any prepaid period.</p>
<h2>10. Governing law</h2><p>These terms are governed by the laws of the State of Colorado, USA, with venue in Colorado courts.</p>
<h2>11. Changes</h2><p>We may update these terms and will email you about material changes before they take effect.</p>
<h2>12. Contact</h2><p><a href="mailto:support@duedove.com">support@duedove.com</a></p></div>''')

page("privacy.html","Privacy Policy · DueDove","DueDove privacy policy.",f'''<div class="wrap legal">{DRAFT}<h1>Privacy Policy</h1><p class="small">Last updated: October 16, 2026</p>
<p>DueDove is operated by DJ Solutions LLC, a Colorado limited liability company (“we”, “us”). This policy explains what we collect, why, and what happens to it.</p>
<h2>What we collect</h2><ul><li><b>Account data:</b> your email address, business name, reply-to address, schedule and templates.</li><li><b>Invoice data from Stripe or QuickBooks Online:</b> for your invoices, the invoice number, amount, balance, currency, due date, status and payment link, plus your customer's name and email address.</li><li><b>Reminder records:</b> which reminders were sent, when, to whom, and unsubscribes.</li><li><b>Billing:</b> handled by Stripe. We never see or store your full card number.</li><li><b>Basic logs:</b> request logs (such as IP address and time) for security and troubleshooting.</li></ul>
<h2>Access to Stripe and QuickBooks</h2><p>You connect through the official authorization flow of Stripe (the DueDove Stripe App) or Intuit QuickBooks Online (OAuth 2.0). We ask only for the access needed to read invoices and customers and to check whether an invoice is still unpaid right before each reminder. We never create, change or delete anything in your accounts and never move money. Access tokens are encrypted at rest. You can revoke access at any time from DueDove, your Stripe Dashboard, or your QuickBooks apps settings.</p>
<h2>How we use it</h2><p>Only to send the reminders you configure, show your dashboard, provide support, and run your subscription. We don't sell data, use advertising trackers, or email your customers for any other purpose.</p>
<h2>Your customers' data</h2><p>For reminders, you are the controller of your customers' data and we process it on your behalf, only on your instructions. Reminders go out from our sending domain in your business's name, with replies going to you. Your customers can unsubscribe in one click.</p>
<h2>Service providers</h2><ul><li><b>Hetzner</b> (Germany): hosting. Our servers and database are in Germany.</li><li><b>Resend</b>: delivering reminder and sign-in emails. Open and click tracking is off.</li><li><b>Stripe</b>: subscription billing, and invoice data if you connect Stripe.</li><li><b>Intuit</b>: invoice data if you connect QuickBooks Online.</li></ul><p>Data may be processed in the United States and the European Union by these providers.</p>
<h2>Retention and deletion</h2><p>When you disconnect Stripe or QuickBooks, we delete the stored access for it and its open-invoice data right away. We keep a minimal history of paid invoices and reminders sent so your dashboard stays accurate, until you close your account. Closing your account deletes your data within 30 days, except records we must keep for tax or legal reasons. Backups roll off within 30 days after that.</p>
<h2>Security</h2><p>Data is encrypted in transit (HTTPS) and access tokens are encrypted at rest. Access to production systems is limited.</p>
<h2>Your rights</h2><p>You can ask to access, correct, export or delete your data by emailing us. If you are your customers' vendor, forward their requests to us and we'll help.</p>
<h2>Changes</h2><p>We'll email you about material changes before they take effect.</p>
<h2>Contact</h2><p><a href="mailto:support@duedove.com">support@duedove.com</a></p></div>''')
print("built")
