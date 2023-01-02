import streamlit as st
import pandas as pd

st.title("Hello world!")

st.header("Native widgets")
st.subheader("Text, numbers and booleans")
st.write("The sum of 1 + 1 is equal to:", 2)
st.write("Paris is the capital of France:", True)

st.subheader("Markdown")
st.markdown(
    """

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~

> Blockquotes can be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

"""
)

st.subheader("Code")
st.code(
    """
def fib(n):
    if n < 2: 
        return 1
    return fib(n-1) + fib(n-2)
    """,
    language="python",
)

st.subheader("pd.DataFrame")
st.write(
    pd.DataFrame(
        {"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40],},
        index=[1, 2, 3, 4],
    )
)

st.header("Interactive")
x = st.slider("Select value", key="x")

st.write(x, "squared is", x * x)

