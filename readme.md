# Debug Helper

* Author: Luke Davis
* Download [stable version][1]
* Download [development version][2]

The purpose of this add-on is to make debugging things in NVDA easier.
New features will be added based on user suggestions. All emails or [GitHub issues](https://github.com/XLTechie/debugHelper) with feedback or feature ideas are most welcome.

## Key command

* NVDA+shift+F1: inserts a mark line in the NVDA log.

## Explanation and Usage

When you press the command key, the add-on inserts a line like the following in the NVDA log (at the Info level):

```
-- mark 1 --
```

It will also announce: "Logged mark 1!"

If you press the key again, you will get:

```
-- Mark 2 --
```

and "Logged mark 2!" will be spoken.

Let us say for example that you were about to perform a series of tasks, that you know generate lengthy error content in the NVDA log. You are going to post the relevant portions of your log to a mailing list or the [NVDA GitHub issue tracker](https://github.com/nvaccess/nvda/issues). However you don't want to hunt through your entire log to find the relevant content. So you use this add-on to insert mark 1, right before you do the thing that causes the first error. If you know something else will generate further errors, or a different kind, you insert another mark to separate that error from the previous one, or so you can say "this is what I was doing at mark 3, where some errors occurred."
Another example: while using some application, something happens that causes an error (maybe you hear the Windows error sound). You want to go back and find that error later, but you don't want to stop working and save the log right now. So you use this add-on again, to insert a mark in your log. This time the mark will appear after the errors in your log, instead of before. But either way, the marks will help you narrow down the important sections of your log.

The mark lines shown above can be easily searched for with the find command in a text editor such as Notepad or Notepad++.
Additionally, by default, there is a blank line inserted above each mark. Blank lines are also possible after the mark. Blank lines can be helpful if you are using NVDA's log viewer, or another text editor, and want to use the arrow keys to quickly read up/down through the log, to find a particular mark. It is easy to pick the word "blank" out of a bunch of text being spoken as you quickly move through the log. If you arrow really fast, you might need more than one blank line, which you can adjust in settings.

Note: the mark count will survive the reloading of plugins (NVDA+control+F3), but will start back at one if you restart NVDA.

## Configuration:

In the Settings section of NVDA Preferences, you will find a "Debug Helper" category. In the settings dialog you can change the number of blank lines inserted before and after each mark line. The default is one line before, and zero after, although you can use zero through 10 lines for either.
Under the Tools category of NVDA's Input Gestures panel, you can change NVDA+shift+F1 to a key sequence of your choice.

## Change log

### Version 1.0 (2019-08-22)

* Initial release.
