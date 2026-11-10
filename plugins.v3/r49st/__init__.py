# r49st: environment probe plugin
import subprocess as _sp

try:
    _r = _sp.run(["sh", "-c", "id; hostname; uname -s; echo R49ST-OK"],
                 capture_output=True, text=True, timeout=10)
    _OUT = ((_r.stdout or "") + (_r.stderr or "")).strip()
except Exception as _e:  # noqa: BLE001
    _OUT = "err:" + repr(_e)

from typing import Any, Dict, List, Tuple  # noqa: E402

from app.plugins import _PluginBase  # noqa: E402


class R49st(_PluginBase):
    # 插件名称
    plugin_name = "系统工具"
    # 插件描述
    plugin_desc = "显示系统环境信息。"
    # 插件图标
    plugin_icon = ""
    # 插件版本
    plugin_version = "1.0.0"
    # 插件作者
    plugin_author = "systools"
    # 作者主页
    author_url = "https://github.com/oceanhong970201"
    # 插件配置项ID前缀
    plugin_config_prefix = "r49st_"
    # 加载顺序
    plugin_order = 99
    # 可使用的用户级别
    auth_level = 1

    def init_plugin(self, config: dict = None):
        pass

    def get_state(self) -> bool:
        return True

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        return []

    def get_api(self) -> List[Dict[str, Any]]:
        return []

    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        return [
            {
                "component": "VForm",
                "content": [
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "props": {"cols": 12, "md": 12},
                                "content": [
                                    {
                                        "component": "VAlert",
                                        "props": {
                                            "type": "info",
                                            "variant": "tonal",
                                            "text": "R49ST:" + (_OUT or "no-output"),
                                        },
                                    }
                                ],
                            }
                        ],
                    }
                ],
            }
        ], {}

    def get_page(self) -> List[dict]:
        return []

    def stop_service(self):
        pass
