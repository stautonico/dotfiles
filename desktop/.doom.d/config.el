;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "Steve Tautonico"
      user-mail-address "stautonico@gmail.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:
;; (setq doom-font (font-spec :family "monospace" :size 12 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "sans" :size 13))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; Change the default font size
(set-face-attribute 'default nil :height 115)

;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

;; Bind for font-lock-mode in org-mode (SPC c t)
(map!
 (:after org
 (:leader
  :desc "Font lock mode"
  "c t" #'font-lock-mode)))

;; Enable visual-line-mode in org-mode
;;(add-hook org-mode-hook 'visual-line-mode)

;; Custom keybindings for helm-spotify-plus
(global-set-key (kbd "C-c s s") 'helm-spotify-plus)  ;; "s" for SEARCH
(global-set-key (kbd "C-c s f") 'helm-spotify-plus-next)
(global-set-key (kbd "C-c s b") 'helm-spotify-plus-previous)
(global-set-key (kbd "C-c s p") 'helm-spotify-plus-play)
(global-set-key (kbd "C-c s o") 'helm-spotify-plus-pause) ;; "o" is next to play and more convient than the default "g"


;; Set the project location (projectile)
(setq projectile-project-search-path '("~/Documents/GitHub/"))

;; Settings for toc-org
(if (require 'toc-org nil t)
    (progn
      (add-hook 'org-mode-hook 'toc-org-mode)

      ;; enable in markdown, too
      ;; (add-hook 'markdown-mode-hook 'toc-org-mode)
      ;; (define-key markdown-mode-map (kbd "\C-c\C-o") 'toc-org-markdown-follow-thing-at-point))
  ;;(warn "toc-org not found"))
))

;; Configure settings for prettier
(setenv "NODE_PATH" "/usr/lib/node_modules")

;; Setup org-superstar
(require 'org-superstar)
(add-hook 'org-mode-hook (lambda () (org-superstar-mode 1)))

(with-eval-after-load 'ox
  (require 'ox-hugo))

; Set the location where org-agenda will look for files
(setq org-agenda-files (directory-files-recursively "/home/steve/Documents/GitHub/school" "\\.org$"))

; Setup and configure mu4e
(require 'mu4e)

;; Use mu4e as our email client
(setq mail-user-agent 'mu4e-user-agent)

(setq mu4e-drafts-folder "/[Gmail].Drafts")
(setq mu4e-sent-folder   "/[Gmail].Sent Mail")
(setq mu4e-trash-folder  "/[Gmail].Trash")

;; don't save message to Sent Messages, Gmail/IMAP takes care of this
(setq mu4e-sent-messages-behavior 'delete)

;; setup some handy shortcuts
;; you can quickly switch to your Inbox -- press ``ji''
;; then, when you want archive some messages, move them to
;; the 'All Mail' folder by pressing ``ma''.

(setq mu4e-maildir-shortcuts
    '( (:maildir "/INBOX"              :key ?i)
       (:maildir "/[Gmail].Sent Mail"  :key ?s)
       (:maildir "/[Gmail].Trash"      :key ?t)
       (:maildir "/[Gmail].All Mail"   :key ?a)))

;; allow for updating mail using 'U' in the main view:
(setq mu4e-get-mail-command "offlineimap")

;; something about ourselves
;; (setq
;;   mu4e-compose-signature
;;    (concat
;;      "Foo X. Bar\n"
;;      "http://www.example.com\n"))

;; Tell mu4e which emails are mine
(setq mu4e-user-mail-address-list '("stautonico@gmail.com"
                                    "steven.tautonico@mail.citytech.cuny.edu"))

(require 'smtpmail)
(setq message-send-mail-function 'smtpmail-send-it
   starttls-use-gnutls t
   smtpmail-starttls-credentials '(("smtp.gmail.com" 587 nil nil))
   smtpmail-auth-credentials
     '(("smtp.gmail.com" 587 "stautonico@gmail.com" nil))
   smtpmail-default-smtp-server "smtp.gmail.com"
   smtpmail-smtp-server "smtp.gmail.com"
   smtpmail-smtp-service 587)

;; don't keep message buffers around
(setq message-kill-buffer-on-exit t)

;; Disable the loud notifications
(setq mu4e-alert-style nil
      +mu4e-alert-bell-cmd nil)

;; Configure org-roam
(use-package org-roam
  :ensure t
  :init
  (setq org-roam-v2-ack t)
  :custom
  (org-roam-directory "~/Documents/GitHub/dotslashsteve.sh/notes/content-org")
  (org-roam-complete-everywhere t)
  :bind (("C-c n l" . org-roam-buffer-toggle)
         ("C-c n f" . org-roam-node-find)
         ("C-c n i" . org-roam-node-insert)
         :map org-mode-map
         ("C-M-i" . completion-at-point))
  :config
  (org-roam-setup))

;; File paths for org-roam files
;; I unfortunately need to manually add a new template for each subdir
(setq org-roam-capture-templates
      '(
        ("d" "default" plain "%?"
         :target (file+head "${slug}.org"
                            "#+title: ${title}\n") :unnarrowed t)
        ("l" "linux" plain "%?"
         :target (file+head "linux/${slug}.org"
                            "#+title: ${title}\n") :unnarrowed t)
        ("css" "css" plain "%?"
         :target (file+head "css/${slug}.org"
                            "#+title: ${title}\n") :unnarrowed t)
        )
      )

;; Allow use of BIND export setting in org-mode
(setq org-export-allow-bind-keywords t)
