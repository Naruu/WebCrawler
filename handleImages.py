from PIL import Image, ImageFilter

logo = Image.open('logo.jpg')
blurryLogo = logo.filter('ImageFilter.GaussianBlur')
blurryLogo.save('logo_bluurred.jpg')
blurryLogo.show()