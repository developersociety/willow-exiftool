# willow-exiftool

[ExifTool](https://exiftool.org/) optimizer for [Willow](https://github.com/wagtail/Willow), to
strip out excessive Exif data.

## Installation

Using [pip](https://pip.pypa.io/):

```console
$ pip install willow-exiftool
```

You'll also need to install ExifTool if you don't have it already. For Debian/Ubuntu you can use
apt, other distributions should also have packages:

```console
$ sudo apt install exiftool
```

Edit your Django project's settings module, and add the application to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "willow_exiftool",
    # ...
]
```

Also add/update `WILLOW_OPTIMIZERS` to enable the optimizer:

```python
WILLOW_OPTIMIZERS = "exiftool"
```
