import pprint

message = '''This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/W32TeX) (preloaded format=pdflatex 2019.10.17)  4 NOV 2019 08:58
entering extended mode
 restricted \write18 enabled.
 %&-line parsing enabled.
**StudentOnlineVotingSystemUpdate.tex
(./StudentOnlineVotingSystemUpdate.tex
LaTeX2e <2019-10-01> patch level 1
(c:/texlive/2019/texmf-dist/tex/latex/base/article.cls
Document Class: article 2019/08/27 v1.4j Standard LaTeX document class
(c:/texlive/2019/texmf-dist/tex/latex/base/size12.clo
File: size12.clo 2019/08/27 v1.4j Standard LaTeX file (size option)
)
\c@part=\count80
\c@section=\count81
\c@subsection=\count82
\c@subsubsection=\count83
\c@paragraph=\count84
\c@subparagraph=\count85
\c@figure=\count86
\c@table=\count87
\abovecaptionskip=\skip41
\belowcaptionskip=\skip42
\bibindent=\dimen102
)
(c:/texlive/2019/texmf-dist/tex/latex/ragged2e/ragged2e.sty
Package: ragged2e 2019/07/28 v2.2 ragged2e Package (MS)

(c:/texlive/2019/texmf-dist/tex/latex/ms/everysel.sty
Package: everysel 2011/10/28 v1.2 EverySelectfont Package (MS)
)
\CenteringLeftskip=\skip43
\RaggedLeftLeftskip=\skip44
\RaggedRightLeftskip=\skip45
\CenteringRightskip=\skip46
\RaggedLeftRightskip=\skip47
\RaggedRightRightskip=\skip48
\CenteringParfillskip=\skip49
\RaggedLeftParfillskip=\skip50
\RaggedRightParfillskip=\skip51
\JustifyingParfillskip=\skip52
\CenteringParindent=\skip53
\RaggedLeftParindent=\skip54
\RaggedRightParindent=\skip55
\JustifyingParindent=\skip56
)
(./StudentOnlineVotingSystemUpdate.aux)
\openout1 = `StudentOnlineVotingSystemUpdate.aux'.

LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 9.
LaTeX Font Info:    ... okay on input line 9.
LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 9.
LaTeX Font Info:    ... okay on input line 9.
LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 9.
LaTeX Font Info:    ... okay on input line 9.
LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 9.
LaTeX Font Info:    ... okay on input line 9.
LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 9.
LaTeX Font Info:    ... okay on input line 9.
LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 9.
LaTeX Font Info:    ... okay on input line 9.

ABD: EverySelectfont initializing macros
LaTeX Info: Redefining \selectfont on input line 9.
LaTeX Font Info:    External font `cmex10' loaded for size
(Font)              <14.4> on input line 10.
LaTeX Font Info:    External font `cmex10' loaded for size
(Font)              <7> on input line 10.

Underfull \hbox (badness 10000) in paragraph at lines 12--15

 []

[1

{c:/texlive/2019/texmf-var/fonts/map/pdftex/updmap/pdftex.map}]
(./StudentOnlineVotingSystemUpdate.aux) ) 
Here is how much of TeX's memory you used:
 310 strings out of 492167
 4361 string characters out of 6129158
 66450 words of memory out of 5000000
 4746 multiletter control sequences out of 15000+600000
 6063 words of font info for 22 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 24i,6n,21p,695b,234s stack positions out of 5000i,500n,10000p,200000b,80000s
<c:/texlive/2019/texmf-dist/fonts/type
1/public/amsfonts/cm/cmbx12.pfb><c:/texlive/2019/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr12.pfb><c:/texlive/2019/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr17.pfb>
Output written on StudentOnlineVotingSystemUpdate.pdf (1 page, 37035 bytes).
PDF statistics:
 20 PDF objects out of 1000 (max. 8388607)
 13 compressed objects within 1 object stream
 0 named destinations out of 1000 (max. 500000)
 1 words of extra memory for PDF output out of 10000 (max. 10000000)'''
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1


pprint.pprint(count)
