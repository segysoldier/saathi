# Saathi: test ka saamaan

**Wada:** jab thak kar reel kholne ka mann kare, Saathi 5 minute ka aisa rest deta hai jo khatam hota hai, aur jo aapke sapne ki duniya ka hai.

**Abhi ka kadam:** 14 din ka haath se chalne wala test, 16 log (umar 18-24). Code tabhi, jab test pass ho.

## Kis kram me padhna hai

| Kaam | File |
|---|---|
| 1. Log dhoondhna | `test-kit/01_bharti_message.md` |
| 2. Din 1-2: sawal aur screenshot | `test-kit/02_onboarding_sawal.md` |
| 3. Logon ki sheet | `test-kit/03_people.csv` |
| 4. Roz ki sheet | `test-kit/04_log.csv` |
| 5. Din 3-12: roz kya bhejna hai | `test-kit/05_roz_ka_tarika.md` |
| 6. Din 13-14: ant, interview, pass/fail | `test-kit/06_din_13_14.md` |

## Kahaniyan (10 din, 3 group)

| Group | File | Hero |
|---|---|---|
| Medical / NEET | `packs/medical_neet.md` | Dr. Ankit Tiwari, Satna ka intern |
| Tech | `packs/tech_engineering.md` | Ankit "Anku" Dubey, Jhansi ka fresher |
| Sarkari exam | `packs/sarkari_exam.md` | Ankit Verma, naya block adhikari |

Teeno hero ka naam Ankit nikla (teen alag lekhakon ne chuna). Har tester sirf ek group dekhta hai, isliye chal jayega; chaho to badal lo.

Har din ke teen hisse hain: THAKA (sirf kahani), THEEK (ek mazedaar sawal), TAAZA (2 minute ka asli kadam).

## App (phone web app)

Folder: `app/`. Sirf static files hain, koi server-code, account ya key nahi.

| File | Kaam |
|---|---|
| `app/index.html` | Poora app (screen, style aur logic) |
| `app/packs.js` | Kahaniyon ka data. Haath se mat badlo; ye `packs/*.md` se banta hai |
| `app/build_packs.py` | `packs/*.md` se `packs.js` banata hai |
| `app/sw.js`, `app/manifest.webmanifest`, `app/icon*` | Phone par install aur offline ke liye |

Computer par chalana:

```bash
python -m http.server 8765 --directory saathi/app
```

Phir browser me `http://localhost:8765` kholo.

Kahani badalni ho to `packs/` ki markdown file badlo, phir:

```bash
python saathi/app/build_packs.py
```

App kya karta hai: haal chuno (thaka / theek / taaza), us din ka episode padho, chaho to sawal ya 2 minute ka kadam, phir "Halka laga?" aur khatam. Ek din me ek hi naya episode. Data sirf usi phone ke browser me rehta hai.

App kya nahi karta: khud message ya notification nahi bhejta, aur doosre apps ko rok nahi sakta.

Phone par asli install ke liye app ko kisi HTTPS pate par rakhna hoga (jaise GitHub Pages, Netlify ya Cloudflare Pages). Abhi ye kahin host nahi hai.

## Research

- `research/competitors.md`: kaun pehle se kya bana raha hai, daam, aur gap asli hai ya nahi.
- `research/formats_telegram_law.md`: kahani ko kya cheez pakad banati hai, Telegram bot kya kar sakta hai, aur Bharat ka data kanoon.

## Kya jaancha gaya, kya nahi

- Tech ke 6 Python snippet chalakar dekhe gaye: sab jawab sahi.
- Medical ke 30 aur sarkari ke 30 sawal ek-ek padh kar jaanche gaye. Ek sarkari sawal (Din 9, rishte wala) do tarah padha ja sakta tha; theek kar diya.
- Kahaniyan AI ne likhi hain. **Bhejne se pehle har episode khud ek baar padho.**
- Research me jo cheez pakki nahi ho saki, wahan UNVERIFIED likha hai. Daam aur user-ginti wale kai aankde isi me aate hain.
