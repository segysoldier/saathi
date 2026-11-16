# Saathi research: story format, Telegram, India law (Nov 2026)

Not legal advice. Items I could not confirm against a primary source are marked UNVERIFIED. Web search returned mostly secondary sources.

## A) What makes short serial stories hook, and what restores energy

**Evidence found**
- **Zeigarnik (unfinished tasks are remembered better) is contested.** A 2025 meta-analysis of Zeigarnik and Ovsiankina studies found no reliable memory advantage for interrupted tasks. It did find a general urge to resume them (the Ovsiankina effect). So "cliffhangers work because of Zeigarnik" is weak. "People want to resume" is better supported. [Ghibellini & Meier 2025]
- **Narrative transportation** (Green & Brock 2000; van Laer et al. 2014 meta-analysis) links absorption in a story to story-consistent beliefs and enjoyment. UNVERIFIED this session: from my background knowledge, not re-checked.
- **Parasocial bonds with characters** are a widely reported driver of serial retention. UNVERIFIED: no source retrieved.
- **Indian audio series.** A Pocket FM report says 40% of users prefer episodes of 5-15 minutes. Pocket FM says 12-month revenue retention rose to 76% from 44%, and its CEO says over 50% of users remain after 12 months. These are company claims and measure different things. [Storyboard18; Inc42]
- **Micro-drama retention is not proven.** Pocket FM shut its video microdrama app Pocket TV, citing low retention and costly production. Kuku is pushing video anyway. I found no public retention numbers for micro-drama. [Exchange4media]
- **Recovery research.** Sonnentag & Fritz (2007) define four recovery experiences: psychological detachment, relaxation, mastery and control. A meta-analysis (Bennett, Bakker & Field 2018) covers all four. Micro-breaks under 10 minutes can restore resources, but only some break types do. One study found mastery breaks produced more detachment than relaxation breaks, yet detachment did not explain performance differences. Exact effect sizes: UNVERIFIED (I saw abstracts only). Note that these studies are mostly of workers, not NEET or JEE students.

**Draft rules for episodes**
1. Keep an episode to about 5 minutes, which is the bottom of the 5-15 minute range users prefer (Pocket FM). Treat this as a hypothesis for your test.
2. End each episode on an open question or choice, not a hard cliffhanger. This leans on the resume urge (Ghibellini & Meier), not on Zeigarnik memory. Also, a hard cliffhanger conflicts with detachment (rule 3).
3. Always include a clear stopping point. Detachment is the recovery factor most associated with well-being, and a story that keeps the mind racing defeats the purpose (Sonnentag & Fritz; Bennett 2018).
4. Make the one optional 2-minute task a small mastery experience, with a visible success and no scoring. Mastery is a recognised recovery experience.
5. Give the user control: skip, snooze and "not today" buttons. Control is one of the four recovery experiences.
6. Use recurring characters and voices, so a bond can form across days (parasocial; UNVERIFIED).
7. Write in concrete scenes with sensory detail, one point of view and one small stake, to aid transportation (Green & Brock; UNVERIFIED this session).
8. Keep exam facts inside the story, light and optional. Do not turn the break into more studying.
9. Cap serial length per week and measure whether people still feel rested. Retention numbers alone can reward compulsion.
10. Test text against audio in your 14 days. I found no solid evidence for audio vs text among Indian 18-24s.

**What this means for Saathi**
- Treat cliffhangers as a soft hook, not a Zeigarnik guarantee.
- Design for closing the app feeling lighter, not for maximum minutes.
- Ask each tester "did you feel rested?", not only "did you open it?".
- Don't copy micro-drama economics: the one visible attempt (Pocket TV) shut down.

## B) Telegram and WhatsApp facts

**Verified in core.telegram.org docs**
- **Rate limits** (FAQ): about 1 message per second per chat, 20 messages per minute per group, about 30 messages per second for free bulk broadcast. Exceeding limits returns 429 errors. Paid broadcast (up to 1000/s, 0.1 Star per message above 30/s) needs 100,000 Stars in balance and 100,000 monthly active users, so it is irrelevant to you.
- **Deep links**: `https://t.me/<bot>?start=<param>` delivers `/start <param>`. Allowed characters: A-Z, a-z, 0-9, `_`, `-`; maximum 64 characters. Use this to onboard each tester with a code. `startgroup` is the group variant.
- **Group privacy**: bots in groups see only commands and relevant messages by default. Private chat messages are always received.
- **Payments**: digital goods and services must use Telegram Stars (currency `XTR`). Telegram says it does not support other currencies for digital goods. Whether Stars can be bought or paid out in India, and UPI limits, are UNVERIFIED. The docs list no countries.
- **Newsletter-style bots**: the docs mention a "Too few private messages" alert for bots that send without user prompts, and a `my_chat_member` update when a user blocks or unblocks the bot. Practical meaning: a bot should expect blocks.

**Not stated on the pages I read (UNVERIFIED in the docs)**
- A bot cannot message a user first. Users see a Start button, and from my knowledge the API rejects messages to users who never started the bot. Treat a tester pressing Start as required.
- Scheduled messages: the Bot API pages I read do not mention them. Assume you must schedule server-side (cron or a job queue).
- Voice notes (`sendVoice`, OGG/OPUS) and inline buttons exist, but I did not confirm formats and size limits.

**Reach in India.** Estimates conflict: roughly 104 million vs 200 million Telegram users in India, none from Telegram itself (UNVERIFIED). WhatsApp has led in India: a 2021 survey put it above 53%. A Statista-based page says Telegram engagement in India is lower than on the major networks. No source gave a 2026 figure for 18-24s. This is a real reach risk.

**WhatsApp Cloud API (alternative).** Billing is per delivered message. Most sources give India marketing at about Rs 0.8631 and utility at about Rs 0.115 per message. One vendor says Rs 1.09 and Rs 0.145 instead. All come from vendor blogs, not Meta's rate card (UNVERIFIED). Meta requires migrating billing to INR by 31 December 2026 (single-source claim). A proactive message outside a 24-hour window needs an approved template, and daily rest packs would likely count as marketing, the expensive category. I did not verify how Meta classifies them.

**What this means for Saathi**
- For the 16-person test, Telegram is free and fine. Ask each tester at recruitment whether they already use Telegram daily.
- Build the scheduler yourself and expect a blocked bot to stop delivery.
- Use `?start=` codes to onboard and to label test cohorts.
- Don't plan payments on Stars yet. Plan UPI on your own site if you ever charge, and check legal fit.
- If Telegram reach is low, price WhatsApp at about Rs 0.86 per daily message, roughly Rs 26 a month per user (my arithmetic from unverified rates).

## C) India law and safety (not legal advice)

**Status.** The DPDP Act 2023 and the DPDP Rules 2025 were notified on 13-14 November 2025 with phased commencement (sources differ on the exact day). Data Protection Board provisions took effect immediately, consent-manager provisions after about 12 months (so around now, UNVERIFIED), and most obligations after 18 months, around 13-14 May 2027. MeitY consulted in early 2026 on cutting 18 months to 12, but I found no notified change; the latest item I saw was from March 2026. So the main obligations are probably not yet in force in November 2026. UNVERIFIED: check the Gazette and MeitY site.

**Key obligations (secondary sources; verify in the Rules text)**
- A clear notice with plain-language consent before collecting personal data, with withdrawal as easy as giving consent.
- For children (under 18), verifiable parental consent (Rule 10). Verification can use government-backed records or Digital Locker tokens. Your audience of 18-24 sits at the edge, so exclude under-18s at sign-up.
- Collect only what you need, delete when the purpose ends, and keep reasonable security.
- Breach reporting: the Board and affected users must be told; the detailed timeline is reported as 72 hours (UNVERIFIED).

**Minimum for a 16-person informal test**
- Send a plain consent message in Hinglish at /start covering what you store (Telegram ID, replies, mood or tiredness answers), why, who can see it, how long (for example, delete 30 days after the test), and how to quit with `/delete`.
- Confirm age 18+ at sign-up.
- Store minimum data in one protected place; no sharing with third parties without telling people.
- Do not give medical or mental health advice. Treat "tired" as a normal state, not a diagnosis.

**Helplines.** Tele-MANAS: 14416 or 1-800-891-4416, free, 24/7, many languages, run under the Health Ministry with NIMHANS (several sources agree; check the official site before launch). Add a crisis keyword response that shows the number instead of a story.

**What this means for Saathi**
- A simple consent plus 18+ check plus delete command is cheap and ready for 2027.
- Don't collect health or mental-state labels beyond what the test needs.
- Write a one-paragraph breach plan now.
- Hold a lawyer review before real launch.

## Sources
- [Ghibellini & Meier 2025, Zeigarnik/Ovsiankina meta-analysis](https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html)
- [Bennett, Bakker & Field 2018 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164214)
- [Pocket FM episode length report (Storyboard18)](https://stgcms.storyboard18.com/?p=18828)
- [Pocket TV shutdown (Exchange4media)](https://www.exchange4media.com/digital-news/pocket-tv-shutdown-a-planned-beta-exit-not-a-setback-rohan-nayak-155817.html)
- [Pocket FM retention (Inc42)](https://inc42.com/buzz/pocket-fm-eyes-15-20-ebitda-margin-global-expansion-with-ai-led-content-push/)
- [Telegram Bots FAQ](https://core.telegram.org/bots/faq)
- [Telegram Bot features](https://core.telegram.org/bots/features)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Telegram vs WhatsApp India survey (Telangana Today)](https://telanganatoday.com/telegram-fast-eating-into-whatsapp-user-base-in-india-survey)
- [WhatsApp pricing India (baat.ai)](https://baat.ai/blog/whatsapp-api-pricing-india)
- [Meta WhatsApp pricing docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing.md)
- [DPDP Rules notified (Storyboard18)](https://www.storyboard18.com/amp/digital/breaking-govt-notifies-final-dpdp-rules-sets-staggered-rollout-with-key-obligations-for-data-fiduciaries-84201.htm)
- [DPDP Rules overview (India Briefing)](https://www.india-briefing.com/news/dpdp-rules-2025-india-data-protection-law-compliance-40769.html)
- [MeitY timeline-cut proposal (Mondaq)](https://www.mondaq.com/india/data-protection/1773554/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs)
- [Tele-MANAS (PIB)](https://pib.gov.in/PressReleasePage.aspx?PRID=2022057)
