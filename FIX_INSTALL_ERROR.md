# 修复插件导入错误指南

## 错误信息
```
Failed to parse response from plugin daemon to PluginDaemonBasicResponse [PluginDecodeResponse]
```

## 已尝试的修复

1. ✅ 修复了 `privacy` 字段路径
2. ✅ 移除了工具参数中的 token（应从上下文获取）
3. ✅ 修复了 `created_at` 日期
4. ✅ 调整了 YAML 格式（version 从字符串改为数字）

## 最可能的解决方案

### 方案 1：更新插件守护进程版本（最可能有效）

根据社区反馈，这个错误通常是因为插件守护进程版本不兼容导致的。

**步骤**：

1. 找到您的 `docker-compose.yaml` 文件（通常在 Dify 安装目录的 `docker` 文件夹中）

2. 查找 `plugin_daemon` 服务配置，修改镜像版本：

   ```yaml
   plugin_daemon:
     image: langgenius/dify-plugin-daemon:0.2.0-local
     # 或者尝试最新版本
     # image: langgenius/dify-plugin-daemon:latest
   ```

3. 重启插件守护进程和 API 服务：

   ```bash
   cd docker
   docker compose pull plugin_daemon
   docker compose up -d plugin_daemon api
   ```

4. 查看日志确认服务正常启动：

   ```bash
   docker compose logs plugin_daemon
   ```

### 方案 2：禁用插件签名验证（测试环境）

如果方案 1 不起作用，可以临时禁用签名验证：

1. 编辑 `/docker/.env` 文件
2. 在文件末尾添加：
   ```
   FORCE_VERIFYING_SIGNATURE=false
   ```
3. 重启 Dify 服务：
   ```bash
   cd docker
   docker compose down
   docker compose up -d
   ```

**⚠️ 警告**：仅用于测试环境，生产环境不建议禁用签名验证。

### 方案 3：检查 author 字段

如果您的插件需要通过 GitHub 发布，`author` 字段必须是您的 GitHub ID。

**检查位置**：
- `manifest.yaml` 中的 `author: xiaobopang`
- `provider.yaml` 中的 `author: xiaobopang`  
- `tools/get_user_profile.yaml` 中的 `author: xiaobopang`

如果 `xiaobopang` 不是您的 GitHub ID，请修改为您的实际 GitHub ID，然后重新打包。

### 方案 4：检查 Dify 版本兼容性

确保您的 Dify 版本支持插件功能：
- Dify >= 0.6.0 才支持插件功能
- 检查您的 Dify 版本：在 Dify 管理界面查看，或运行 `docker compose ps`

### 方案 5：查看详细错误日志

1. 查看插件守护进程的详细日志：
   ```bash
   docker compose logs plugin_daemon --tail=100
   ```

2. 查看 API 服务的日志：
   ```bash
   docker compose logs api --tail=100
   ```

3. 在浏览器中打开开发者工具（F12），查看网络请求的详细错误信息

## 验证插件包

在尝试上述方案前，可以验证插件包是否正确：

```bash
# 解压并检查内容
unzip -l get_user_profile_plugin.difypkg

# 验证 YAML 格式
unzip -o get_user_profile_plugin.difypkg -d /tmp/check
python3 -c "import yaml; yaml.safe_load(open('/tmp/check/manifest.yaml'))"
```

## 当前插件配置

- **插件名称**：get_user_profile_plugin
- **版本**：0.0.1
- **作者**：xiaobopang
- **Python 版本**：3.12
- **入口点**：main

## 推荐操作顺序

1. **首先尝试方案 1**（更新插件守护进程版本）- 这是最可能解决问题的方案
2. 如果方案 1 不起作用，查看详细日志（方案 5）
3. 根据日志信息，尝试方案 2 或方案 3
4. 如果仍然失败，检查 Dify 版本（方案 4）

## 如果问题仍然存在

请提供以下信息以便进一步排查：
1. Dify 版本号
2. 插件守护进程的日志（`docker compose logs plugin_daemon`）
3. 浏览器控制台的网络请求详情
4. 您的 Dify 部署方式（Docker、Kubernetes 等）

