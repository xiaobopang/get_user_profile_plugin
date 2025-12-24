#!/bin/bash
# 打包工具插件为 .pkg 文件

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

PLUGIN_NAME="get_user_profile_plugin"
OUTPUT_FILE="${PLUGIN_NAME}.difypkg"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

echo "正在打包插件: $PLUGIN_NAME"
echo "当前目录: $SCRIPT_DIR"
echo "输出文件: $OUTPUT_FILE"

# 创建临时目录
TEMP_DIR=$(mktemp -d)
echo "临时目录: $TEMP_DIR"

# 复制文件到临时目录（直接放在根目录，不嵌套）
# Dify 插件包要求文件直接在根目录，而不是嵌套在子目录中
cp manifest.yaml provider.yaml main.py requirements.txt privacy.md "$TEMP_DIR/" 2>/dev/null || true
# 将工具文件复制到根目录（根据 provider.yaml 中的配置）
cp tools/get_user_profile.yaml "$TEMP_DIR/get_user_profile.yaml" 2>/dev/null || true
# 将 icon 文件复制到根目录（不包含 _assets 目录）
cp icon.svg "$TEMP_DIR/icon.svg" 2>/dev/null || true

cd "$TEMP_DIR"

# 打包为 zip 文件（Dify 使用 .difypkg 扩展名，但实际上是 zip 格式）
# 文件直接在根目录，不包含父目录
zip -r "$OUTPUT_FILE" . -x "*.git*" -x "*.DS_Store" -x "*__pycache__*" -x "*.pkg" -x "*.difypkg" -x "README.md" -x "INSTALL.md" -x "package.sh"

# 移动回父目录（agent 目录）
mv "$OUTPUT_FILE" "$PARENT_DIR"
cd "$SCRIPT_DIR"

# 清理临时目录
rm -rf "$TEMP_DIR"

echo ""
echo "✅ 打包完成!"
echo "📦 插件文件: $PARENT_DIR/$OUTPUT_FILE"
echo ""
echo "下一步："
echo "1. 在 Dify 管理界面中安装此插件"
echo "2. 在 Agent 应用中启用 'get_user_profile' 工具"

