" General
set number			" Show line numbers
set linebreak			" Break lines at word (requires Wrap lines)
"set showbreak=↪\   		" Wrap-broken line prefix
set showbreak==>\ 
set textwidth=100		" Line wrap (number of cols)
set showmatch			" Highlight matching brace
set visualbell			" Use visual bell (no beeping)

set hlsearch			" Highlight all search results
set smartcase			" Enable smart-case search
set ignorecase			" Always case-insensitive
set incsearch			" Searches for strings incrementally

set autoindent			" Auto-indent new lines
set shiftwidth=4		" Number of auto-indent spaces
set smartindent			" Enable smart-indent
set smarttab			" Enable smart-tabs
set softtabstop=4		" Number of spaces per Tab

set t_Co=256
colorscheme steve

" Advanced
set ruler			" Show row and column ruler information

set undolevels=1000		" Number of undo levels
set backspace=indent,eol,start	" Backspace behaviour
set encoding=utf-8

" Neovide settings
let g:neovide_refresh_rate=140
let g:neovide_transparency=0.95

" Aliases
function! IDE(...)
    if a:0 > 0
	let l:path = a:1
    else
	let l:path = getcwd()
    endif
    execute "NERDTree" l:path
    execute "bo 10sp | term"
endfunction

command! -nargs=? -complete=file IDE call IDE(<f-args>)

" Load plugins
call plug#begin()
  Plug 'preservim/nerdtree'	    " Tree explorer
  Plug 'vim-airline/vim-airline'    " Custom status bar
  Plug 'mboughaba/i3config.vim'     " Syntax highlighting for i3 config files
call plug#end()

