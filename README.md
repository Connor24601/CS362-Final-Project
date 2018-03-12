# CS362-Final-Project
a brief tetranucleotide frequency comparison program

Exact sequences can be found on NCBI Genome by searching the first line of the FASTA files included in the repository. 
Some brief results:
Staphylococcus aureus vs. Escherichia coli IAI39 : 0.5956
Staphylococcus aureus vs. Escherichia coli O83:H1 str. NRG 857C: 0.5957
Staphylococcus aureus vs. Desulfobacula toluolica Tol2: 0.3925
Escherichia coli IAI39 vs. Escherichia coli O83:H1 str. NRG 857C: 0.0131
Escherichia coli IAI39 vs. Desulfobacula toluolica Tol2: 0.3925
Escherichia coli O83:H1 str. NRG 857C vs. Desulfobacula toluolica Tol2: 0.3949


The real phylogenetic relationships:
                                              |
                                              |
                            --------------------------------------
                            |                                     |
                            |                                     |
                            |                                     |
                            |                                     |
               ------------------------------                     |
              |                             |                     |
              |                             |                     |       
      ----------------                      |                     |
     |                |                     |                     |
     |                |                     |                     |
E. coli IAI39   E. coli 083:H1        D. toluolica            S. aureus
