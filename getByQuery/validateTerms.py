import wikipedia

def validateTerm(term,score):
    try:
        summary = {
            "term":term,
            "score":score,
            "summary":wikipedia.summary(term,sentences=2,auto_suggest=False)
        }
        return summary
    except:
        return None

def validateTerms(terms_list,terms_score):
    validatedTermsObjs = []
    for i in range(0,len(terms_list)):
        validateResult = validateTerm(terms_list[i],terms_score[i])
        if (validateResult):
            validatedTermsObjs.append(validateResult)
    return validatedTermsObjs