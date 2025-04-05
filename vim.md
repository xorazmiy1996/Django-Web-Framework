### 1. `Vim` nima?

> `Vim` - bu kuchli, sozlanishi mumkin bo'lgan matn tahrirlovchi dastur bo'lib, asosan terminalda ishlatiladi. Uni
`Vi Improved` (`Vi` ning takomillashtirilgan versiyasi) deb ham atashadi.

**Afzalliklari:**

- Barcha Unix/Linux tizimlarida o'rnatilgan keladi
- Juda tez va yengil
- Pluginlar orqali kengaytirish mumkin
- Klaviatura bilan samarali ishlash

**Vimda Eng Ko'p Ishlatiladigan Asosiy Buyruqlar:**

| Buyruq                | Nima uchun ishlatilishi:           |
|-----------------------|------------------------------------|
| `:w`                  | Faylni saqlash (write)             |
| `:q`                  | Vimdan chiqish (quit)              |
| `:wq`                 | Saqlab chiqish (write + quit)      |
| `:q!`                 | O'zgarishlarni saqlamasdan chiqish |
| `:e file.txt`         | Boshqa faylni ochish (edit)        |
| `:saveas newfile.txt` | Yangi nom bilan saqlash            |

2. **Harakatlanish**

| Buyruq | Nima uchun ishlatilishi: |
|--------|--------------------------|
| `h`    | Chapga (←)               |
| `j`    | Pastga (↓)               |
| `k`    | Tepaga (↑)               |
| `l`    | O'ngga (→)               |
| `w`    | Keyingi so'z boshiga     |
| `b`    | Oldingi so'z boshiga     |
| `0`    | Joriy qator boshiga      |
| `$`    | Joriy qator oxiriga      |
| `gg`   | Fayl boshiga             |
| `G`    | Fayl oxiriga             |
| `:10`  | 10-qatorga o'tish        |

3. **Matnni O'zgartirish**

| Buyruq    | Nima uchun ishlatilishi:        |
|-----------|---------------------------------|
| `i`       | Kursor oldiga yozish (insert)   |
| `a`       | Kursor keyiniga yozish (append) |
| `o`       | Yangi qator ochish (pastga)     |
| `0`       | Yangi qator ochish (tepaga)     |
| `x`       | Belgini o'chirish               |
| `dd`      | Butun qatorni o'chirish         |
| `yy`      | Qatorni nusxalash (yank)        |
| `p`       | Nusxalangan matnni qo'yish (paste)                                |
| `u`       |Oxirgi amalni bekor qilish (undo)                                 |
| `ctr + r` | Qaytarish (redo)                                |

**Misol: Oddiy Fayl Tahrirlash**

1. Terminalda `vim test.txt` yozing
2. `i` tugmasini bosib matn yozing
3. `Esc` tugmasi bilan Normal rejimga qayting
4. `:wq` yozib faylni saqlab chiqing

**`Vim` ni Tez O'rganish uchun Maslahatlar**

1. Har doim `Esc` tugmasi bilan Normal rejimga qayting
2. `:help` buyruq yozib har qanday buyruq haqida yordam oling
3. `vimtutor` dasturini ishga tushiring (terminalda yozing)

> `Vim` dastlab qiyin ko'rinishi mumkin, lekin bir marta o'rgansangiz, boshqa tahrirlovchilarga qaytishni xohlamaysiz! 🚀













































































































