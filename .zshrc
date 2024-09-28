# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/data/wxd/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/data/wxd/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/data/wxd/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/data/wxd/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

PROMPT='%n@%m:%~$ '
export GOOGLE_APPLICATION_CREDENTIALS="/data/wxd/dataset_Auto-UI/apt-impact-427407-q4-c3c015728f0b.json"


# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/wxd/google-cloud-sdk/path.zsh.inc' ]; then . '/home/wxd/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/wxd/google-cloud-sdk/completion.zsh.inc' ]; then . '/home/wxd/google-cloud-sdk/completion.zsh.inc'; fi
#!/bin/bash
export PATH=/usr/local/cuda-12.5/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.5/lib64:$LD_LIBRARY_PATH

# 继续执行脚本中的其他命令
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
export ANDROID_SDK_ROOT=/data/wxd/android_sdk
export PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
export ANDROID_AVD_HOME=$ANDROID_SDK_ROOT/avd
export LD_LIBRARY_PATH=/data/wxd/android_sdk/emulator/lib64:/data/wxd/android_sdk/emulator/lib64/qt/lib:$LD_LIBRARY_PATH
export ANDROID_STUDIO_HOME=/data/wxd/android_sdk/android-studio
export PATH=$PATH:$ANDROID_STUDIO_HOME/bin
export https_proxy=http://127.0.0.1:7890
