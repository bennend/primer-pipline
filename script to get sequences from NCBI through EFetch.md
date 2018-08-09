```
Sequence_identifiers_list=['AY236073','HM015773','HQ700343','JN205800','JN704570','JQ809466','JX423831','JX438000','JX438001','JX893517','FN396876','JF703135','JQ734687','JN104597','JN967644', 'JX262694', 'AB744718' ,'KC999080' ,'KF361506', 'KP265939' ,'AB926431' ,'LC012596' ,'KM210087', 'KP735848', 'KP862821','AJ243491','AB010417','AF244145','AF290912','AB040994','AF318077','AF322577','KC543497','AB074433','AB074436','AJ420864','AJ550807','AY553332','AY553333','AJ584652','AY780674','EF118171','AB196988','AB204557','DQ361087','EF192154','EU541448','GU045307','JF894248','JQ407409','HQ438058','DQ522237','KF148593','JQ002629','JN848782','AB715422','JF816544','JX131372','HQ875573','AB753457','AB753458','AB753456','AB777500','AB777501','KJ510410','KP050486','KM087857','KP681694','LC031883','LC055762','AF191564', 'AF300454', 'AY135661','AY144612', 'AY165025', 'AJ536835', 'AY524987', 'AY524988', 'AY524989', 'AY605049', 'DQ143913', 'DQ365886', 'AY635904','EU419745', 'EU419746', 'EU118148', 'AM778091', 'FJ822963', 'GQ242167', 'HM855205', 'HM750249', 'FR748153', 'HQ858608', 'JF900599' ,'JX311308', 'JN129451','JN982330', 'JN676230', 'JX258134', 'JX013656', 'JX982634', 'JX982635', 'JX982636', 'KC469971', 'KF131539', 'KP071470', 'KP096412','KP681696','KP681695', 'KP749829','AY034847', 'AF395881', 'AY700571', 'EU400222', 'EU555534', 'EU729727', 'FJ234412', 'FJ624872', 'GQ140348', 'HM066995', 'HQ641421', 'HQ342889', 'JX524191', 'KC433553', 'KC465199', 'KC465200', 'KP681699', 'KJ775801', 'KM379100', 'KR052099']
from Bio import Entrez
from Bio import SeqIO
from Bio import SeqFeature
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
Entrez.email='Your e-mail'
OXA_productlist=[]
VIM_productlist=[]
IMP_productlist=[]
KPC_productlist=[]
NDM_productlist=[]
handle=Entrez.efetch(db="nucleotide",id=IDlist,rettype='gb')
for record in SeqIO.parse(handle,"genbank"):
    for feature in record.features:
        if "OXA" in str(feature.qualifiers.get("product")):
            f=open("/Your favored directory/OXA48like_SEQ.fasta","a+")
            f.write(">"+ record.id+'|'+"".join(feature.qualifiers.get('product'))+"\n"+str(feature.location.extract(record.seq))+"\n")
            f.close
        if "IMP" in str(feature.qualifiers.get("product")):
            f=open("/Your favored directory/IMP_SEQ.fasta", "a+")
            f.write(">"+ record.id+' | '+"".join(feature.qualifiers.get('product'))+"\n"+str(feature.location.extract(record.seq))+"\n")
            f.close
            # IMP_seqences=SeqRecord(feature.location.extract(record.seq),id=feature.qualifiers.get("product_id"),description=str(feature.qualifiers.get("product")))
            # IMP_productlist.append(IMP_seqences)
        if "KPC" in str(feature.qualifiers.get("product")):
            f=open("/Your favored directory/KPC_SEQ.fasta", "a+")
            f.write(">"+ record.id+' | '+"".join(feature.qualifiers.get('product'))+"\n"+str(feature.location.extract(record.seq))+"\n")
            f.close
            # KPC_seqences=SeqRecord(feature.location.extract(record.seq),id=feature.qualifiers.get("product_id"),description=str(feature.qualifiers.get("product")))
            # KPC_productlist.append(KPC_seqences)
        if "VIM" in str(feature.qualifiers.get("product")):
            f=open("/Your favored directory/VIM_SEQ.fasta", "a+")
            f.write(">"+ record.id+' | '+"".join(feature.qualifiers.get('product'))+"\n"+str(feature.location.extract(record.seq))+"\n")
            f.close
            # VIM_seqences=SeqRecord(feature.location.extract(record.seq),id=feature.qualifiers.get("product_id"),description=str(feature.qualifiers.get("product")))
            # VIM_productlist.append(VIM_seqences)
        if "NDM" in str(feature.qualifiers.get("product")):
            f=open("/Your favored directory/NDM_SEQ.fasta", "a+")
            f.write(">"+ record.id+' | '+"".join(feature.qualifiers.get('product'))+"\n"+str(feature.location.extract(record.seq))+"\n")
            f.close
            # NDM_seqences=SeqRecord(feature.location.extract(record.seq),id=feature.qualifiers.get("product_id"),description=str(feature.qualifiers.get("product")))
            # NDM_productlist.append(NDM_seqences)
        else:
            pass
```
