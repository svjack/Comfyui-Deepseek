from .deepseek import DeepseekNode, DeepseekAdvancedNode, DeepseekReasonerNode
from .silicon_deepseek import SiliconDeepseekChat, SiliconDeepseekReasoner

# 在模块级别定义这些映射
NODE_CLASS_MAPPINGS = {
    "DeepseekNode": DeepseekNode,
    "DeepseekAdvancedNode": DeepseekAdvancedNode,
    "DeepseekReasonerNode": DeepseekReasonerNode,
    "SiliconDeepseekChat": SiliconDeepseekChat,
    "SiliconDeepseekReasoner": SiliconDeepseekReasoner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepseekNode": "Deepseek Chat",
    "DeepseekAdvancedNode": "Deepseek Chat Advanced",
    "DeepseekReasonerNode": "Deepseek Reasoner",
    "SiliconDeepseekChat": "Silicon Deepseek Chat",
    "SiliconDeepseekReasoner": "Silicon Deepseek Reasoner"
}

# 确保这些变量可以被ComfyUI导入
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 
