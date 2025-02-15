from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚 Mavjud Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="ℹ️ Biz haqimizda", callback_data="about"),
        ],
        [
            InlineKeyboardButton(text="📞 Aloqa", callback_data="contact"),
            InlineKeyboardButton(text="📍 Manzil", callback_data="location"),
        ],
        [
            InlineKeyboardButton(text="📝 Ro'yxatdan O'tish", callback_data="register"),
            InlineKeyboardButton(text="📰 Yangiliklar", callback_data="news"),
        ],
        [
            InlineKeyboardButton(text="💡 Takliflar", callback_data="feedback"),
        ],
    ]
)





# Kurslar uchun tugmalarni yaratish
menu_courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Backend Dasturlash", callback_data="backend"),
            InlineKeyboardButton(text="🌐 Frontend Dasturlash", callback_data="frontend"),
        ],
        [
            InlineKeyboardButton(text="🖥 Kompyuter Savodxonligi", callback_data="computer_literacy"),
            InlineKeyboardButton(text="🎨 Grafik Dizayn", callback_data="graphic_design"),
        ],
        [
            InlineKeyboardButton(text="📱 SMM", callback_data="smm"),
            InlineKeyboardButton(text="🏛 Foundation", callback_data="foundation"),
        ],
        [
            InlineKeyboardButton(text="🤖 Robototexnika", callback_data="robotics"),
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="main_menu"),
        ],
    ]
)
