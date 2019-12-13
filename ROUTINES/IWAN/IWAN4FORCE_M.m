function [F, dFdu] = IWAN4FORCE_M(ut, pars)
    R = pars(:, 1);
    S = pars(:, 2);
    Chi = pars(:, 3);
    PhiMx = pars(:, 4);
    
    sut = sign(ut);
    ut = abs(ut);
    
    F = (((S+R.*PhiMx.^(Chi+1)./(Chi+1)).*ut - R.*ut.^(Chi+2)./((Chi+1).*(Chi+2))).*(ut<PhiMx) + ...
         (S+R.*PhiMx.^(Chi+1)./(Chi+2)).*PhiMx.*(ut>=PhiMx)).*sut;
    
    dFdu = (S + R.*(PhiMx.^(Chi+1)-ut.^(Chi+1))./(Chi+1)).*(ut<PhiMx);
    
    F = real(F);
    dFdu = real(dFdu);
end