from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator
from .redir import blog
from .redir import blog_entry
from .redir import blog_slash
from .redir import book
from .views import contact
from .views import default
import deform_bootstrap


def main(global_config, **settings):
    """
    Oppan wsgi style! Configure and return WSGI application.
    """
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(session_factory=my_session_factory)
    config.include('pyramid_mako')
    config.add_route('blog', '/blog')
    config.add_route('blog_entry', '/blog/{entry:.*}')
    config.add_route('blog_slash', '/blog/')
    config.add_route('book', '/book')
    config.add_route('book-promo', '/book-promo')
    config.add_route('contact', '/contact')
    config.add_route('clients', '/clients')
    config.add_route('services', '/services')
    config.add_route('team', '/team')
    config.add_route('technology', '/technology')
    config.add_route('testimonials', '/testimonials')
    config.add_route('root', '/')
    config.add_static_view(
        'static', 'aclarknet:static', cache_max_age=3600)
    config.add_view(blog, route_name='blog')
    config.add_view(blog_entry, route_name='blog_entry')
    config.add_view(blog_slash, route_name='blog_slash')
    config.add_view(book, route_name='book')
    config.add_view(
        default,
        renderer='aclarknet:templates/book.mak',
        route_name='book-promo')
    config.add_view(
        default,
        renderer='aclarknet:templates/clients.mak',
        route_name='clients')
    config.add_view(
        contact,
        renderer='aclarknet:templates/contact.mak',
        route_name='contact')
    config.add_view(
        default,
        renderer='aclarknet:templates/technology.mak',
        route_name='technology')
    config.add_view(
        default,
        renderer='aclarknet:templates/root.mak',
        route_name='root')
    config.add_view(
        default,
        renderer='aclarknet:templates/services.mak',
        route_name='services')
    config.add_view(
        default,
        renderer='aclarknet:templates/testimonials.mak',
        route_name='testimonials')
    config.add_view(
        default,
        renderer='aclarknet:templates/team.mak',
        route_name='team')
    config.include(deform_bootstrap)
    return config.make_wsgi_app()
