""" once we have mtDNA from the Circulamapper and schumutzi endoCaller, our seqeunce will be having many "N" in sequence, accordingly our depth and quality
hence it is important to determine which sequence have how many N in data, so this small script will be helpful """

def count_N_IN_fasta(fasta_file):

  with open(fasta_file) as f:
    N_details = {}
    current_header = None
  
    for line in f:
      line = line.strip()
      if not line:
        continue
      
      if line.startswith(">"):
        current_header = line.split()[0]
        N_details[current_header] = 0
      elif current_header is not None:
        N_details[current_header] += line.upper().count("N")

    for key, values in N_details.items():
      print(f"{key}: contain {values} Ns")


count_N_IN_fasta("Final_dataset_aligned_2.fas")
