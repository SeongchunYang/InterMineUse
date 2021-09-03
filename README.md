# InterMine Usecase


This repository contains the use case of [InterMine](https://github.com/intermine/intermine "InterMine Link"), a registry of various data sources that may prove useful to a variety of researchers in biology.

My primary use was to explore the genes associated with particular pathways of interest, specifically GO terms.

I can certainly go my merry way and manually download all gene lists through portals like [this](http://www.informatics.jax.org/vocab/gene_ontology/GO:0048143 "MGI database").

But after a few requests, I decided to go find out if there are alternatives. And that is what you are seeing here.

Note that InterMine in general is not designed for simply scraping data off of a database, but does so much more.

But this is what I found useful in many of their functions, and I hope it gives you a starting point as it did for me.


## Scripts

Note that due to how GO terms are structured and created, some gene names may overlap between GO term levels. As such, only unique list of gene names are returned.

- <code>query.py</code> allows you to run the job on the command line. The script will ask for a text file of individual GO term names on every line. It will then return the genelist contained in the GO term through the form of a .csv file all of which are saved in a newly created folder <code>GOterms</code> in the current directory. This script can be tested by using the test file provided <code>testTerms.txt</code>.
    - In order to run, use the following line in your terminal; <code> python {your directory}/InterMineUse/query.py</code>.
    - The script will prompt you to provide a .txt file containing the GO terms. Provide the absolute pathname for the file without quotes. An example is like the following; <code>{your directory}/InterMineUse/testTerms.txt</code>.

- <code>query.ipynb</code> allows you to run the job on an ipython notebook. You can run this on jupyter or your IDE of choice. Since everything is configurable on the spot, just input your GO terms as a list of strings and the script will take care of the rest.


## System Requirements

Tested on MacBook Pro 16inch (2019, Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz).

Conda environment .yml is provided directly in the repo. Create an environment in your machine by the following line in the terminal.

<code> conda env create -n environment_name -f environment.yml </code>


## References

[1] A. Kalderimis et al., “InterMine: extensive web services for modern biology,” Nucleic Acids Res, vol. 42, no. W1, pp. W468–W472, Jul. 2014, https://doi.org/10.1093/nar/gku301.

[2] R. N. Smith et al., “InterMine: a flexible data warehouse system for the integration and analysis of heterogeneous biological data,” Bioinformatics, vol. 28, no. 23, pp. 3163–3165, Dec. 2012, https://doi.org/10.1093/bioinformatics/bts577.

