// Editorial review-draft styling for Quarto's Typst output.
// Text and citations stay in index.qmd; this file controls only presentation.

#let ink = rgb("#121417")
#let charcoal = rgb("#252b31")
#let navy = rgb("#16324b")
#let accent = rgb("#ad342d")
#let muted = rgb("#5f6872")
#let rule = rgb("#d7dde2")
#let soft-rule = rgb("#e8edf1")
#let panel = rgb("#f8fafb")
#let panel-strong = rgb("#f1f5f7")
#let table-head = rgb("#eaf0f5")
#let code-paper = rgb("#eef4f6")

#set text(font: "Libertinus Serif", size: 10.15pt, fill: ink)
#set par(justify: true, leading: 0.62em, first-line-indent: 0em)
#set page(
  numbering: "1",
  header: context {
    if counter(page).get().first() > 1 {
      block(width: 100%, below: 5pt)[
        #text(font: "Helvetica Neue", size: 7.1pt, fill: muted)[A History of Modern Multi-Agent LLM Systems]
        #v(2pt)
        #line(length: 100%, stroke: 0.35pt + soft-rule)
      ]
    } else {
      none
    }
  },
  footer: context [
    #align(center, text(font: "Helvetica Neue", size: 7.8pt, fill: muted)[#counter(page).display()])
  ],
)

// Override Quarto's generic article title block with a compact editorial deck.
#let article(
  title: none,
  subtitle: none,
  authors: none,
  date: none,
  abstract: none,
  abstract-title: none,
  cols: 1,
  lang: "en",
  region: "US",
  font: "libertinus serif",
  fontsize: 11pt,
  title-size: 1.5em,
  subtitle-size: 1.25em,
  heading-family: "libertinus serif",
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  sectionnumbering: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  mathfont: none,
  codefont: none,
  keywords: none,
  doc,
) = {
  set par(justify: true, leading: 0.62em, first-line-indent: 0em)
  set text(lang: lang, region: region, font: font, size: fontsize, fill: ink)
  set heading(numbering: sectionnumbering)

  if title != none {
    block(below: 0.18in)[
      #line(length: 100%, stroke: 1.4pt + accent)
      #v(0.18in)
      #block(width: 91%)[
        #set par(justify: false, leading: 0.72em)
        #text(font: "Helvetica Neue", weight: "bold", size: 24pt, fill: ink)[#title]
        #if subtitle != none {
          parbreak()
          text(font: "Helvetica Neue", size: 13.4pt, fill: muted)[#subtitle]
        }
      ]
      #v(0.18in)
      #if authors != none {
        let count = authors.len()
        let ncols = calc.min(count, 3)
        grid(
          columns: (1fr,) * ncols,
          row-gutter: 0.5em,
          ..authors.map(author =>
            align(left)[
              #text(font: "Helvetica Neue", size: 8.7pt, weight: "bold", fill: charcoal)[#author.name]
              #if not empty(author.affiliation) {
                linebreak()
                text(font: "Helvetica Neue", size: 8pt, fill: muted)[#author.affiliation]
              }
              #if not empty(author.email) {
                linebreak()
                text(font: "Helvetica Neue", size: 8pt, fill: muted)[#author.email]
              }
            ]
          )
        )
      }
      #if date != none {
        v(0.07in)
        text(font: "Helvetica Neue", size: 7.7pt, fill: muted)[#date]
      }
    ]
  }

  if abstract != none {
    block(
      width: 100%,
      above: 0.05in,
      below: 0.22in,
      inset: (x: 12pt, y: 9pt),
      fill: panel,
      stroke: (left: 2.2pt + navy),
      radius: 2pt,
    )[
      #set par(justify: true, leading: 0.56em, first-line-indent: 0em)
      #text(font: "Helvetica Neue", size: 7.8pt, weight: "bold", fill: navy)[#abstract-title]
      #h(0.7em)
      #text(size: 9.15pt)[#abstract]
    ]
  }

  if toc {
    let title = if toc_title == none { auto } else { toc_title }
    block(above: 0em, below: 2em)[
      #outline(title: title, depth: toc_depth, indent: toc_indent);
    ]
  }

  if cols == 1 {
    doc
  } else {
    columns(cols, doc)
  }
}

#show heading.where(level: 1): set block(
  above: 1.45em,
  below: 0.50em,
  inset: (top: 0.36em),
  stroke: (top: 0.45pt + rule),
)
#show heading.where(level: 2): set block(above: 1.05em, below: 0.42em)
#show heading.where(level: 3): set block(above: 0.85em, below: 0.32em)
#show heading.where(level: 1): set text(font: "Helvetica Neue", size: 15.8pt, weight: "bold", fill: navy)
#show heading.where(level: 2): set text(font: "Helvetica Neue", size: 12.2pt, weight: "bold", fill: navy)
#show heading.where(level: 3): set text(font: "Helvetica Neue", size: 10.5pt, weight: "bold", fill: charcoal)

#show figure.caption: set text(font: "Helvetica Neue", size: 7.8pt, fill: rgb("#34404a"))
#show figure.caption: set block(above: 0.42em, below: 0.05em)
#show figure: it => block(
  width: 100%,
  above: 1.02em,
  below: 1.22em,
  inset: (x: 6pt, y: 7pt),
  fill: rgb("#fcfdfe"),
  stroke: 0.35pt + soft-rule,
  radius: 2pt,
)[#it]

#show raw: set text(font: "Menlo", size: 8.1pt, fill: rgb("#0d4058"))
#show raw.where(block: true): set block(
  above: 0.7em,
  below: 0.85em,
  inset: 7pt,
  radius: 2pt,
  fill: code-paper,
  stroke: (left: 1.2pt + rgb("#b9cbd7")),
)
#show link: set text(fill: rgb("#11617f"))
#show strong: set text(weight: "bold")

#set table(
  inset: (x: 7pt, y: 5pt),
  fill: (x, y) => if y == 0 { table-head } else { none },
  stroke: (x, y) => if y == 0 {
    (bottom: 0.8pt + navy)
  } else {
    (bottom: 0.35pt + soft-rule)
  },
)
#show table: it => block(
  width: 100%,
  above: 1.02em,
  below: 1.12em,
  stroke: (top: 0.45pt + navy, bottom: 0.45pt + soft-rule),
)[
  #set par(justify: false, leading: 0.50em)
  #set text(size: 9.05pt)
  #it
]
#show table.cell.where(y: 0): set text(font: "Helvetica Neue", size: 8.45pt, weight: "bold", fill: navy)

#show quote.where(block: true): it => block(
  inset: (left: 12pt, right: 10pt, top: 7pt, bottom: 7pt),
  stroke: (left: 2.4pt + accent),
  fill: panel,
  radius: 2pt,
  above: 0.75em,
  below: 0.75em,
)[
  #set text(size: 9.75pt, fill: charcoal)
  #it.body
]

#let keypoints(body) = block(
  width: 100%,
  breakable: true,
  inset: (x: 13pt, y: 11pt),
  fill: panel-strong,
  stroke: (left: 3pt + accent),
  radius: 2pt,
  above: 0.55em,
  below: 1.05em,
)[
  #set text(size: 9.15pt)
  #set par(justify: false, leading: 0.52em, first-line-indent: 0em)
  #show heading.where(level: 1): set block(above: 0pt, below: 0.42em, stroke: none, inset: 0pt)
  #show heading.where(level: 1): set text(font: "Helvetica Neue", size: 12.5pt, weight: "bold", fill: navy)
  #show heading.where(level: 2): set block(above: 0pt, below: 0.42em, stroke: none, inset: 0pt)
  #show heading.where(level: 2): set text(font: "Helvetica Neue", size: 12.5pt, weight: "bold", fill: navy)
  #show list: set block(above: 0em, below: 0em)
  #body
]

#let reviewbox(body) = block(
  width: 100%,
  breakable: true,
  inset: (x: 12pt, y: 10pt),
  fill: panel,
  stroke: (left: 2.6pt + navy),
  radius: 2pt,
  above: 0.9em,
  below: 0.95em,
)[
  #set text(size: 9.1pt)
  #set par(justify: false, leading: 0.51em, first-line-indent: 0em)
  #show list: set block(above: 0.15em, below: 0em)
  #body
]
