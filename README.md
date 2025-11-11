# MiniAuth

MiniAuth 是一个基于 **FastAPI** 实现的轻量级用户认证系统，提供用户注册、登录与身份验证功能。


## 🧱 技术栈
| 技术 | 用途 |
|-----|-----|
| Python | 项目主语言 |
| FastAPI | Web 框架 |
| SQLite | 简单数据库存储用户信息 |
| passlib[bcrypt] | 密码加密 |
| python-jose | JWT Token 生成与验证 |
| Uvicorn | 开发服务器 |

## ✅ 当前进度
- 项目结构初始化 ✅
- 基础 FastAPI 路由 ✅

## 📦 启动方式
pip install -r requirements.txt
uvicorn app.main:app --reload

访问： http://127.0.0.1:8000/

## 🗓 项目路线图
- [ ] 用户模型设计
- [ ] 注册接口（带密码加密）
- [ ] 登录接口（生成 JWT token）
- [ ] 个人信息接口（需要 token 才能访问）
- [ ] 简单前端页面（可选）
- [ ] 部署到 Render / Railway （免费上线）
