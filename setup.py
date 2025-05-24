from setuptools import setup

setup(
    name='utilitasparserkustom',  # Nama paket saat diinstal
    version='0.1.0',
    py_modules=['parser_utils'], # Menunjukkan file .py mana yang menjadi modul
    install_requires=[
        # Jika parser_utils.py Anda butuh library lain, tambahkan di sini
        # 'regex', # Contoh, jika Anda pakai library regex pihak ketiga
    ],
    author='Nama Anda',
    author_email='email@anda.com',
    description='Kumpulan utilitas parser kustom.',
    # url='https://github.com/usernameanda/utilitas-parser-saya', # Opsional
)
