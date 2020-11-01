from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uemails = set()
        for email in emails:
            at = email.find("@")
            if at == -1:
                continue
            local = email[:at]
            domain = email[at:]
            plus = local.find("+")
            if plus != -1:
                local = local[0:plus]
            local = local.replace(".", "")
            uemails.add(local+domain)
        return len(uemails)
