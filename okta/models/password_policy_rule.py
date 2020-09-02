# flake8: noqa
"""
Copyright 2020 Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.models.policy_rule\
    import PolicyRule
import okta.models.password_policy_rule_actions\
    as password_policy_rule_actions
import okta.models.password_policy_rule_conditions\
    as password_policy_rule_conditions


class PasswordPolicyRule(
    PolicyRule
):
    """
    A class for PasswordPolicyRule objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.type = "PASSWORD"
            if "actions" in config:
                if isinstance(config["actions"],
                              password_policy_rule_actions.PasswordPolicyRuleActions):
                    self.actions = config["actions"]
                else:
                    self.actions = password_policy_rule_actions.PasswordPolicyRuleActions(
                        config["actions"]
                    )
            else:
                self.actions = None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              password_policy_rule_conditions.PasswordPolicyRuleConditions):
                    self.conditions = config["conditions"]
                else:
                    self.conditions = password_policy_rule_conditions.PasswordPolicyRuleConditions(
                        config["conditions"]
                    )
            else:
                self.conditions = None
            self.name = config["name"]\
                if "name" in config else None
        else:
            self.actions = None
            self.conditions = None
            self.name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "actions": self.actions,
            "conditions": self.conditions,
            "name": self.name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
