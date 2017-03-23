from app.extensions import nav
from flask_nav.elements import Navbar, View, Subgroup, Separator, Link, Text


@nav.navigation()
def navbar():
    return Navbar(
        'Ryan Ground Hotel',
        View('Home', 'home'),
        View('Register', 'register'),
        View('Log in', 'login'),
        View('Log out', 'logout'),
        Subgroup(
            'Booking',
        View('Booking', 'make_book_form'),
        View('Cancel', 'cancel_booking_form'),
        ),
        Subgroup(
            'Test',
            View('admin role', 'special_admin'),
            View('guest role', 'special_guest'),
            Separator(),
            Text('Testing'),
            View('Login required', 'special'),
        ),
    )
