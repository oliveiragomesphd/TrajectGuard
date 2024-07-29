from itertools import combinations, permutations
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from model.mat import MultipleAspectTrajectory

class LocationRisk:

    def __init__(self, knowledge, dataset, columns, operation, title, anonimo=None):
        self.knowledge = knowledge
        self.dataset = dataset
        self.anonimo = anonimo
        self.columns = columns
        self.operation = operation
        self.title = title

        self.groupby_volatile_location = {}
        self.total = []
        self.user_locations = {}
        self.user_locations_anonimo = {}
        self.risk = pd.DataFrame(columns=["uid", "risk"])
        self.skip = pd.DataFrame(columns=["uid", "skips", "combs"])

    def create_user_location(self):
        self.user_locations = self._create_user_location_dict(self.dataset)
        if self.anonimo is not None:
            self.user_locations_anonimo = self._create_user_location_dict(self.anonimo)

    def _create_user_location_dict(self, dataset):
        user_locations = {}
        for _, row in dataset.iterrows():
            user_date_id = str(row['uid'])
            if user_date_id not in user_locations:
                user_locations[user_date_id] = []
            user_locations[user_date_id].append(row[self.columns].values.tolist())
        return user_locations

    def create_counts(self):
        print(len(self.user_locations))
        total = self.dataset.groupby(self.columns).size().reset_index(name='total')
        dataset_freq = pd.merge(self.dataset, total, left_on=self.columns, right_on=self.columns)

        count = 0
        for user in self.user_locations:
            user_id = user
            count += 1
            print(count)
            points = self.user_locations[user]
            if self.operation == 'combinations':
                combs = combinations(points, self.knowledge)
            elif self.operation == 'permutations':
                combs = permutations(points, self.knowledge)

            dataset_user = dataset_freq[dataset_freq['uid'] == user_id]
            unique = dataset_user[dataset_user['total'] == 1]

            arr_df2 = unique[self.columns].values
            combs_list = list(combs)
            count2 = 0
            for comb in combs_list:
                inst = pd.DataFrame(data=comb, columns=self.columns)
                arr_df1 = inst.values
                condition = np.any(np.all(arr_df1[:, None, :] == arr_df2[None, :, :], axis=-1))

                if not condition:
                    if str(comb) not in self.groupby_volatile_location:
                        self.groupby_volatile_location[str(comb)] = 0
                    self.groupby_volatile_location[str(comb)] += 1

    def evaluate_error(self, filter_strings=None, filter_columns=None):
        if self.anonimo is not None:
            self._evaluate_with_two_datasets(filter_strings, filter_columns)
        else:
            self._evaluate_with_single_dataset(filter_strings, filter_columns)

    def _evaluate_with_single_dataset(self, filter_strings=None, filter_columns=None):
        self.total = []
        print(filter_columns)
        self.risk = pd.DataFrame(columns=["uid", "risk"])
        self.skip = pd.DataFrame(columns=["uid", "skips", "combs"])
        groupby_volatile_location_user_unique = {}
        print(len(self.user_locations))

        for user in self.user_locations:
            count_skip = 0
            user_id = user
            points = self.user_locations[user]

            if len(points) >= self.knowledge:
                if self.operation == 'combinations':
                    combs = combinations(points, self.knowledge)
                elif self.operation == 'permutations':
                    combs = permutations(points, self.knowledge)

                combs_list = list(combs)
                for comb in combs_list:
                    if str(user_id) + str(comb) not in groupby_volatile_location_user_unique:
                        groupby_volatile_location_user_unique[str(user_id) + str(comb)] = 0
                    groupby_volatile_location_user_unique[str(user_id) + str(comb)] += 1
                aux_values = []
                if filter_strings is not None:
                    filter_strings['id_date'] = filter_strings['uid'].astype(str)
                    user_data = filter_strings[filter_strings['id_date'] == user]
                    arr_df2 = user_data[filter_columns].values
                for comb2 in combs_list:
                    if filter_strings is not None:
                        inst = pd.DataFrame(data=comb2, columns=self.columns)

                    if str(comb2) not in self.groupby_volatile_location:
                        risk = groupby_volatile_location_user_unique[str(user_id) + str(comb2)]
                    else:
                        risk = self.groupby_volatile_location[str(comb2)]
                    value = groupby_volatile_location_user_unique[str(user_id) + str(comb2)] / risk
                    aux_values.append(value)
                    if value == 1:
                        break
                if len(aux_values) > 0:
                    self.total.append(max(aux_values))
                    self.risk.loc[len(self.risk.index)] = [user, max(aux_values)]
                    self.skip.loc[len(self.skip.index)] = [user, count_skip, len(combs_list)]
                groupby_volatile_location_user_unique = {}

    def _evaluate_with_two_datasets(self, filter_strings=None, filter_columns=None):
        self.total = []
        self.risk = pd.DataFrame(columns=["uid", "risk"])
        self.skip = pd.DataFrame(columns=["uid", "skips", "combs"])
        groupby_volatile_location_user_unique = {}
        print(len(self.user_locations_anonimo))

        for user in self.user_locations_anonimo:
            count_skip = 0
            user_id = user
            points = self.user_locations_anonimo[user]

            if len(points) >= self.knowledge:
                if self.operation == 'combinations':
                    combs = combinations(points, self.knowledge)
                elif self.operation == 'permutations':
                    combs = permutations(points, self.knowledge)

                combs_list = list(combs)
                for comb in combs_list:
                    if str(user_id) + str(comb) not in groupby_volatile_location_user_unique:
                        groupby_volatile_location_user_unique[str(user_id) + str(comb)] = 0
                    groupby_volatile_location_user_unique[str(user_id) + str(comb)] += 1
                aux_values = []
                if filter_strings is not None:
                    filter_strings['id_date'] = filter_strings['uid'].astype(str)
                    user_data = filter_strings[filter_strings['id_date'] == user]
                    arr_df2 = user_data[filter_columns].values
                for comb2 in combs_list:
                    if filter_strings is not None:
                        inst = pd.DataFrame(data=comb2, columns=self.columns)

                    if str(comb2) not in self.groupby_volatile_location:
                        risk = groupby_volatile_location_user_unique[str(user_id) + str(comb2)]
                    else:
                        risk = self.groupby_volatile_location[str(comb2)]
                    value = groupby_volatile_location_user_unique[str(user_id) + str(comb2)] / risk
                    aux_values.append(value)
                    if value == 1:
                        break
                if len(aux_values) > 0:
                    self.total.append(max(aux_values))
                    self.risk.loc[len(self.risk.index)] = [user, max(aux_values)]
                    self.skip.loc[len(self.skip.index)] = [user, count_skip, len(combs_list)]
                groupby_volatile_location_user_unique = {}

    def error_aggregate(self):
        total = pd.DataFrame(self.total, columns=['risk'])
        return total.groupby(['risk']).size().reset_index(name='quantity')

    def create_chart(self, file_name, title, totals, markers):
        for x in range(len(totals)):
            total = totals[x]
            results = total[0]
            plt.plot(results["risk"], results["quantity"], marker=markers[x], label=total[1])

        plt.xlabel("Risk", fontsize=16, weight='bold')
        plt.xticks(fontsize=15, weight='bold')
        plt.yticks(fontsize=15, weight='bold')
        plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        plt.ylabel("Quantity Trajectories", fontsize=16, weight='bold')
        plt.legend(fontsize=14).set_title("Aspects")
        plt.title(title, fontsize=17, weight='bold')
        plt.savefig(file_name, bbox_inches='tight')
        plt.show()




