from django.core.exceptions import PermissionDenied

def perm(perm, view, **viewkwargs):
    assert(perm in ["any", "user", "volunteer", "staff", "admin"])

    def decorator(request, **reqkwargs):
        if perm != "any":
            if not request.user.is_authenticated(): raise PermissionDenied
            user, vol, staff, admin = (request.user.profile.is_user, 
                                       request.user.profile.is_volunteer, 
                                       request.user.profile.is_staff,
                                       request.user.profile.is_admin)
            if perm == "admin" and not admin: raise PermissionDenied
            elif perm == "staff" and not (admin or staff): raise PermissionDenied
            elif perm == "volunteer" and not (admin or staff or vol): raise PermissionDenied
            elif perm == "user" and not (admin or staff or vol or user): raise PermissionDenied

        return view.as_view(**viewkwargs)(request, **reqkwargs)

    return decorator

def require_admin(user):
    if not user.is_authenticated(): raise PermissionDenied
    if user.profile.is_admin: return True
    raise PermissionDenied

def require_staff(user):
    if not user.is_authenticated(): raise PermissionDenied
    if user.profile.is_admin: return True
    if user.profile.is_staff: return True
    raise PermissionDenied

def require_volunteer(user):
    if not user.is_authenticated(): raise PermissionDenied 
    if user.profile.is_admin: return True
    if user.profile.is_staff: return True
    if user.profile.is_volunteer: return True
    raise PermissionDenied

def require_user(user):
    if not user.is_authenticated(): raise PermissionDenied 
    if user.profile.is_admin: return True
    if user.profile.is_user: return True
    raise PermissionDenied