export TERM="xterm-256color"                      # getting proper colors
export HISTORY_IGNORE="(ls|cd|pwd|exit|sudo reboot|history|cd -|cd ..)"
export EDITOR="nvim"
export VISUAL="emacs"


#Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#   source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/steve/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="agnoster"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(zsh-autosuggestions zsh-syntax-highlighting git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
# [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

ex ()
{
  if [ $# -eq 0 ] ; then
    echo "usage: ex <file>"
  else
    if [ -f $1 ] ; then
        case $1 in
        *.tar.bz2)   tar xjf $1   ;;
        *.tar.gz)    tar xzf $1   ;;
        *.bz2)       bunzip2 $1   ;;
        *.rar)       unrar x $1   ;;
        *.gz)        gunzip $1    ;;
        *.tar)       tar xf $1    ;;
        *.tbz2)      tar xjf $1   ;;
        *.tgz)       tar xzf $1   ;;
        *.zip)       unzip $1     ;;
        *.Z)         uncompress $1;;
        *.7z)        7z x $1      ;;
        *.deb)       ar x $1      ;;
        *.tar.xz)    tar xf $1    ;;
        *.tar.zst)   unzstd $1    ;;
        *)           echo "'$1' cannot be extracted via ex()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
  fi
}

fastfind ()
{
    if [ $# -eq 0 ] ; then
	echo "usage: $0 <filename or pattern>"
    else
	find / -iname "*$1*" 2> /dev/null
    fi
}

alias ff="fastfind"

change-qtile-theme () {
    if ! [ -z "$1" ]; then
    echo "$1" > /home/steve/.config/qtile/theme
	set_theme=$1
    else
	echo "default" > /home/steve/.config/qtile/theme
	set_theme="default"
    fi

    echo "Restart qtile to apply theme: '$set_theme'"

}

# Aliases
alias ls="exa"
alias oldls="/usr/bin/ls"
alias cat="bat"
alias oldcat="/usr/bin/cat"
alias vim="nvim -S ~/.config/nvim/init.vim"
alias oldvim="/usr/bin/vim"
alias hexdump="/usr/bin/hexyl"
alias oldhexdump="/usr/bin/hexdump"

alias math="bc"
alias reboot-bios="sudo systemctl reboot --firmware-setup"
alias neovide="/usr/bin/neovide -S ~/.config/nvim/init.vim"
alias nano="/usr/bin/nano -l"
alias upgrade="sudo pacman -Syyuu && yay -Syyuu --noconfirm"
alias update="sudo pacman -Syyuu && yay -Syyuu --noconfirm"
alias q="exit"
alias startwebcam="screen -S webcam -dm /home/steve/Documents/Scripts/webcam.sh"
alias stopwebcam="screen -X -S webcam quit"
alias image="nomacs"
alias json="/usr/bin/jq . "
alias grep="ripgrep"
alias open="xdg-open"
alias ps="procs"

# Shortcuts to common folders
alias github="cd /home/steve/Documents/GitHub"
alias school="cd /mnt/steven/School/"

export eng="/mnt/steven/School/Fall_2021/ENG2575/"
export econ="/mnt/steven/School/Fall_2021/ECON1101/"

# Force myself to use vim
# alias nano="vim"

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'
alias rmnoconfirm='/usr/bin/rm'

# Common cd locations
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .3="cd ../.."
alias .4="cd ../../.."


alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB

alias neofetch="neofetch --ascii_distro anarchy"

## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'

## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'

alias tb="nc termbin.com 9999"

alias discord="discord-canary"
alias top="bpytop"
alias firefox="/usr/bin/firefox-developer-edition"
alias firefox-regular="/usr/bin/firefox"
alias proxy="/home/steve/.cargo/bin/proxy"

alias updatemirrorlist="sudo reflector --verbose -l 200 -n 20 -p https -p http -c 'United States' --sort rate --save /etc/pacman.d/mirrorlist"

# Note: This is because sometimes META+CTRL+R doesn't restart qtile
alias restart-qtile="qtile cmd-obj -o cmd -f restart"
alias update-qtiledocs="python3 /home/steve/.config/qtile/generate_docs.py"

alias allusers="cut -d: -f1 /etc/passwd"
alias userlist="egrep -E '/bin/bash|/usr/bin/zsh' /etc/passwd | cut -d: -f1"
#alias pacman="sudo pacman --color auto"
alias cleanup="sudo pacman -Rs $(pacman -Qqtd)"

alias monitormic="pacat -r --latency-msec=1 -d alsa_input.usb-Razer_Razer_Nari_Ultimate-00.mono-fallback | pacat -p --latency-msec=1 -d alsa_output.usb-Razer_Razer_Nari_Ultimate-00.mono-fallback"

alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="youtube-dl --extract-audio --audio-format best "
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
alias yta-opus="youtube-dl --extract-audio --audio-format opus "
alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "

alias ytv-best="youtube-dl -f bestvideo+bestaudio "

# Make tilix work
# if [ $TILIX_ID ] || [ $VTE_VERSION ]; then
#         source /etc/profile.d/vte.sh
# fi

# Setup zoxide
# eval "$(zoxide init zsh)"

# Flag autocomplete
autoload -U compinit && compinit

# Shortcuts to common config files
export CONF_QTILE="/home/steve/.config/qtile/"
export CONF_I3="/home/steve/.config/i3/"
export CONF_ZSH="/home/steve/.zshrc"
export CONF_NVIM="/home/steve/.config/nvim/"
export CONF_VIM="/home/steve/.config/nvim/"
export CONF_CSGO="/home/steve/.local/share/Steam/steamapps/common/Counter-Strike Global Offensive"
export CONF_ALACRITTY="/home/steve/.config/alacritty"

export GOPATH=/home/steve/go
export PATH="$PATH:/home/steve/.local/bin:/home/steve/.emacs.d/bin:/home/steve/.cargo/bin"

#startup_commands=(neofetch pfetch)

#size=${#startup_commands[@]}
#index=$(($RANDOM % $size+1))

#{$startup_commands[$index]}

python-colorscript --256 --ignore-distro
