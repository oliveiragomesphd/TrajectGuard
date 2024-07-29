import pandas as pd
from itertools import combinations
from tqdm import tqdm
from typing import List, Dict, Any
from model.mat import MultipleAspectTrajectory


def read_and_prepare_dataset(dataset: pd.DataFrame, columns: List[tuple]) -> pd.DataFrame:
    dataset['coord'] = dataset.apply(lambda row: str(row['lat']) + str(row['lng']), axis=1)
    dataset = dataset[columns]
    return dataset


def mat_to_dataframe(mat: MultipleAspectTrajectory) -> pd.DataFrame:
    data = []

    permanent_aspects = {aspect.name: aspect.aspect for aspect in mat.permanent_aspects}

    for trajectory in mat.trajectories:
        long_term_aspects = {aspect.name: aspect.aspect for aspect in trajectory.long_term_aspects}
        for point in trajectory.points:
            volatile_aspects = {aspect.name: aspect.aspect for aspect in point.va}
            record = {
                "lat": point.lat,
                "lng": point.lng,
                "datetime": point.datetime,
                **permanent_aspects,
                **long_term_aspects,
                **volatile_aspects
            }
            data.append(record)

    return pd.DataFrame(data)


def generate_combinations(columns: List[str]) -> List[tuple]:
    array = []
    for i in range(len(columns)):
        array.extend(combinations(columns, i + 1))
    return array


def process_combinations(dataset: pd.DataFrame, combinations_list: List[tuple]) -> Dict[str, Any]:
    dic = {}
    msu = {}
    total = 0

    for combo in tqdm(combinations_list, desc="Processing Combinations"):
        position = list(combo[0])
        if len(combo) == 1:
            dataset_filtered = dataset.groupby(position).size().reset_index(name='total')
            dataset_filtered = dataset_filtered[dataset_filtered['total'] == 1]
            dic[str(position)] = dic.get(str(position), 0) + len(dataset_filtered)
            total += len(dataset_filtered)
            list_values = dataset_filtered[position].values.tolist()
            msu[str(position)] = msu.get(str(position), []) + list_values
        else:
            group = dataset.groupby(list(combo[-1])).size().reset_index(name='total')
            merge_total = group[group['total'] == 1]
            if len(merge_total) > 0:
                merge = pd.merge(dataset, merge_total, left_on=list(combo[-1]), right_on=list(combo[-1]))
                del merge['total']
                for count in range(len(combo) - 1):
                    if len(combo) - 1 != count:
                        filter_dataset = merge.groupby(list(combo[count])).size().reset_index(name='total')
                        filter_dataset = filter_dataset[filter_dataset['total'] > 1]
                        merge = pd.merge(merge, filter_dataset, left_on=list(combo[count]), right_on=list(combo[count]))
                        del merge['total']
                    if len(merge) == 0:
                        break
                if len(merge) > 0:
                    list_values = merge[list(combo[-1])].values.tolist()
                    msu[str(list(combo[-1]))] = msu.get(str(list(combo[-1])), []) + list_values
                    for sub_combo in combo:
                        dic[str(sub_combo)] = dic.get(str(sub_combo), 0) + len(merge)
                    total += len(merge)
    return dic, msu, total


def print_results(msu: Dict[str, Any], total: int):
    for key, values in msu.items():
        if len(values) > 0:
            print(
                f"""{key.replace('[', '').replace(']', '').replace("'", '')} & {round((len(values) / total) * 100, 5)}%  \\ \hline""")


def aspect_guard(mat: MultipleAspectTrajectory, columns: List[tuple]):
    dataset = mat_to_dataframe(mat)
    dataset = read_and_prepare_dataset(dataset, columns)
    columns = list(dataset.columns)
    combinations_list = generate_combinations(columns)
    dic, msu, total = process_combinations(dataset, [generate_combinations(list(combo)) for combo in combinations_list])
    print_results(msu, total)

