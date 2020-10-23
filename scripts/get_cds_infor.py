#coding:utf-8
import argparse
import sys
import re
gene_id=set()
final_info={}
cds=open('/mnt/ilustre/users/dongmei.fu/newmdt/project/Genome_DB_finish/plants/Ipomoea_batatas/MPI/cds/transcript.fa.transdecoder.cds','r')
out=open('/mnt/ilustre/users/dongmei.fu/newmdt/project/Genome_DB_finish/plants/Ipomoea_batatas/MPI/cds/transcript.fa.transdecoder.cds.out','w')
for gene_info in cds.read( ).strip('>').split('\n>'):
    a=gene_info.split('|')[0]
    print(a)
    if not a in gene_id:
        gene_id.add(a)
        b=gene_info.split('\n')
        c='\n'.join(b[1:])
        final_info[a]=c
        out.write('>'+a+'\n'+c+'\n')
cds.close()
out.close()











