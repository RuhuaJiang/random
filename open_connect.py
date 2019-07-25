"""
This assumes we already have male.csv
and female.csv, ordered by timestamp,
everyone in that csv interests in opposite sex, LGBT is
handled sperated.
"""


SEX_INDEX = 3
TRAIT_1_INDEX = 5
TRAIT_2_INDEX = 6
WANT_TRAIT_1_INDEX = 7
WANT_TRAIT_2_INDEX = 8
INTEREST_1_INDEX = 9
INTEREST_2_INDEX = 10


# Collect male and female list
male_profile_list = []
female_profile_list = []
with open("male.csv") as f:
    male_id = 0
    for line in f:
        profile = line.split(',')
        male_profile_list.append((male_id, profile))
        male_id += 1

with open("female.csv") as f:
    female_id = 0
    for line in f:
        profile = line.split(',')
        female_profile_list.append((female_id,profile))
        female_id += 1

print male_profile_list
print female_profile_list

matched_female_ids = set()
matched_male_ids = set()

trait_matched_couple = set()


### first pass, match all by traits
for male_id, male_profile in male_profile_list:
    if male_id in matched_male_ids:
        continue
    for female_id, female_profile in female_profile_list:
        if female_id in matched_female_ids:
            continue
        male_want_traits = set([male_profile[WANT_TRAIT_1_INDEX], male_profile[WANT_TRAIT_2_INDEX]])
        male_traits = set([male_profile[TRAIT_1_INDEX], male_profile[TRAIT_2_INDEX]])

        female_want_traits = set([female_profile[WANT_TRAIT_1_INDEX], female_profile[WANT_TRAIT_2_INDEX]])
        female_traits = set([female_profile[TRAIT_1_INDEX], female_profile[TRAIT_2_INDEX]])

        if male_want_traits.intersection(female_traits) and female_traits.intersection(male_traits):
            matched_female_ids.add(female_id)
            matched_male_ids.add(male_id)
            # print "male %s and female %s match success"%( male_id, female_id)
            # print male_want_traits.intersection(female_traits)
            # print female_traits.intersection(male_traits)
            # print ','.join(male_profile)
            # print ','.join(female_profile)
            trait_matched_couple.add((','.join(male_profile), ','.join(female_profile)))



### second pass, match all by interests
interests_matched_couple = set()
for male_id, male_profile in male_profile_list:
    if male_id in matched_male_ids:
        continue
    for female_id, female_profile in female_profile_list:
        if female_id in matched_female_ids:
            continue
        male_interests = set([male_profile[INTEREST_1_INDEX], male_profile[INTEREST_2_INDEX]])
        female_interests = set([female_profile[INTEREST_1_INDEX], female_profile[INTEREST_2_INDEX]])
        if male_interests.intersection(female_interests):
            # print ','.join(male_profile)
            # print ','.join(female_profile)
            interests_matched_couple.add((','.join(male_profile), ','.join(female_profile)))


#### Print all matched result
for matched in trait_matched_couple:
    print "trait matched:"
    print matched[0], matched[1]
for matched in interests_matched_couple:
    print "interests matched:"
    print matched[0], matched[1]
