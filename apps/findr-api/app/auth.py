from __future__ import annotations

from typing import Iterable, Optional

from fastapi import Header, HTTPException, status

from .config import settings
from .models import AuthContext


def parse_roles(raw_roles: Optional[str]) -> list[str]:
    if not raw_roles:
        return []
    return [role.strip() for role in raw_roles.split(",") if role.strip()]


def required_search_roles() -> list[str]:
    return parse_roles(settings.default_search_roles)


def _require_shared_secret(provided_secret: Optional[str]) -> None:
    if not settings.auth_required:
        return
    if not settings.trusted_shared_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Auth is enabled but FINDR_TRUSTED_SHARED_SECRET is not configured.",
        )
    if provided_secret != settings.trusted_shared_secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid trusted shared secret.",
        )


def _require_roles(user_roles: Iterable[str], expected_roles: Iterable[str]) -> None:
    if not settings.auth_required:
        return
    role_set = {role.strip() for role in user_roles if role.strip()}
    if not role_set.intersection(expected_roles):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not have a Finder role required for this action.",
        )


def require_auth_context(
    x_findr_user_id: Optional[str] = Header(default=None),
    x_findr_user_name: Optional[str] = Header(default=None),
    x_findr_roles: Optional[str] = Header(default=None),
    x_findr_shared_secret: Optional[str] = Header(default=None),
) -> AuthContext:
    roles = parse_roles(x_findr_roles)
    _require_shared_secret(x_findr_shared_secret)

    if settings.auth_required and not x_findr_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Finder user context.",
        )

    _require_roles(roles, required_search_roles())

    return AuthContext(
        user_id=x_findr_user_id or "anonymous",
        user_name=x_findr_user_name,
        roles=roles,
        authenticated_via="proxy-header" if x_findr_user_id else "anonymous",
    )
