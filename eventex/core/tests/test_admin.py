from django.test import TestCase
from eventex.core.admin import SpeakerModelAdmin, Speaker, Contact, Talk, Course, TalkModelAdmin, admin


class SpeakerModelAdminTest(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(name='Henrique Bastos', slug='henrique-bastos',
                               photo='http://hbn.link/hb-pic', website='http://henriquebastos.net',
                               description='Palestrante')

        Contact.objects.create(speaker=speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        Contact.objects.create(speaker=speaker, kind=Contact.PHONE, value='99-99999-9999')

        self.queryset = Speaker.objects.all()
        self.model_admin = SpeakerModelAdmin(Speaker, admin.site)

    def test_website_link(self):
        expected = '<a href="{0}">{0}</a>'.format('http://henriquebastos.net')
        self.assertEqual(expected, self.model_admin.website_link(self.queryset[0]))

    def test_photo_img(self):
        expected = '<img width="32px" src="http://hbn.link/hb-pic" />'
        self.assertEqual(expected, self.model_admin.photo_img(self.queryset[0]))

    def test_email(self):
        compare = (
            (Contact.EMAIL, self.model_admin.email(self.queryset[0]).kind),
            ('henrique@bastos.net', self.model_admin.email(self.queryset[0]).value)
        )
        for expected, result in compare:
            with self.subTest():
                self.assertEqual(expected, result)

    def test_phone(self):
        compare = (
            (Contact.PHONE, self.model_admin.phone(self.queryset[0]).kind),
            ('99-99999-9999', self.model_admin.phone(self.queryset[0]).value)
        )
        for expected, result in compare:
            with self.subTest():
                self.assertEqual(expected, result)


class TalkModelAdminTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Título da palestra', start='09:00', )
        Course.objects.create(title='Título do curso', start='10:00', slots=20)
        self.model_admin = TalkModelAdmin(Talk, admin.site)

    def test_get_queryset(self):
        """Model admin queryset must contain only talks"""
        qs = self.model_admin.get_queryset({})
        expected = ['Título da palestra']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)
