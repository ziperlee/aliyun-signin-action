import pushplus
from os import environ


def main():
  config = {
      "pushplus_token": environ['PUSHPLUS_TOKEN'],
      "pushplus_topic": ""
  }
  content = f"测试数据推送: {environ['GP_TOKEN']}"
  content_html = ""
  title = "测试数据推送"
  pushplus.push(config, content, content_html, title)

main()
