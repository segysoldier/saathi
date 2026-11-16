# Saathi Rest Packs: TECH / ENGINEERING (10 din)

**Character sheet**
1. **Ankit Dubey "Anku"**, 22, Jhansi se, B.Tech ke baad Bengaluru ki ek chhoti startup "ChaiByte" (kaalpanik) mein fresher backend developer.
2. **Flaw:** har cheez pe "arre ho jayega bhai" bolta hai, phir 11 baje raat ko panic karta hai.
3. **Running joke:** har variable ka naam `temp` rakhta hai: `temp`, `temp2`, `temp_final`, `temp_final_pakka`. Saath mein Meera di (senior dev, bahut shaant, thodi daravni) aur Bunty (dost, QA tester, meme ka bhandaar).

AI se bana content. Bhejne se pehle founder review kare.

---

### Din 1: Pehla din, pehla laptop
**THAKA pack (sirf kahani):**
Ankit ne Jhansi station pe mummy ko teen baar bola, "Haan mummy, parathe kha lunga." Bengaluru pahuncha to office dekha: ek kamra, chaar desk, ek plant jo shayad plastic ka tha. Yahi thi ChaiByte, ek startup jo chai ki dukaanon ke liye billing app banati hai.
Pehle din laptop mila. Ankit ne itni izzat se pakda jaise naya phone ho, cover bhi nahi utara. Bunty, QA wala, bola, "Bhai, sticker laga le, warna kal tak koi aur le jayega."
Phir aayi Meera di. Senior developer. Aawaz dheemi, nazar tez. Unhone bas itna kaha, "Ankit, setup kar lo. Kal tumhe pehla ticket milega." Aur chali gayi.
Ankit ne apne aap se kaha, "Arre ho jayega bhai." Setup mein teen ghante lage, do baar password bhool gaya, ek baar galti se poore office ke group mein "hello test" bhej diya.
Raat ko hostel PG mein leta to phone pe notification aaya. Meera di ka message: "Kal 10 baje. Tumhara ticket thoda... interesting hai."
Interesting matlab kya?

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Group mein galti se "hello test" chala gaya. Tum hote to kya karte: (a) delete kar dete, (b) "sorry wrong chat" likhte, (c) chupchaap 😎 bhej ke cool ban jaate?
Ankit ne (d) chuna: phone ulta rakh ke so gaya. Bunty ne us message pe 14 reactions daal diye.

**TAAZA add-on (2 minute ka asli kadam):**
Ankit ka pehla Python warm-up. Output kya aayega?
```python
x = 5
y = x
x = x + 2
print(x, y)
```
**Jawab:** `7 5`
**Kyun:** `y = x` ke waqt y ko 5 mil gaya. Baad mein x badla, y nahi badla, kyunki number ki value copy hoti hai.

---

### Din 2: Pehla ticket
**THAKA pack (sirf kahani):**
10 baje Ankit desk pe tha, 9:40 se. Meera di ne screen ghumayi. Ticket ka naam: "Bill mein sirf even number wale items ka total galat aa raha hai."
Ankit ne socha, "Bas? Ho jayega bhai." Code khola. Andar variables the: `a`, `b`, `xyz`, aur ek `temp`. Ankit ko apnapan mehsoos hua. Phir pata chala woh `temp` usne nahi, kisi purane intern ne likha tha jo ab Pune mein hai aur phone nahi uthata.
Do ghante baad Ankit ne fix banaya, apna naya variable daala: `temp2`. Bunty ne peeche se dekha aur hans hans ke chai gira di.
Meera di ne code review mein sirf ek line likhi: "Variable ka naam aisa rakho ki tumhari mummy bhi samajh jaaye."
Ankit ne `temp2` ko badal ke `temp_total` kar diya. Progress hai na?
Shaam ko test pass ho gaya. Ankit ne khushi mein mummy ko call kiya, "Mummy, mera code chal gaya!" Mummy boli, "Accha beta, khana khaya?"
Aur tabhi Slack pe laal dot aaya. Ek naya message. Sender: "Production Alerts".

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Tumhara sabse funny variable naam kya raha hai kabhi? `abc`? `pls_work`? `final_final`?
Ankit ka record: `temp_final_pakka_v3`. Usne khud maana ki v1 aur v2 kabhi the hi nahi.

**TAAZA add-on (2 minute ka asli kadam):**
Ankit wala ticket, chhota version. Output kya aayega?
```python
nums = [1, 2, 3, 4]
total = 0
for n in nums:
    if n % 2 == 0:
        total += n
print(total)
```
**Jawab:** `6`
**Kyun:** Sirf even numbers (2 aur 4) jude, 2 + 4 = 6.

---

### Din 3: Pehla production bug
**THAKA pack (sirf kahani):**
"Production Alerts" ka message tha: "Chai Point Gwalior: bill mein pehla item dikh hi nahi raha."
Ankit ka dil pet mein utar gaya. Gwalior! Jhansi ka padosi! Ab ghar tak baat jayegi.
Bunty ne turant meme bheja: ek aadmi jalte hue ghar ke saamne chai pi raha hai. Caption: "Ankit right now."
Meera di aayi, kursi kheenchi, baith gayi. Na gussa, na lecture. Bas bola, "Chalo, saath dekhte hain."
Code mein ek loop tha. Ankit ne dekha, phir dobara dekha. Loop 1 se start ho raha tha, 0 se nahi. Pehla item har baar chhoot raha tha. Ek number. Bas ek number ki galti.
Fix teen second ka tha. Dhoondhne mein ek ghanta laga.
Meera di uthte hue boli, "Sabse bade bug aksar sabse chhote hote hain." Ankit ko laga yeh line kisi film ki hai.
Raat ko Chai Point Gwalior wale uncle ne app pe review diya: "Ab sahi hai. Ladka accha hai." Ankit ne screenshot le liya, frame karwane ka plan bhi bana liya.
Par agle din subah, office mein ek naya chehra tha. Ek aur senior. Aur woh muskura nahi raha tha.

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Production mein bug aaye to tumhara pehla reaction kya hoga: (a) shaant rehna, (b) Bunty jaisa meme, (c) mummy ko call?
Ankit ka sach: pehle (c) socha, phir yaad aaya mummy poochengi "khana khaya?", to (a) pe aa gaya.

**TAAZA add-on (2 minute ka asli kadam):**
Bug pakdo! Isme gadbad kya hai?
```python
items = ["chai", "samosa", "bun"]
for i in range(1, len(items)):
    print(items[i])
```
**Jawab:** Yeh sirf `samosa` aur `bun` print karega, `chai` chhoot jaayegi.
**Kyun:** List ka index 0 se shuru hota hai. Fix: `range(len(items))` ya seedha `for item in items:`.

---

### Din 4: Rathore sir ka code review
**THAKA pack (sirf kahani):**
Naya chehra tha Rathore sir. Tech lead. Doosre office se aaye the, sirf ek hafte ke liye. Unke baare mein afwah thi ki unhone ek baar ek PR pe 47 comments diye the.
Ankit ka naya PR unke paas gaya. Ankit ne teen baar khud check kiya. `temp` sab hata diye. Sab variable ke naam sundar. "Ho jayega bhai."
Comment aaya. Sirf ek: "Yahan loop ke andar loop kyun hai? Hazaar items hue to kya hoga?"
Ankit ne socha, hazaar items? Chai ki dukaan pe hazaar items kaun bechta hai?
Bunty ne dhire se bataya, "Bhai, Indore wale ek client ki dukaan pe 1,200 items hain. Namkeen ke 300 type."
Ankit ne Rathore sir ke paas jaa ke poocha. Rathore sir ne napkin pe ek graph banaya. Ek line seedhi upar jaati hui. "Yeh tumhara code hai. Isse seedha karo."
Ankit ne loop ke andar wala loop hataya, ek dictionary use ki. Speed dus guna.
Rathore sir ne PR approve kiya. Bina ek shabd. Bunty bola, "Bhai, yeh to shaadi ke rishte se bada approval hai."
Par jaate jaate Rathore sir ne Meera di se kuch kaha. Aur dono ne Ankit ki taraf dekha.

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Guess karo: Rathore sir ne Meera di se kya kaha hoga? (a) "Ladka theek hai", (b) "Isko Friday deploy do", (c) "Iska variable naam check karo"?
Pata kal chalega. Par hint: Bunty ne sunte hi "RIP" likha.

**TAAZA add-on (2 minute ka asli kadam):**
3 chhote sawal, time complexity ke:
1. List mein ek item ko shuru se ek ek karke dhoondhna (linear search): (a) O(1) (b) O(n) (c) O(n²)
2. List mein index se item nikalna, jaise `items[5]`: (a) O(1) (b) O(n) (c) O(n²)
3. n items pe loop, uske andar phir n items pe loop: (a) O(n) (b) O(log n) (c) O(n²)

**Jawab:** 1-(b), 2-(a), 3-(c)
**Kyun:** Ek ek karke dekhna n kaam, index se seedha pahunchna ek kaam, aur loop ke andar loop n × n kaam.

---

### Din 5: Git ka gadbad jhala
**THAKA pack (sirf kahani):**
Rathore sir ne kya kaha tha? "Ankit ko agle Friday ka deploy do." Bunty ne "RIP" isliye likha tha.
Par pehle ek aur museebat aayi. Ankit ne subah kaam shuru kiya, bina latest code laaye. Do ghante code likha. Phir commit kiya, push kiya. Screen laal ho gayi. "Rejected."
Ankit ne Google se ek command uthayi aur chala di. Ab terminal mein ajeeb sa likha tha: "CONFLICT." Ankit ko laga koi jung shuru ho gayi.
Bunty bola, "Bhai, tune Meera di ka kaam overwrite toh nahi kar diya?" Ankit ka chehra Jhansi ki garmi jaisa safed pad gaya.
Meera di aayi. Screen dekhi. Haske boli, "Sab pehle din yahi karte hain. Main ne bhi kiya tha. Ek baar poori team ka kaam ud gaya tha."
"Phir?"
"Phir git ne bacha liya. Git kuch bhoolta nahi."
Dono ne milke conflict suljhaya. Meera di ne sikhaya: kaam shuru karne se pehle `git pull`. Ankit ne haath pe pen se likh liya.
Shaam ko Ankit ne pehli baar bina dar ke push kiya. Hara tick.
Phir calendar pe ek invite aaya: "Friday 5 PM: Production Deploy. Owner: Ankit."

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
"CONFLICT" padh ke tumhe kya yaad aata hai? Ghar mein remote ki ladai? Hostel mein last Maggi ka packet?
Ankit ko seedha yaad aaya: bhaiya ke saath cricket mein "out tha, nahi tha" wala jhagda. Woh bhi aaj tak resolve nahi hua.

**TAAZA add-on (2 minute ka asli kadam):**
Git ke 3 sawal:
1. Kaun si files badli hain, dekhne ke liye: (a) `git status` (b) `git push` (c) `git clone`
2. Badlaav ko ek message ke saath save karne ke liye: (a) `git pull` (b) `git commit -m "msg"` (c) `git log`
3. Remote se latest code laake apne branch mein milane ke liye: (a) `git push` (b) `git init` (c) `git pull`

**Jawab:** 1-(a), 2-(b), 3-(c)
**Kyun:** `status` haalat batata hai, `commit` save karta hai, `pull` naya code laata aur merge karta hai.

---

### Din 6: Friday 5 PM
**THAKA pack (sirf kahani):**
Friday. 4:55 PM. Poore office mein sannata. Bunty ne chips ka packet khola, jaise movie dekhne aaya ho.
Ankit ne deploy ka button dabaya. Progress bar chala. 20%... 60%... 100%. Hara.
"Ho gaya bhai!" Ankit ne haath upar kiye.
5:07 PM. Bunty ki screen pe laal. "Bhai... app khol ke dekh."
Login page pe likha tha: "Error 500."
Ankit ke haath thande. Meera di ne bina ghabraye logs khole. Ek line chamki: ek naya config value tha jo production mein set hi nahi tha. Ankit ki machine pe tha, server pe nahi.
"Rollback karein?" Meera di ne poocha. Ankit ne sir hilaya. Do minute mein purana version wapas. App chalu.
Phir dono ne config theek kiya aur 5:40 pe dobara deploy kiya. Is baar sab hara. Sach mein hara.
Rathore sir ka message aaya: "Friday deploy, sahi rollback. Accha." Ankit ne woh "Accha" 11 baar padha.
Ghar jaate waqt mummy ka call. "Beta, khana khaya?" Ankit ne kaha, "Mummy, aaj maine server bachaya." Mummy boli, "Accha. Khana khaya?"
Par Monday ko ek naya kaam milne wala tha. Database ka.

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Tum hote to 5:07 pe kya karte: (a) rollback, (b) turant fix try, (c) chips Bunty se le ke kha lete?
Ankit ne (a) chuna, aur sahi chuna. Pehle app chalao, phir aaram se galti dhoondho. (c) baad mein hua.

**TAAZA add-on (2 minute ka asli kadam):**
HTTP status codes ka match karo:
1. `200` (a) Page/cheez mili hi nahi
2. `404` (b) Sab theek, kaam ho gaya
3. `500` (c) Server ke andar kuch toot gaya

**Jawab:** 200-(b), 404-(a), 500-(c)
**Kyun:** 2xx matlab success, 4xx matlab request mein dikkat (client side), 5xx matlab server ki galti.

---

### Din 7: Database wala darr
**THAKA pack (sirf kahani):**
Monday. Ticket: "Jhansi ke sabhi customers ki list nikalo, marketing ko chahiye." Ankit khush. Apna sheher!
Meera di ne database ka access diya aur ek baat boli, dheere se, jaise koi raaz: "Kabhi bhi DELETE likho, to WHERE pehle likhna."
Ankit hasa. "Di, main to sirf SELECT kar raha hoon."
Query likhi, chalayi. 312 customers. Ankit ne naam padhe. Ek naam jaana pehchana laga: "Sharma General Store, Sipri Bazaar." Yeh to woh dukaan thi jahan se Ankit bachpan mein Parle-G lene jaata tha!
Bunty ne dekha aur bola, "Bhai, tera bachpan ab tera client hai. Bill galat aaya to chacha seedha teri mummy ko batayenge."
Phir Bunty ne ek kahani sunayi: ek purane intern ne ek baar WHERE bhool ke poori table delete kar di thi. Backup se 4 ghante mein wapas aaya. Us din se office mein ek rule hai: jo bhi aisa kare, poori team ke liye samose laata hai.
Ankit ne apne haath pe pen se doosri line likhi: "WHERE pehle."
Shaam ko Meera di ne kaha, "Is Thursday client demo hai. Tum present karoge."
Ankit ka "ho jayega bhai" is baar gale mein atak gaya.

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Agar tumhari team mein bhi "samosa rule" hota, to kis galti pe lagta? Late standup? Galat branch pe push?
Bunty ka sujhav: "Jo variable ka naam `temp` rakhe." Ankit ne turant topic badal diya.

**TAAZA add-on (2 minute ka asli kadam):**
Table `customers` mein yeh 3 rows hain:
| name | city |
|---|---|
| Sharma Store | Jhansi |
| Gupta Chai | Gwalior |
| Raju Tea | Jhansi |

Is query ka output kya hoga?
```sql
SELECT name FROM customers WHERE city = 'Jhansi';
```
**Jawab:** `Sharma Store` aur `Raju Tea` (2 rows)
**Kyun:** `WHERE` sirf un rows ko chunta hai jinka city 'Jhansi' hai. Bonus: `DELETE FROM customers;` bina WHERE ke saari rows uda deta. Isliye "WHERE pehle."

---

### Din 8: Demo ki taiyaari
**THAKA pack (sirf kahani):**
Demo ek bade client ke saamne tha: ek chai chain jiske 40 outlet the. Agar unhe pasand aaya, ChaiByte ka agla saal set.
Ankit ne slides banayi. Pehli slide pe bada sa likha: "Welcome." Meera di ne dekha aur kaha, "Client ko feature dikhao, welcome nahi."
Ankit ne slides kam ki, demo zyada rakha. Har button do baar test kiya. Phir teesri baar. Bunty ne beech mein ek fake order daala, "Masala chai × 999." App ne theek handle kiya. Ankit ne chain ki saans li.
Raat ko practice ki, PG ke kamre mein, sheeshe ke saamne. Roommate ne darwaze se jhaanka aur bola, "Bhai, shaadi ka speech hai kya?"
Ek aur cheez hui. Code ke ek kone mein Ankit ko apna hi purana variable mila: `temp_final_pakka`. Teen hafte purana. Ab Ankit khud nahi samajh pa raha tha ki yeh kya karta hai.
Usne dhire se uska naam badla: `order_discount`. Aur pehli baar Meera di wali baat samajh aayi: naam tumhare liye bhi hote hain, teen hafte baad wale tumhare liye.
Raat 1 baje phone pe message. Bunty: "Bhai, kal ka WiFi... wahan WiFi hai na?"
Kisi ne check nahi kiya tha.

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Demo se pehle raat ka tumhara ritual kya hoga: (a) poori raat practice, (b) jaldi so jaana, (c) Bunty ki tarah 1 baje darr bhejna?
Ankit ne (a) socha, (b) kiya nahi, aur (c) ka shikaar hua. Classic.

**TAAZA add-on (2 minute ka asli kadam):**
String slicing! Output kya hoga?
```python
s = "deploy"
print(s[:3], s[-2:])
```
**Jawab:** `dep oy`
**Kyun:** `s[:3]` index 0, 1, 2 deta hai ("dep"). `s[-2:]` aakhri do letters deta hai ("oy"). `print` beech mein space laga deta hai.

---

### Din 9: Demo day
**THAKA pack (sirf kahani):**
Client ka office. Kaanch ki deewarein. Ek bada TV. Aur WiFi... jiska password kisi ko nahi pata tha.
Ankit ka "ho jayega bhai" poori tarah gaayab. Bunty ne apne phone ka hotspot on kiya. Signal: ek dandi. Ankit ne man hi man Jhansi ke Hanuman ji ko yaad kiya.
Demo shuru hua. Login: chala. Menu: chala. Order: thoda soch ke, par chala. Client ke manager ne poocha, "Agar 40 outlet ek saath bill banaye to?"
Ankit ko Rathore sir ka napkin wala graph yaad aaya. Usne aaram se samjhaya ki loop ke andar loop kyun hataya tha, aur dictionary se kaise tez hua. Manager ne sir hilaya.
Phir aakhri sawal: "Galti hui to?" Ankit ne Friday 5:07 ki kahani suna di. Rollback, do minute, app wapas. Manager pehli baar muskuraya. "Achha hai. Galti chhupate nahi ho."
Bahar nikle to Bunty ne Ankit ko gale lagaya, phir turant bola, "Bhai, mera 400 MB data gaya, wapas dega?"
Meera di ka message aaya: "Kal subah jaldi aana. Kuch dikhana hai."
Kuch accha? Ya kuch aur?

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Guess karo, Meera di kya dikhana chahti hain: (a) client ka jawab, (b) Ankit ka naya bug, (c) office ka naya samosa rule?
Answer kal. Par ek hint: Meera di ne message ke saath ek smiley bheja tha. Pehli baar.

**TAAZA add-on (2 minute ka asli kadam):**
Dictionary ka sawal (wahi jisne Ankit ko bachaya). Output kya hoga?
```python
d = {"a": 1, "b": 2}
d["a"] = d["a"] + d["b"]
d["c"] = 5
print(len(d), d["a"])
```
**Jawab:** `3 3`
**Kyun:** `d["a"]` ban gaya 1 + 2 = 3. `"c"` naya key juda, to total 3 keys hui.

---

### Din 10: Naam wala commit
**THAKA pack (sirf kahani):**
Subah 9 baje. Meera di ne screen ghumayi. Client ka email: "Hum 40 outlets ke liye aage badhna chahte hain."
Office mein shor. Bunty ne table pe dhol bajaya. Plastic wala plant gir gaya.
Phir Meera di ne doosri cheez dikhayi. Release notes. Sabse neeche ek line: "Billing loop fix aur speed improvement: Ankit Dubey."
Ankit ka naam. Asli code mein. Asli dukaanon mein. Gwalior wale uncle, Indore ke 300 namkeen, aur Sipri Bazaar ke Sharma chacha, sab ke bill mein thoda sa Ankit.
Rathore sir ka bhi message aaya, doosre office se: "Suna demo accha gaya. Variable ke naam ab bhi check karta hoon." Ankit hasa.
Shaam ko mummy ka call. "Beta, khana khaya?" Is baar Ankit ne pehle jawab diya: "Haan mummy, khaya. Aur suno, aaj mera naam aaya hai."
Mummy chup. Phir boli, "Sharma ji ki dukaan wala app? Wahi tera hai?"
"Haan mummy."
"Arre! Unko bata deti hoon."
Ankit ne laptop band kiya. Kal naya ticket tha. Uska naam tha: "Ek naya feature, shuru se. Owner: Ankit."
Pehli baar, "ho jayega bhai" sach mein bharose se nikla.

Aaj ka rest poora. Kal milte hain.

**THEEK add-on (ek mazedaar sawal):**
Agar tumhara naam kabhi kisi release notes mein aaye, to sabse pehle kise batayoge?
Ankit ne socha tha Bunty ko. Par mummy pehle pahunch gayi, aur Sharma chacha tak khabar 10 minute mein pahunch gayi.

**TAAZA add-on (2 minute ka asli kadam):**
Aakhri puzzle. Output kya hoga?
```python
n = 10
count = 0
while n > 1:
    n = n // 2
    count += 1
print(count)
```
**Jawab:** `3`
**Kyun:** n chalta hai 10 → 5 → 2 → 1. Teen baar aadha hua, phir loop ruka. Har baar aadha karna hi O(log n) ka jaadu hai.

---

## Jaanchne layak facts
Koi nahi. (Saare snippets do baar mann mein chalaye gaye: Din 1 `7 5`, Din 2 `6`, Din 3 sirf `samosa` aur `bun`, Din 8 `dep oy`, Din 9 `3 3`, Din 10 `3`.) Founder ek baar yeh dekh le ki "ChaiByte" naam ki koi asli company to nahi hai; agar ho, to naam badal dein.
