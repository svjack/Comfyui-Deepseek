from .deepseek import DeepseekNode
from .deepseek import DeepseekAdvancedNode

# 在模块级别定义这些映射
NODE_CLASS_MAPPINGS = {
    "DeepseekNode": DeepseekNode,
    "DeepseekAdvancedNode": DeepseekAdvancedNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepseekNode": "Deepseek Chat",
    "DeepseekAdvancedNode": "Deepseek Chat Advanced"
}

# 确保这些变量可以被ComfyUI导入
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 