import os
import pandas as pd
from flask import Blueprint,request,jsonify
from Bio.Seq import Seq, translate


bp = Blueprint("trans_seq", __name__, url_prefix="/trans_seq")

@bp.route('/<rawseq>',methods=['post','get'])
def trans_seq(rawseq):
    try:
        print(rawseq)
        rawseq = rawseq.upper()
        # rawseq = request.form.get('rawseq')
        rawseq = ''.join(list(filter(str.isalpha,rawseq)))
        translate_dict = {}
        result_53 = {}
        result_35 = {}
        for start in range(3):
            result_53[f'5`3` frame{start+1}'] = str(Seq(rawseq[start:]).translate())
            result_35[f'3`5` frame{start+1}'] = str((Seq(rawseq).reverse_complement())[start:].translate())
        translate_dict['53'] = result_53
        translate_dict['35'] = result_35
        result = {'message':'','result':translate_dict,'rawseq':rawseq,'code':200}
        print(result)
    except BaseException as e:
        result = {'message':str(e),'result':{},'rawseq':rawseq,'code':400}
    print(jsonify(result))
    return jsonify(result)
    # print(result)
    # return 'haha'
