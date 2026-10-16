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
<div><h3>What if someone already paid?</h3><p>We check with Stripe right before every email. Paid, voided and canceled invoices never get a reminder.</p></div>
<div><h3>Do you take a cut of what I collect?</h3><p>No. One flat price. Payments go from your customer to your Stripe account as they always have.</p></div>
<div><h3>Can you move money in my Stripe account?</h3><p>We only read invoices and listen for payments. We never charge, refund or move money.</p></div>
<div><h3>Do I need a card for the trial?</h3><p>No. Try it free for 14 days. Add a card only if you want to keep going.</p></div>
<div><h3>Which invoices does it remind about?</h3><p>Stripe invoices you send by email (with a due date) that are still open. Card-on-file subscriptions are left alone.</p></div>
</div>'''

page("index.html","DueDove: polite reminders for overdue Stripe invoices","DueDove connects to Stripe and sends friendly, scheduled reminders for overdue invoices, in your name. Stops the moment they pay. $59/month, 14-day free trial.",f'''
<section class="hero center"><div class="wrap">
<div class="eyebrow">For businesses that invoice with Stripe</div>
<h1>Get paid on time without chasing anyone</h1>
<p class="lead">DueDove sends friendly, well-timed reminders for your unpaid Stripe invoices, in your name. It stops the moment they pay.</p>
<div class="actions"><a class="btn lg" href="/signup.html">Start your 14-day free trial</a><a class="btn link" href="#how">See how it works →</a></div>
<p class="small" style="margin-top:14px">No card needed · Set up in 2 minutes · $59/month after</p>
<div class="mock"><div class="mail"><div class="hd"><b>Acme Plumbing</b> &lt;via DueDove&gt;<br>Subject: <b>Following up on invoice INV-0042</b></div>
<div class="bd"><p>Hi Jordan,</p><p>I wanted to follow up on invoice INV-0042 for <b>$1,250.00</b>, which was due on November 2.</p><span class="pay">Pay invoice</span><p>If something's holding it up, just reply and let me know. Happy to help.</p><p>Thank you,<br>Acme Plumbing</p></div>
<div class="ft">Replies go to Acme Plumbing · Unsubscribe link included</div></div>
<div class="dash"><div class="k"><span>Overdue now</span><b>$4,820</b></div><div class="k"><span>Reminders sent</span><b>37</b></div><div class="k good"><span>Recovered after a reminder</span><b>$11,460</b></div>
<div class="timeline"><span>3 days before</span><span>Due date</span><span>+3 days</span><span class="paid">Paid ✓ reminders stop</span></div></div></div>
</div></section>
<section class="soft" id="how"><div class="wrap"><h2 class="center" style="margin-bottom:32px">How it works</h2><div class="grid g3">
<div class="card step"><div class="n">1</div><h3>Connect Stripe</h3><p>One click. We see your open invoices. We never move money.</p></div>
<div class="card step"><div class="n">2</div><h3>Pick your schedule</h3><p>Start with ours: 3 days before, on the due date, then 3, 7 and 14 days after. Change it anytime.</p></div>
<div class="card step"><div class="n">3</div><h3>Get paid</h3><p>Customers get a polite note with a pay link. When they pay, reminders stop.</p></div></div></div></section>
<section><div class="wrap"><div class="grid g4">
<div><h3>Sounds like you</h3><p class="small">Sent in your business name with three friendly templates you can edit.</p></div>
<div><h3>Never awkward</h3><p class="small">A live check with Stripe before every email means paid customers aren't bothered.</p></div>
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
<p class="small" style="margin:14px 0 0">We'll email you a link to sign in. No password to remember. Then connect Stripe and you're done.</p></form>
<ul class="checks small" style="margin:24px auto 0;max-width:360px"><li>Set up in about 2 minutes</li><li>Reminders go out in your name</li><li>Cancel anytime, in one click</li></ul>
<p class="small center" style="margin-top:20px">By signing up you agree to our <a href="/terms.html">Terms</a> and <a href="/privacy.html">Privacy Policy</a>.</p></div></section>''',"/signup.html")

DRAFT='<p class="draft"><b>Draft.</b> Not yet reviewed. This page will be finalized before launch.</p>'
page("terms.html","Terms of Service · DueDove","DueDove terms of service (draft).",f'''<div class="wrap legal">{DRAFT}<h1>Terms of Service</h1><p class="small">Last updated: October 16, 2026</p>
<p>These terms govern your use of DueDove, a service operated by DJ Solutions LLC (“we”, “us”). By creating an account you agree to them.</p>
<h2>1. What DueDove does</h2><p>DueDove connects to your Stripe account with read access to your invoices and sends payment reminder emails to your customers on a schedule you control. We do not collect debts, hold funds, or move money in your Stripe account.</p>
<h2>2. Your responsibilities</h2><ul><li>You may only send reminders for genuine invoices you issued to your own customers.</li><li>You are responsible for the content of your reminder templates and for complying with laws that apply to you, including consumer-protection and anti-spam laws (such as CAN-SPAM).</li><li>DueDove is not a debt collector. You must not use it to threaten, harass, or misrepresent legal consequences.</li><li>Keep your login email secure. Anyone with access to it can sign in.</li></ul>
<h2>3. Subscription and trial</h2><p>DueDove costs $59 per month after a 14-day free trial. If you don't add a payment method by the end of the trial, your subscription ends and reminders stop. Paid subscriptions renew monthly until canceled. You can cancel anytime from Settings; access continues to the end of the paid period. Fees are non-refundable except where required by law.</p>
<h2>4. Unsubscribes</h2><p>Every reminder includes an unsubscribe link. We honor unsubscribes immediately and you may not circumvent them.</p>
<h2>5. Availability</h2><p>We aim for reliable service but don't guarantee that every reminder will be sent at a particular time. Reminders are a courtesy, not a legal notice.</p>
<h2>6. Liability</h2><p>To the extent permitted by law, the service is provided “as is”, and our total liability is limited to the amount you paid us in the 3 months before the claim.</p>
<h2>7. Termination</h2><p>We may suspend accounts that misuse the service. You can disconnect Stripe and close your account at any time.</p>
<h2>8. Changes</h2><p>We may update these terms and will notify you by email of material changes.</p>
<h2>9. Contact</h2><p><a href="mailto:support@duedove.com">support@duedove.com</a></p></div>''')

page("privacy.html","Privacy Policy · DueDove","DueDove privacy policy (draft).",f'''<div class="wrap legal">{DRAFT}<h1>Privacy Policy</h1><p class="small">Last updated: October 16, 2026</p>
<p>DueDove is operated by DJ Solutions LLC. This policy explains what we collect and why.</p>
<h2>What we collect</h2><ul><li><b>Account data:</b> your email address, business name and reply-to address.</li><li><b>Stripe data:</b> for open invoices in your connected account: invoice number, amount, due date, status, payment link, and your customer's name and email.</li><li><b>Reminder records:</b> which reminders were sent, when, and to whom, plus unsubscribes.</li><li><b>Billing:</b> handled by Stripe. We never see your full card number.</li></ul>
<h2>How we use it</h2><p>Only to send the reminders you configure, show your dashboard, and run your subscription. We don't sell data, use advertising trackers, or email your customers for any other purpose.</p>
<h2>Service providers</h2><p>Stripe (payments and invoice data), our email delivery provider (sending reminders), and our hosting provider in the EU (Hetzner).</p>
<h2>Your customers</h2><p>For reminders, you are the controller of your customers' data and we process it on your behalf. Your customers can unsubscribe from any reminder in one click.</p>
<h2>Retention</h2><p>When you disconnect Stripe we delete open-invoice data. Closing your account deletes your data within 30 days, except records we must keep for tax or legal reasons.</p>
<h2>Security</h2><p>Data is encrypted in transit. Access to your Stripe account uses Stripe's official Connect authorization, which you can revoke anytime.</p>
<h2>Contact</h2><p><a href="mailto:support@duedove.com">support@duedove.com</a></p></div>''')
print("built")
