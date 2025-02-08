---
title: Title of Post
#date: yyyy-mm-ddThh:mm:ss+13:00
draft: true

---

Text

{{< figure src="images/image2.jpeg" caption="A nice flower caption 1." class="center" alt="Flower 1" >}}

Text

# How to setup and keep producing podcasts
<p>The main purpose of this article is to make sure that all basic HTML Elements are decorated with CSS so as to not miss any possible elements when creating new themes for Hugo.
<!--more-->

# Headings

Let's start with all possible headings. The HTML `<h1>`—`<h6>` elements represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

***

# Paragraph

According to the [HTML5 specification](https://www.w3.org/TR/html5/dom.html#elements) by [W3C](https://www.w3.org/), **HTML documents consist of a tree of elements and text**. Each element is denoted in the source by a [start tag](https://www.w3.org/TR/html5/syntax.html#syntax-start-tags), such as `<body>`, and an [end tag](https://www.w3.org/TR/html5/syntax.html#syntax-end-tags), such as `</body>`. (*Certain start tags and end tags can in certain cases be omitted and are implied by other tags.*)

Elements can have attributes, which control how the elements work. For example, hyperlink are formed using the `a` element and its `href` attribute.

# List Types

## Ordered List

1. First item
	* subitem for Item 1
		* subitem for Item 1
2. Second item
	* subitem for Item 2
		* subitem for Item 2
3. Third item
	* subitem for Item 3
		* subitem for Item 3

## Unordered List

* List item
* Another item
* And another item

## Nested list
* First item - alright!
* Second item
    * Second item First subitem
    * Second item second subitem
        * Second item Second subitem First sub-subitem
        * Second item Second subitem Second sub-subitem
        * Second item Second subitem Third sub-subitem
    * Second item Third subitem
        * Second item Third subitem First sub-subitem
        * Second item Third subitem Second sub-subitem
* Third item

## Definition List

HTML also supports definition lists.

Blanco tequila
: The purest form of the blue agave spirit...
Reposado tequila
: Typically aged in wooden barrels for between two and eleven months...

# Code

{{< highlight html >}}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
{{< /highlight >}}

