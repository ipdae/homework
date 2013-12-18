(global-linum-mode 1)
(setq-default tab-width 4)

(iswitchb-mode t)

(require'hangul)
(set-input-method "korean-hangul1390") ;; for 3 beolsik 390...
;; (set-unput-method "korean-hangul13f") ;; if you want 3 beolsik final...
(setq load-path (cons (expand-file-name "~/.emacs.d/") load-path))
(set-language-environment "UTF-8")
(set-terminal-coding-system 'utf-8)
(setq default-process-coding-system '(utf-8 . utf-8))
(prefer-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
