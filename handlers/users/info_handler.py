from aiogram import types
from keyboards.inline.menu import menu  # Asosiy menyu
from loader import dp
from keyboards.inline.menu import menu_courses


@dp.callback_query_handler(text="courses")
async def show_courses(call: types.CallbackQuery):
    await call.message.edit_text("Bizda  mavjud kurslar", reply_markup=menu_courses)


@dp.callback_query_handler(text="backend")
async def backend_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "💻 *Backend Dasturlash* kursi haqida ma'lumot:\n\n"
        "- Bu kursda Python, Django va REST API larni o'rganasiz.\n"
        "- Kurs davomiyligi: 3 oy\n\n"
        "🔙 Orqaga qaytish uchun 'Orqaga' tugmasini bosing.",
        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()

@dp.callback_query_handler(text="frontend")
async def frontend_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "🌐 *Frontend Dasturlash* kursi:\n\n"
        "- HTML, CSS, JavaScript va React haqida chuqur bilimlar beriladi.\n"
        "- Kurs davomiyligi: 3 oy\n\n",

        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()

@dp.callback_query_handler(text="computer_literacy")
async def computer_literacy_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "🖥 *Kompyuter Savodxonligi* kursi:\n\n"
        "- Kompyuterning asosiy tushunchalari va dasturlar bilan ishlashni o'rganing.\n"
        "- Kurs davomiyligi: 1 oy\n\n",

        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()

@dp.callback_query_handler(text="graphic_design")
async def graphic_design_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "🎨 *Grafik Dizayn* kursi:\n\n"
        "- Adobe Photoshop, Illustrator va CorelDRAW bilan ishlashni o'rganasiz.\n"
        "- Kurs davomiyligi: 2 oy\n\n",

        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()

@dp.callback_query_handler(text="smm")
async def smm_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "📱 *SMM* kursi:\n\n"
        "- Ijtimoiy tarmoqlarda marketing va kontent yaratishni o'rganing.\n"
        "- Kurs davomiyligi: 1,5 oy\n\n",

        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()

@dp.callback_query_handler(text="foundation")
async def foundation_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "🏛 *Foundation* kursi:\n\n"
        "- Akademik asoslarni o'rganing va tayyorgarlik ko'ring.\n"
        "- Kurs davomiyligi: 6 oy\n\n",

        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()

@dp.callback_query_handler(text="robotics")
async def robotics_course(call: types.CallbackQuery):
    await call.message.edit_text(
        "🤖 *Robototexnika* kursi:\n\n"
        "- Robotlar yaratish va dasturlashni o'rganing.\n"
        "- Kurs davomiyligi: 2 oy\n\n",

        reply_markup=menu_courses,
        parse_mode="Markdown"
    )
    await call.answer()




# Orqaga tugmasi bosilganda asosiy menyuga qaytarish
@dp.callback_query_handler(text="main_menu")
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        "Asosiy menyuga qaytdingiz! 🎯\n"
        "Quyidagi tugmalar orqali tanlovni davom ettiring:",
        reply_markup=menu,
        parse_mode="Markdown"
    )
    await call.answer()




# "Biz haqimizda" tugmasi
@dp.callback_query_handler(text="about")
async def about_us(call: types.CallbackQuery):
    await call.message.edit_text(
        "ℹ️ *Biz haqimizda*\n\n"
        "IT TAT O'quv Markazi zamonaviy IT yo'nalishlarida ta'lim beradi. "
        "Maqsadimiz – yoshlarni zamonaviy bilimlar bilan ta'minlash!\n\n",

        reply_markup=menu,
        parse_mode="Markdown"
    )
    await call.answer()


# "Aloqa" tugmasi
@dp.callback_query_handler(text="contact")
async def contact_info(call: types.CallbackQuery):
    await call.message.edit_text(
        "📞 *Aloqa ma'lumotlari:*\n"
        "📱 Telefon: +998 90 123 45 67\n"
        "📧 Email: info@ittat.uz\n\n",

        reply_markup=menu,
        parse_mode="Markdown"
    )
    await call.answer()

# "Manzil" tugmasi
@dp.callback_query_handler(text="location")
async def location_info(call: types.CallbackQuery):
    await call.message.edit_text(
        "📍 *Bizning manzil:*\n"
        "Toshkent sh., Amir Temur ko'chasi, 10-uy.\n\n"
        "🌍 [Google Xaritada ochish](https://goo.gl/maps/example)\n\n",

        reply_markup=menu,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
    await call.answer()

# "Ro'yxatdan o'tish" tugmasi
@dp.callback_query_handler(text="register")
async def register(call: types.CallbackQuery):
    await call.message.edit_text(
        "📝 *Ro'yxatdan o'tish uchun:*\n"
        "📞 Telefon: +998 90 123 45 67\n"
        "🌐 Web-saytimiz: [it-tat.uz](https://it-tat.uz)\n\n",

        reply_markup=menu,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
    await call.answer()

# "Yangiliklar" tugmasi
@dp.callback_query_handler(text="news")
async def news_info(call: types.CallbackQuery):
    await call.message.edit_text(
        "📰 *Yangiliklar va aktsiyalar:*\n"
        "- Sentyabr oyi uchun 20% chegirma!\n"
        "- Yangi *Python Backend* kursi ro'yxati ochildi!\n\n",

        reply_markup=menu,
        parse_mode="Markdown"
    )
    await call.answer()

# "Takliflar" tugmasi
@dp.callback_query_handler(text="feedback")
async def feedback(call: types.CallbackQuery):
    await call.message.edit_text(
        "💡 *Taklif va mulohazalaringizni kutib qolamiz!*\n"
        "📩 Email: feedback@ittat.uz\n\n",

        reply_markup=menu,
        parse_mode="Markdown"
    )
    await call.answer()

# Orqaga tugmasi bosilganda asosiy menyuga qaytarish
@dp.callback_query_handler(text="main_menu")
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        "Asosiy menyuga qaytdingiz! 🎯\n"
        "Quyidagi tugmalar orqali tanlovni davom ettiring:",
        reply_markup=menu,
        parse_mode="Markdown"
    )
    await call.answer()
