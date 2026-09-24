import core


def login_page(navigator):
    """
TODO : هناخد الميل والباس لو ادمن نحول لادمن بيدج ولو اليوزر ليوز
    """
    pass


def register_page(navigator):
    """
    TODO:  بيانات التسجيل  مع التحقق
          (core.validate) ونادي core.register_user()
    """
    pass


def home_page(navigator, current_user):
    """TODO: اعرض core.CATEGORIES المستخدم يختار """
    pass


def category_page(navigator, category_name, current_user):
    """
    TODO:
        1) core.get_by_category(category_name)
        2) اعرض خيارات: بحث (core.search_attraction_by_name) /
           ترتيب (core.sort_attractions) / فتح تفاصيل / رجوع
    """
    pass


def attraction_detail_page(navigator, attraction, current_trip):
    """
    TODO: اعرض تفاصيل المكان وزرار إضافة/إزالة من الرحلة
          (core.add_to_trip / core.remove_from_trip)
    """
    pass


def my_trip_page(navigator, current_trip):
    """TODO: اعرض كل الأماكن المختارة في current_trip"""
    pass


def final_summary_page(navigator, current_trip, current_user):
    """TODO: نادي core.calculate_final_summary() واعرض النتيجة"""
    pass


def admin_menu(navigator):
    """
    TODO: اعرض خيارات Add / Update / Remove attraction ونادي
          core.add_attraction / core.update_attraction /
          core.remove_attraction
    """
    pass


def run():
    """

    TODO:
        1) navigator = core.PageNavigator()
        2) ابدأ ب login_page(navigator)
        # لازممممممممممممم
        3) اعمل main loop بيفضل شغال لحد ما المستخدم يختار Exit
    """
    pass


if __name__ == "__main__":
    run()
