import copy

import pysubs2

def load_subtitles(file_name: str):
    subs = pysubs2.load(f"output/{file_name}.srt")
    return subs

def revise(subs, idx: int, content: str):
    subs[idx].text = content
    return 0

def merge(subs, idx01, idx02):
    if idx02 - 1 == idx01 and 0 <= idx01 <= len(subs):
        first = subs[idx01]
        second = subs[idx02]
        subs[idx01].text = first.text + second.text
        subs[idx01].end = second.end
        del subs[idx02]
        return 0
    else:
        print("merge error")
        return 1

def split(subs, idx, split_time, content01, content02):
    original_content = subs[idx]

    if not original_content.start < split_time < original_content.end:
        print("split error")
        return 1
    else:
        first = copy.copy(subs[idx])
        first.text = content01
        first.end = split_time

        second = copy.copy(subs[idx])
        second.text = content02
        second.start = split_time

        subs[idx:idx+1] = [first, second]

        return 0

def delete(subs, idx):
    subs.pop(idx)
    return 0

def insert(subs, idx, content, end_time):
    new_content = copy.copy(subs[idx])

    if not new_content.start < end_time < new_content.end:
        print("insert error")
        return 1
    else:
        new_content.text = content
        new_content.end = end_time

        subs[idx].start = end_time
        subs.insert(idx, new_content)

        return 0

def revise_time(subs, idx, start_time, end_time):
    subs[idx].start = start_time
    subs[idx].end = end_time
    return 0

def save_subtitles(subs, title: str):
    subs.save(f"output/{title}_edited.srt")
    return 0