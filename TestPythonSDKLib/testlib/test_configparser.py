import configparser
import os

base_path = os.path.abspath(os.path.dirname(__file__))
conf_path = os.path.join(base_path, "config", "conf.ini")

conf = configparser.ConfigParser()

if not conf.has_section("redis"):
    conf.add_section("redis")
conf.set("redis", "host", "10.10.100.1")
conf.set("redis", "port", "6379")
print(conf.get("redis", "host"))

conf.set(conf.default_section, "host", "10.10.100.2")
print(conf.defaults())


# 持久化为文件
if not os.path.exists(os.path.dirname(conf_path)):
    os.makedirs(os.path.dirname(conf_path))
f = open(conf_path, "w+", encoding="utf-8")
conf.write(f)


# 从文件中加载配置
conf.read(conf_path, encoding="utf-8")
print(conf.sections())
print(conf.options("redis"))

