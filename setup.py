from setuptools import setup, find_packages

setup(
    name="BNS_network_toolkit",  # نام برنامه
    version="1.0.0",  # نسخه برنامه
    author="Erfan Parasti",  # نام سازنده
    author_email="Erfan.mail@gmail.com",  # ایمیل سازنده
    description="BNS Network Toolkit for scanning and analysis",  # توضیحات کوتاه
    long_description=open("README.md").read(),  # توضیحات طولانی از فایل README
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/BNS_network_toolkit",  # لینک به مخزن گیت‌هاب (در صورت وجود)
    packages=find_packages(),  # بسته‌ها را به‌طور خودکار پیدا می‌کند
    include_package_data=True,
    install_requires=[
        "colorama",  # برای رنگی کردن متن در ترمینال
        "scapy",  # برای اسکن شبکه و آنالیز بسته‌ها
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # نسخه پایتون مورد نیاز
    entry_points={
        "console_scripts": [
            "BNS_network_toolkit=main:main",  # دستوری برای اجرای برنامه
        ],
    },
)
