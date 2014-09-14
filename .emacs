(global-linum-mode 1)
(setq-default tab-width 4)
(setq-default indent-tabs-mode nil)

(iswitchb-mode t)


(setq package-archives '(("gnu" . "http://elpa.gnu.org/packages/")
                         ("marmalade" . "http://marmalade-repo.org/packages/")
                         ("melpa" . "http://melpa.milkbox.net/packages/")))

(setq make-backufp-files nil)
(setq auto-save-default nil)

(require 'package)
(add-to-list 'package-archives '("marmalad". "http://marmalade-repo.org/packages/"))
(add-to-list 'package-archives '("melpa". "http://melpa.milkbox.net/packages/"))
(package-initialize)

(require 'flymake-python-pyflakes)
(add-hook 'python-mode-hook 'flymake-python-pyflakes-load)
(setq flymake-python-pyflakes-executable "flake8")
(setq flymake-cursor-mode 't)
(add-hook 'flymake-mode-hook
		  '(lambda ()
			 (local-set-key (kbd "C-c n")
							'flymake-goto-next-error)))
(add-hook 'flymake-mode-hook
		  '(lambda ()
			 (local-set-key (kbd "C-c p")
							'flymake-goto-prev-error)))
(setq flymake-python-pyflakes-extra-arugments '("--ignore=W806"))

(setq inhibit-startup-message t)

(add-to-list 'auto-mode-alist '("\\.html?\\'" . web-mode))
(setq web-mode-markup-indent-offset 2)
(setq web-mode-css-indent-offset 2)
(setq web-mode-code-indent-offset 4)

(setq web-mode-indent-style 1)
(setq web-mode-comment-style 2)

(setq web-mode-engines-alist
      '(("jinja" . "\\.html\\'")))

(require 'pymacs)
(pymacs-load "ropemacs" "rope-")

(setq markdown-command "pandoc")

(setq venv-location "~/.venvs")

(add-hook 'python-mode-hook 'jedi:setup)
(setq jedi:setup-keys t)
(setq jedi:complete-on-dot t)

(load-theme 'solarized-light t)

(set-fontset-font "fontset-default" '(#x1100 . #xffdc) '("나눔바른고딕" . "iso10646-1"))

(setq venv-location "~/.venvs")

(venv-workon "dodo")
