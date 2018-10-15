import pandas as pd
import numpy as np
from ROC.get_fpr_tpr import PlotRoc


class PlotRocHamming(PlotRoc):
    def __init__(self, input_gene_path, leave_gene_path, input_all_path, predict_path):
        super().__init__(input_gene_path, leave_gene_path, input_all_path, predict_path)



    def tans_predict(self, pre_path, p_name, n_name):
        # read predict
        data = pd.read_csv(pre_path, sep='\t')
        # get ecm+ and llr
        re = data

        re_symbol = list(re['name'])
        re_llr = list(re['score'])
        # if p_name not in predict result
        not_pre_p_names = [x for x in p_name if x not in re_symbol]
        # n_name not in predict result

        not_pre_n_names = [x for x in n_name if x not in re_symbol]
        if not_pre_p_names:
            re_symbol.extend(not_pre_p_names)
            llr = [float("inf")] * len(not_pre_p_names)
            re_llr.extend(llr)
        if not_pre_n_names:
            re_symbol.extend(not_pre_n_names)
            llr2 = [float("inf")] * len(not_pre_n_names)
            re_llr.extend(llr2)
        # change col names
        dic = {'name': re_symbol, 'score': re_llr}
        pre = pd.DataFrame(dic)
        pre = pre.sort_values('score', ascending=False)

        return pre

    def get_tpr_fpr(self, p_name: list,
                    n_name: list,
                    threshold: int,
                    pre: 'dataframe', ) -> "The tpr and fpr":
        """
        Get fpr and tpr
        :param p_name: Positive genes
        :param n_name: Negative genes
        :param threshold: The threshold
        :param pre: The predict dataframe
        :return: tpr and fpr
        """

        # bayes threshold
        threshold_up = list(pre.name[pre.score <= threshold])
        threshold_down = list(pre.name[pre.score > threshold])

        # # distance threshold
        # threshold_up = list(pre.name[pre.score <= threshold])
        # threshold_down = list(pre.name[pre.score > threshold])
        tp = len([x for x in p_name if x in threshold_up])
        fp = len([x for x in n_name if x in threshold_up])
        tn = len([x for x in n_name if x in threshold_down])
        fn = len([x for x in p_name if x in threshold_down])
        # print((tp, fp, tn, fn))

        tpr = tp / (tp + fn)

        fpr = fp / (fp + tn)
        if tp + fp == 0:
            precision = np.nan
        else:
            precision = tp / (tp + fp)

        return precision, tpr, fpr, (tp, fp, tn, fn)  # do every threshold