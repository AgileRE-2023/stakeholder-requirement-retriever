import wikipedia

def validateTerm(term):
    try:
        summary = {
            "term":term,
            "summary":wikipedia.summary(term,sentences=2,auto_suggest=False)
        }
        return summary
    except:
        return None

def validateTerms(terms_list):
    validatedTermsObjs = []
    for term in terms_list:
        validateResult = validateTerm(term)
        if (validateResult):
            validatedTermsObjs.append(validateResult)
    return validatedTermsObjs