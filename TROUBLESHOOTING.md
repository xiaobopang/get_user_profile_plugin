# 插件导入错误排查指南

## 错误信息
```
Failed to parse response from plugin daemon to PluginDaemonBasicResponse [PluginDecodeResponse]
```

## 已修复的问题

1. ✅ **privacy 字段路径**：已从 `"./privacy.md"` 修改为 `"privacy.md"`
2. ✅ **工具参数定义**：移除了 token 参数（应从上下文自动获取）
3. ✅ **YAML 格式验证**：所有 YAML 文件格式已验证正确

## 可能的解决方案

### 方案 1：检查 author 字段（如果使用 GitHub 发布）

如果您的插件需要通过 GitHub 发布，`author` 字段必须是您的 GitHub ID。

**检查位置**：
- `manifest.yaml` 中的 `author: xiaobopang`
- `provider.yaml` 中的 `author: xiaobopang`
- `tools/get_user_profile.yaml` 中的 `author: xiaobopang`

如果 `xiaobopang` 不是您的 GitHub ID，请修改为您的实际 GitHub ID。

### 方案 2：禁用插件签名验证（仅用于测试环境）

如果插件签名验证导致问题，可以在测试环境中临时禁用：

1. 编辑 Dify 的 `/docker/.env` 文件
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

**⚠️ 警告**：禁用签名验证会带来安全风险，仅建议在测试环境中使用。

### 方案 3：检查插件守护进程

1. 检查插件守护进程是否正常运行
2. 查看 Dify 日志，查找插件守护进程相关的错误信息
3. 如果守护进程异常，尝试重启 Dify 服务

### 方案 4：验证插件包结构

确保插件包包含以下文件（都在根目录）：
- ✅ `manifest.yaml`
- ✅ `provider.yaml`
- ✅ `main.py`
- ✅ `requirements.txt`
- ✅ `privacy.md`
- ✅ `get_user_profile.yaml`

### 方案 5：检查 Dify 版本兼容性

确保您的 Dify 版本支持 Python 插件。检查：
- Dify 版本是否 >= 0.6.0（支持插件功能）
- Python 版本是否匹配（插件要求 Python 3.12）

## 验证步骤

1. **验证插件包内容**：
   ```bash
   unzip -l get_user_profile_plugin.difypkg
   ```

2. **验证 YAML 格式**：
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('manifest.yaml'))"
   ```

3. **检查文件权限**：
   确保所有文件都有读取权限

## 如果问题仍然存在

1. 查看 Dify 的完整错误日志
2. 检查浏览器控制台的网络请求详情
3. 在 Dify GitHub 仓库提交 issue，包含：
   - 错误信息
   - Dify 版本
   - 插件包结构
   - 相关日志

## 当前插件配置摘要

- **插件名称**：get_user_profile_plugin
- **版本**：0.0.1
- **作者**：xiaobopang
- **工具名称**：get_user_profile
- **提供者**：user_profile_provider
- **Python 版本**：3.12
- **入口点**：main.get_user_profile

