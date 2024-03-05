# glados-checkin-python

**English** | [简体中文](./README.md)

## Usage

> This project does not use Github Action, please deploy your own

Import the environment variables with export, or rename the `.env.example` file to `.env` and fill in the information accordingly
```bash
export GLADOS_COOKIE="<your_glados_cookie>"   # Require
export FEISHU_WEBHOOK="<your_feishu_webhook>" # Optional
```

```bash
# Execute once
python main.py

# It is executed every 24 hours
python main.py -i 24
```
