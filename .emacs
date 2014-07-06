(global-linum-mode 1)
(setq-default tab-width 4)

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
(setq flymake-python-pyflakes-extra-arugments '("--ignore=W806"))
