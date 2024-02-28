def upload_products(instance, filename):
    return f"image/{instance.tort_image}/{filename}"


def upload_images(instance, filename):
    return f"images/{instance.flour_image}/{filename}"
