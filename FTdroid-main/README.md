# FTdroid
FTdroid

step 0: input
step 1: abstractor
    输入-另外几（4）个原用例(迁移前的ground truth)的自然语言描述；输出-该场景的综合的描述
step 2: generator-matching
    以该场景的综合描述和steps2_txt_prompt（迁移后的Reference test case）为输入，产生specific_steps_text输出（每一个汇总步骤中映射的Reference test case步骤），而result_steps_text是从specific_steps_text的映射步骤中选取出现次数最多的共同描述。
step 3: generator-completion，用result_steps_text引导生成过程
validation 是在每个step 都有写


FTdroid 消融实验：？
直接使用迁移前的任意一个用例描述做Generator-completion
直接使用迁移后的任意一个用例描述做Generator-completion
最终事件描述中，Step-i是在固定位置i的最高可能事件，但实际中事件位置和顺序可能调整，没有充分考虑事件的前后依存关系

下两周：构建形成操作步骤知识库（基本完成），基于Top1直接在llamaIndex数据集上引导大模型做生成，看看效果如何（软件学报或计算机学报）。

利用大模型将知识库进行操作标准化（难点）。针对某一个功能描述，利用语义相关性提取知识库中的相似操作，基于相似操作构建基于概率的标准化操作状态转换图。Generator-completion方式由大模型探索，每次操作时从转换图中匹配标准化操作，将标准化操作对应的下一步以及对应概率扔给大模型做探索。

针对特定app，进行在线探索的过程中构建该app的领域知识（类似AutoDroid）用于增强上述方法。

python start.py -o outtmp -is_emulator