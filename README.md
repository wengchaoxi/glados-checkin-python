# glados-checkin-python

**简体中文** | [English](./README.en-US.md)

## Usage

> 本项目不使用 Github Action，请自行部署

使用 export 导入环境变量，或者将 `.env.example` 文件重命名为 `.env` 并填写相应信息
```bash
export GLADOS_COOKIE="<your_glados_cookie>"   # 必须的
export FEISHU_WEBHOOK="<your_feishu_webhook>" # 可选
```

```bash
# 执行一次
python main.py

# 每隔 24 小时执行一次
python main.py -i 24
```
