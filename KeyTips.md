You should add system version and app version to compose function step description, because among various versions, gui operations often differs
Automator 文件夹操作 shell脚本 ;bash /Users/water2cloud/procVolumes.sh; 选中某文件，右键点击服务，选择文件夹操作
ps aux | awk 'NR==1 || /qemu/'

模拟器网络设置（port为代理转发接口），官方网站https://developer.android.com/studio/run/emulator-networking?hl=zh-cn ：
10.0.2.2:port
# 查看 HTTP 代理
networksetup -getwebproxy Wi-Fi
# 查看 HTTPS 代理
networksetup -getsecurewebproxy Wi-Fi
# 查看 SOCKS 代理
networksetup -getsocksfirewallproxy Wi-Fi
如果你使用的是其他网络接口（如有线网络），可以替换 Wi-Fi 为 Ethernet 或其他接口名称。


emulator -avd blabla -no-snapshot-load -http-proxy 127.0.0.1:7890(代理好像不起作用)
Ubuntu 服务器运行：系统不支持为包含 Vulkan 图形库的模拟器创建快照。如需在不使用 Vulkan 的情况下运行模拟器，请通过命令行启动模拟器，并使用标志 -feature -Vulkan。
针对allow debugging和authorized状态不能保存问题：在模拟器中确认权限，删除~/.android/adbkey adbkey.pub，revoke authority必须但顺序不确定，运行 adb kill-server(会重新创建adbkey adbkey.pub)， adb start-server（重新创建adbkey & adbkey.pub）。关闭模拟器后，重新使用cmdline命令启动,应该就不会再弹出allow debugging窗口。  

llmatouch_dataset_0521:处理后形成的基准数据集。
dataset:将某种手动录制的序列作为输入，对数据集进行后处理从而形成llmatouch_dataset_0521的一系列程序
Evaluator:访问llmatouch_dataset_0521的主要封装函数，对比groundtruth和collected traces from AgentEnv
AgentEnv: agent运行的环境，用于交互和collect traces.
agent_exec_traces: AutoUI在AgentEnv运行形成的traces，以及人工标准是否成功的基准。

只设置export https_proxy=http://127.0.0.1:7890（不设置http_proxy）
curl -v https://www.google.com


export AGENTENV_PATH='/data/wxd/LlamaTouch/AgentEnv'
export FIRST_N_EPISODES=2
export OPENAI_APIKEY='sk-lNSaW2EZ2kkc0Bw1Db9645248e98434693410e0656F93c2d'
export OPENAI_BASEURL='https://aigc.x-see.cn/v1/'
python3 main_exec_testbed3.py

environment.py  AgentEnv setup()中self.emulator_controller.load_emulator_with_snapshot()取消，改为提前启动模拟器
emulator -avd pixel_6a_api31 -no-snapshot-save -feature -Vulkan