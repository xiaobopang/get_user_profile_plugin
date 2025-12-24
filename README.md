# Get User Profile Plugin

这是一个 Dify 工具插件，用于获取用户信息。

## 功能

- 调用外部 API 获取用户个人信息
- 支持从请求中获取 Authorization token
- 返回用户信息包括：user_id, email, user_name, timezone, language, created_time

## 安装

1. 将插件打包为 .pkg 文件
2. 在 Dify 中导入插件
3. 在 Agent 应用中启用该工具

## 使用

在 Agent 应用的提示词中，可以引导模型调用 `get_user_profile` 工具来获取用户信息。

## API 接口

- URL: http://43.130.39.119/user/get_profile
- Method: POST
- Headers: Authorization: Bearer {token}
- Body: {}

## 返回数据格式

```json
{
  "result": 0,
  "data": {
    "user": {
      "user_id": "用户ID",
      "email": "邮箱",
      "user_name": "昵称",
      "timezone": "时区",
      "language": "语言",
      "created_time": "注册时间"
    }
  }
}
```

