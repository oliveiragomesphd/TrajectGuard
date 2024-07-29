import pandas as pd


class PermanentAspectRiskCalculator:
    def __init__(self, mats):
        self.mats = mats
        self.permanent_aspects_df = self._create_permanent_aspects_df()
        self.risk = pd.DataFrame(columns=['user_id', 'risk'])

    def _create_permanent_aspects_df(self):
        data = []
        for mat in self.mats:
            aspect_dict = {aspect.name: aspect.aspect for aspect in mat.permanent_aspects}
            aspect_dict['user_id'] = mat.user_id
            data.append(aspect_dict)
        return pd.DataFrame(data)

    def calculate_frequencies(self):
        aspect_cols = self.permanent_aspects_df.drop(columns=['user_id'])
        freq_df = aspect_cols.groupby(list(aspect_cols.columns)).size().reset_index(name='frequency')
        return freq_df

    def calculate_risk(self):
        freq_df = self.calculate_frequencies()
        merged_df = pd.merge(self.permanent_aspects_df, freq_df, on=list(self.permanent_aspects_df.columns.drop('user_id')), how='left')
        merged_df['risk'] = 1 / merged_df['frequency']
        self.risk = merged_df[['user_id', 'risk']]

    def get_risk(self):
        return self.risk



