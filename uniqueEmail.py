class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            # Step 0: Split the email into local and domain parts
            local_name,domain_name = email.split("@")

            # Step 1: Split at the '+' character
            plus_split = local_name.split('+')  # ["jo.hn.doe", "spam"]

            # Step 2: Take the part before '+'
            before_plus = plus_split[0]  # "jo.hn.doe"

            # Step 3: Split that part by '.'
            dot_split = before_plus.split('.')  # ["jo", "hn", "doe"]

            # Step 4: Join the parts without dots
            cleaned_local_name = "".join(dot_split)  # "johndoe"

            # Assign to final variable
            local_name = cleaned_local_name

            email = local_name +'@' + domain_name
            email_set.add(email)
        return len(email_set)