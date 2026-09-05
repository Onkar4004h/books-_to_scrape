def freq_of_each(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1 
    return freq
# print(freq_of_each([1, 2, 2, 3, 1, 1, 4]))

def most_frequnt(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    max_count = 0
    answer = None        
    for num,count in freq.items():
        if count > max_count:
            max_count = count
            answer=num 
    return answer

# print(most_frequnt([1, 2, 2, 3, 3, 3, 4]))
def first_non_repeating(word):

    freq = {}
    for x in word:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    for letter,count in freq.items():
        if count==1:
            return letter

# print(first_non_repeating("lleetcode"))
def unique_element(s):

    freq = {}
    for x in s:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    answer = ""        
    for letter,count in freq.items():
        if count==1:
            answer=letter
            break
    for i in range(len(s)):
        if s[i]==answer:
            return i 
    return -1    
# print(unique_element("aabb"))
def first_repeating(nums):
    freq={}
    for x in nums:
        if x in freq:
            freq[x]+=1
            if freq[x]==2:
                return x
        else:
            freq[x]=1
# print(first_repeating([10, 5, 3, 4, 3, 5, 6])) 
def check_frequinces(num1,num2):
    freq1={}
    freq2={}
    for x in num1:
        if x in freq1:
            freq1[x]+=1
        else:
            freq1[x]=1 
    for y in num2:
        if y in freq2:
            freq2[y]+=1
        else:
            freq2[y]=1
    if freq1==freq2:
        return True
    else:
        return False

print(check_frequinces([1, 2, 2, 3],[1, 2, 3, 3]))                                        
             
                               
    
