"""
Auth: Yaqiong
Email: waishushu@outlook.com
Time: 11 Mar 2018 16:43
Notice:
    If anything goes wrong, please don't contact me.
    If everything is OK, please do email me with a "Thank you" message.
"""

from .badge import Badge, BadgeType, BadgeUser
from .contest import Contest, ContestNotice, ContestProblem
from .covery_img import CoveryImg
from .file import File, FileType
from .forum import ForumNote, ForumSection, ForumSubject
from .judge_server import JudgeServer
from .login_log import LoginLog
from .mail import Mail, MailUser
from .option import Option
from .permission import Permission, PermissionUser
from .problem import Problem, ProblemTag, ProblemToTag
from .register import Register, RegisterType
from .sign_in import SignIn, SignInUser
from .similarity import Similarity
from .special_judge import SpecialJudge
from .submission import Submission
from .users import Users, UserGroup, UserToGroup

models = {
    'Badge': Badge,
    'BadgeType': BadgeType,
    'BadgeUser': BadgeUser,
    'Contest': Contest,
    'ContestNotice': ContestNotice,
    'ContestProblem': ContestProblem,
    'CoveryImg': CoveryImg,
    'File': File,
    'FileType': FileType,
    'ForumNote': ForumNote,
    'ForumSection': ForumSection,
    'ForumSubject': ForumSubject,
    'JudgeServer': JudgeServer,
    'LoginLog': LoginLog,
    'Mail': Mail,
    'MailUser': MailUser,
    'Option': Option,
    'Permission': Permission,
    'PermissionUser': PermissionUser,
    'Problem': Problem,
    'ProblemTag': ProblemTag,
    'ProblemToTag': ProblemToTag,
    'Register': Register,
    'RegisterType': RegisterType,
    'SignIn': SignIn,
    'SignInUser': SignInUser,
    'Similarity': Similarity,
    'SpecialJudge': SpecialJudge,
    'Submission': Submission,
    'Users': Users,
    'UserGroup': UserGroup,
    'UserToGroup': UserToGroup
}
