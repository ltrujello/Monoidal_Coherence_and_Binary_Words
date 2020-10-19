# Monoidal_Coherence_and_Binary_Words
Implementation of the category of binary words in Python for its application to Mac Lane's Coherence Theorem for monoidal categories. There are interesting combinatorial and geometric properties of this category, and due to its recursive nature, it can be programmed, making investigation of such properties much easier and efficient.

As an application of the Python module on binary words, I made a simple app that computes and visualizes the three dimensional projections of the first ten associahedrons, or Stasheff Polytopes as they are sometimes called. I imagine this has been done before, but I cannot find anything on the internet past K_6. 

To make this, I used [3d-force-graph](https://github.com/vasturiano/3d-force-graph) and [dat.gui](https://github.com/dataarts/dat.gui).

## The App
[Click here to run the application](https://ltrujello.github.io/Monoidal_Coherence_and_Binary_Words/associahedra_in_3D/).
With the app you can drag and drop the vertices, hover over vertices to obtain their binary word representation, zoom in and out, and rotate the figure itself. 

The app also has four basic options to change the presentation of the figure. 
* **K_n**: Use the slider to select which Associahedron you want to see. You can see K_1 to K_10. K_10 might be laggy but K_1 - K_9 should be fine. Really, I put K_10 in there just for fun. With 4862 vertices and 19448 edges, it is a curious combinatorial nightmare that you aren't going to learn much from seeing. It's just a strange object to witness.

* **Binary Words**: Check this if you want to see the binary words. One way to think about the vertices of the associahedra are as binary words; or more informally, as formal paranthesizations of a product of some number of elements. The binary words are represented as .jpg images of some latex. Note that the binary word option is not available for K_8, K_9, or K_10. To display all these images is too much data for a single browser to handle. However, you can still hover over nodes to view their binary word representations.

* **Arrows**: Check this if you want to see the arrows. Imagining the vertices as the binary words, the edges can be thought of as "shift operations" which make a single change of paranthesization, possibly within some more complicated expression. 

* **Show vertices**: Check this if you want to see the vertices; either the binary words or just the nodes. If this is unchecked, the vertices will be hidden. 

To read more about the associahedra, check out this nice [category cafe post](https://golem.ph.utexas.edu/category/2018/01/more_secrets_of_the_associahed.html). 