"Vlad Solokha vim config

" adapted from 
"https://stevelosh.com/blog/2010/09/coming-home-to-vim/#using-the-leader
"remove all compatibility to improve functionality
set nocompatible 

" security exploits with modlines in files
set modelines=0

set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab

set encoding=utf-8
set scrolloff=3
set autoindent
set showmode
set showcmd
set hidden
set wildmenu
set wildmode=list:longest
set visualbell
set cursorline
set ttyfast
set ruler
set backspace=indent,eol,start
set laststatus=2
" display how far away eachline is from the current one
set relativenumber
" save undos to the current file even after close and reopen
set undofile

" esc in insert and visual mode
inoremap kj <esc>
vnoremap kj <esc>

" esc in command mode
cnoremap kj <C-C>
" <C-C> means Ctrl-C

" MAP LEADER \ to ,
let mapleader = ","

" ,W strip all trailing whitespace in current file
nnoremap <leader>W :%s/\s\+$//<cr>:let @/=''<CR>

" ,v reselect the text that was just pasted 
nnoremap <leader>v V`

" Tame searching/moving
set ignorecase
set smartcase
set gdefault " apply substitutions globally on lines
set incsearch
set showmatch
set hlsearch
nnoremap <leader><space> :noh<cr> "clear out search by typing ,<space>
" make tab the movement to move around bracket pairs
nnoremap <tab> %
vnoremap <tab> %

set textwidth=79
set formatoptions=qrn1
set colorcolumn=85

" Disable arrow keys for movement
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>
nnoremap j gj
nnoremap k gk

" sometimes you miss the ESC key? 
inoremap <F1> <ESC>
nnoremap <F1> <ESC>
vnoremap <F1> <ESC>

" ,w opens new vertical split and switches over to it
nnoremap <leader>w <C-w>v<C-w>l

" <C-<movement-key>> moves around your splits
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

