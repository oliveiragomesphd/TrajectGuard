import pandas as pd

class LongTermAspectRiskCalculator:
    def __init__(self, mats):
        self.mats = mats
        self.long_term_aspects_df = self._create_long_term_aspects_df()
        self.risk = pd.DataFrame(columns=['user_id', 'risk'])

    def _create_long_term_aspects_df(self):
        data = []
        for mat in self.mats:
            user_id = mat.user_id
            for trajectory in mat.trajectories:
                for aspect in trajectory.long_term_aspects:
                    aspect_dict = {
                        'user_id': user_id,
                        'trajectory_id': trajectory.identifier,
                        aspect.name: aspect.aspect
                    }
                    data.append(aspect_dict)
        return pd.DataFrame(data)

    def calculate_frequencies(self):
        aspect_cols = self.long_term_aspects_df.drop(columns=['user_id', 'trajectory_id'])
        freq_df = aspect_cols.groupby(list(aspect_cols.columns)).size().reset_index(name='frequency')
        return freq_df

    def calculate_risk(self):
        freq_df = self.calculate_frequencies()
        merged_df = pd.merge(self.long_term_aspects_df, freq_df, on=list(self.long_term_aspects_df.columns.drop(['user_id', 'trajectory_id'])), how='left')
        total_long_terms = len(self.long_term_aspects_df)
        merged_df['risk'] = merged_df['frequency'] / total_long_terms
        self.risk = merged_df[['user_id', 'risk']].drop_duplicates()

    def get_risk(self):
        return self.risk
