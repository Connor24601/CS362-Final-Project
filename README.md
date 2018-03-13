# CS362-Final-Project
A brief tetranucleotide frequency comparison program. Our code tries to determine percentage difference in genomes/a set of contigs based on tetranucleotide frequency. Our numbers are quite likely not actual percentages. What we did is we got the concentrations of each tetranucleotide, divided by the total number of nucleotides, and then summed all the differences in those ratios. This allowed us to return just 1 number instead of 256 tetranucleotides. <br>
<br>  Our code can be run with 2 FASTA files through Python. <br>
<code>
  Python3 tetranucleotideFrequencies.py genome1 genome2
  </code>
<p>
  <br>
Exact sequences can be found on NCBI Genome by searching the first line of the FASTA files included in the repository. 
Some brief results:
  <br>
<br>Staphylococcus aureus vs. Escherichia coli IAI39 : 0.5956
<br>Staphylococcus aureus vs. Escherichia coli O83:H1 str. NRG 857C: 0.5957
<br>Staphylococcus aureus vs. Desulfobacula toluolica Tol2: 0.3925
<br>Escherichia coli IAI39 vs. Escherichia coli O83:H1 str. NRG 857C: 0.0131
<br>Escherichia coli IAI39 vs. Desulfobacula toluolica Tol2: 0.3925
<br>Escherichia coli O83:H1 str. NRG 857C vs. Desulfobacula toluolica Tol2: 0.3949
<br>
<br>
<br>The real phylogenetic relationships (backed up with our data):
</p>
<pre class="tab">
                                              |
<br>                                              |
<br>                            |-------------------------------------|
<br>                            |                                     |
<br>                            |                                     |
<br>                            |                                     |
<br>                            |                                     |
<br>              |-----------------------------|                     |
<br>              |                             |                     |
<br>              |                             |                     |       
<br>     |----------------|                     |                     |
<br>     |                |                     |                     |
<br>     |                |                     |                     |
<br>E. coli IAI39   E. coli 083:H1        D. toluolica            S. aureus
</pre>
