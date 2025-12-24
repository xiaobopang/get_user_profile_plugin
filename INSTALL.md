# 工具插件安装说明

## 方法 1：通过 Dify 界面安装（推荐）

1. **打包插件**：
   ```bash
   cd get_user_profile_plugin
   # 将整个目录打包为 .zip 文件
   zip -r get_user_profile_plugin.pkg .
   ```

2. **在 Dify 中安装插件**：
   - 进入 Dify 管理界面
   - 找到 "插件" 或 "Plugins" 菜单
   - 点击 "安装插件" 或 "Install Plugin"
   - 上传 `get_user_profile_plugin.pkg` 文件
   - 等待安装完成

3. **在 Agent 应用中启用工具**：
   - 编辑你的 Agent 应用
   - 在 "Agent 模式" → "工具" 中添加工具
   - 选择 "get_user_profile" 工具
   - 保存配置

## 方法 2：直接使用工具配置（如果支持）

如果 Dify 支持直接在 YAML 中引用已安装的插件，可以在 Agent 配置中使用：

```yaml
agent_mode:
  tools:
    - tool_name: get_user_profile
      provider_type: plugin
      provider_id: user_profile_provider
```

## Token 传递说明

工具会自动从请求头中获取 Authorization token。调用 Agent 应用时，确保在请求头中包含：

```
Authorization: Bearer <your_token>
```

工具会将这个 token 传递给用户信息接口。

