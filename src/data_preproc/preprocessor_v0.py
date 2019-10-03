import pandas as pd
import os
from Bio import SeqIO

def process ( f_name, label, source) :
    df_columns = [
        'db_id',
        'seq_id',
        'seq',
        'label',
        'description_src'
    ]
    df = pd.DataFrame(columns=df_columns)
    SOURCE = './../../RawData/trainingsets'
    input_file = os.path.join(SOURCE,f_name)
    fasta_sequences = SeqIO.parse(open(input_file),'fasta')
    count = 0
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        tmp = str(fasta.id).split('|')
        _dict = {
            'db_id' : tmp[0],
            'seq_id':  tmp[1],
            'seq': str(sequence),
            'label' : label,
            'description_src' : source
        }
        df = df.append(_dict,ignore_index=True)
        count+=1

    print('label :',label, '|| count = ',count)
    return df

def main():

    input_file_names = [
        'dataset_pos.fa',
        'dataset_hard.fa',
        'dataset_mod.fa',
        'dataset_easy.fa'
    ]
    input_sources = ['pos','hard','mod','easy']
    input_labels = [ 1, 0, 0, 0 ]
    master_df = None

    for f_name,_label,source in zip(input_file_names,input_labels,input_sources):

        df = process(f_name, _label, source)
        if master_df is not None:
            master_df = master_df.append(df,ignore_index=True)
        else:
            master_df = pd.DataFrame(df,copy=True)

    op_loc = './../../GeneratedData'
    op_f_name = 'combined_toxins_sequence.csv'
    master_df.to_csv(
        os.path.join(
            op_loc,op_f_name
        ),
        index=False
    )

    return

main()

