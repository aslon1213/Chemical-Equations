from .views import (
    create_reactions_view,
    show_reaction_description_view,
    home,
    contact_view,
)
from django.urls import path


urlpatterns = [
    path("create_reactions/", create_reactions_view, name="create_reactions"),
    path(
        "show_reaction/<int:reaction_id>/",
        show_reaction_description_view,
        name="show_reaction",
    ),
    path("", home, name="home"),
    path("contact/", contact_view, name="contact"),
]
