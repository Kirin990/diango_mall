"""
Generate verification code:
1. Prepare materials
Font (ttf), text content, color, interference lines
2. Draw verification code
pip install Pillow, random
Create picture
Record text content, django session [server, python code]
abcdefg cookie [Browser]

(1) The first request, cookie + session correspondence is generated
(2) The second request, carrying cookies, find the corresponding session [submit form]
     Request to bring verification code parameter and compare with verification code in session
3. io file stream
BytesIO
"""
import random

import os

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from io import BytesIO

from django.http import HttpResponse


class VerifyCode(object):
    """ Verification code """

    def __init__(self, dj_request):
        self.dj_request = dj_request
        # Verification code length
        self.code_len = 4
        # Captcha image size
        self.img_width = 100
        self.img_height = 30

        # The name of the session in django
        self.session_key = 'verify_code'

    def gen_code(self):
        """ Generate verification code """
        # 1.Generate a verification code string using random numbers
        code = self._get_vcode()
        # 2.The session where the verification code exists
        self.dj_request.session[self.session_key] = code
        # 3.Prepare random elements (background color, color of captcha text, interference lines,)
        font_color = ['black', 'darkblue', 'darkred', 'brown', 'green', 'darkmagenta', 'cyan', 'darkcyan']
        # RGB random background color
        bg_color = (random.randrange(230, 255), random.randrange(230, 255), random.randrange(230, 255))
        # Font path
        font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts', 'timesbi.ttf')

        # Create picture
        im = Image.new('RGB', (self.img_width, self.img_height), bg_color)
        draw = ImageDraw.Draw(im)

        # Draw interference lines
        # Random number, draw a few in the end
        for i in range(random.randrange(1, int(self.code_len / 2) + 1)):
            # Line color
            line_color = random.choice(font_color)
            # Line position
            point = (
                random.randrange(0, self.img_width * 0.2),
                random.randrange(0, self.img_height),
                random.randrange(self.img_width - self.img_width * 0.2, self.img_width),
                random.randrange(0, self.img_height))
            # Line width
            width = random.randrange(1, 4)
            draw.line(point, fill=line_color, width=width)

        # Draw verification code
        for index, char in enumerate(code):
            code_color = random.choice(font_color)
            # Specify font
            font_size = random.randrange(15, 25)
            font = ImageFont.truetype(font_path, font_size)
            point = (index * self.img_width / self.code_len,
                     random.randrange(0, self.img_height / 3))
            draw.text(point, char, font=font, fill=code_color)

        buf = BytesIO()
        im.save(buf, 'gif')
        return HttpResponse(buf.getvalue(), 'image/gif')

    def _get_vcode(self):
        random_str = 'ABCDEFGHIGKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
        code_list = random.sample(list(random_str), self.code_len)
        code = ''.join(code_list)
        return code

    def validate_code(self, code):
        """ Verify the verification code is correct """
        # 1.Change case
        code = str(code).lower()
        vcode = self.dj_request.session.get(self.session_key, '')
        # if vcode.lower() == code:
        #     return True
        # return False
        return vcode.lower() == code


if __name__ == '__main__':
    client = VerifyCode(None)
    client.gen_code()
