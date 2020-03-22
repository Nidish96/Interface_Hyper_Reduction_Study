function [ErrsWZD, dErrsdp, BB] = WJMODEL_BBFUN_MASING(pars, mdi, expdat, K, M, X0, Fv, L, Txyn, Qxyn, CFUN, DFUN, Npatches, opt)

    % Prestress
    [Xstat, eflg] = fsolve(@(X) WJRES_STR([X; 0.0], pars, K, Fv, Fv, L, Txyn, Qxyn, CFUN, Npatches), X0, opt);
    [~,dRstat,~,dRdpstat] = WJRES_STR([Xstat; 0.0], pars, K, Fv, Fv, L, Txyn, Qxyn, CFUN, Npatches);
    dXdpstat = -dRstat\dRdpstat;
    [Dxynstat, dDxyndXstat, dDxyndpstat] = DFUN([Qxyn(1:3:end,:)*Xstat, Qxyn(2:3:end,:)*Xstat, Qxyn(3:3:end,:)*Xstat], pars);
	prev.uxyn = [Qxyn(1:3:end,:)*Xstat, Qxyn(2:3:end,:)*Xstat, Qxyn(3:3:end,:)*Xstat*0];
    [prev.Fxyn, dFxynstat, prev.dFxyndpar] = CFUN(prev.uxyn, pars);
    prev.dFxyndXdpar = reshape(dFxynstat', Npatches*3, 1).*Qxyn*dXdpstat;
    
%     prev.uxyn = prev.uxyn*0;
%     prev.Fxyn = prev.Fxyn*0;
%     prev.dFxyndpar = prev.dFxyndpar*0;
%     prev.dFxyndXdpar = prev.dFxyndXdpar*0;
    %% Modal Analysis
    [Vst, Wst] = eigs(dRstat, M, 10, 'SM');
    Wst = sqrt(diag(Wst));
    Vst = Vst./sqrt(diag(Vst'*M*Vst)');
    
    Vm = Vst(:, mdi);
    Wm = Wst(mdi);
    
    %% QSNMA
    BB.Q = expdat.Q;
    BB.W = zeros(size(BB.Q));
    BB.Z = zeros(size(BB.Q));
    BB.D = zeros(size(BB.Q));
    
    dWdp = zeros(1, length(pars));
    dDdp = zeros(1, length(pars));
    dZdp = zeros(1, length(pars));
    
    ErrsWZD = zeros(3, 1);
    dErrsdp = zeros(3, length(pars));
    
    for i=1:length(BB.Q)
        X0 = [Xstat+Vm*BB.Q(i); Wm^2];
        Xd = fsolve(@(X) WJRES_RQNM([X; BB.Q(i)], pars, prev, K, M, Xstat, dXdpstat, ...
            Fv, L, Txyn, Qxyn, CFUN, Npatches), X0, opt);
        [~, dRdX, ~, dRdp] = WJRES_RQNM([Xd; BB.Q(i)], pars, prev, K, M, Xstat, dXdpstat, Fv, ...
            L, Txyn, Qxyn, CFUN, Npatches);
        dXdp = -dRdX\dRdp;
        [Dxyn, dDxyndX, dDxyndp] = DFUN([Qxyn(1:3:end,:)*Xd(1:end-1), Qxyn(2:3:end,:)*Xd(1:end-1), Qxyn(3:3:end,:)*Xd(1:end-1)], pars);
        
        BB.W(i) = sqrt(Xd(end));
        BB.D(i) = sum(sum(Dxyn-Dxynstat));
        BB.Z(i) = BB.D(i)/(2*pi*(BB.Q(i)*BB.W(i))^2) + expdat.Z(1)*0;
        
        dWdp = dXdp(end,:)/(2*BB.W(i));
        dDdp = sum(sum(dDxyndp-dDxyndpstat, 1), 3) + ...
            reshape(dDxyndX', Npatches*3, 1)'*Qxyn*dXdp(1:end-1,:) - ...
            reshape(dDxyndXstat', Npatches*3, 1)'*Qxyn*dXdpstat;
        dZdp = (dDdp - 2*BB.D(i)/BB.W(i)*dWdp)/(2*pi*(BB.Q(i)*BB.W(i))^2);
        
        ErrsWZD(1) = ErrsWZD(1) + ((BB.W(i)-expdat.W(i))/expdat.W(i))^2;
        ErrsWZD(2) = ErrsWZD(2) + ((BB.Z(i)-expdat.Z(i))/expdat.Z(i))^2;
        ErrsWZD(3) = ErrsWZD(3) + ((BB.D(i)-expdat.D(i))/expdat.D(i))^2;
        
        dErrsdp(1,:) = dErrsdp(1,:) + 2*((BB.W(i)-expdat.W(i))/expdat.W(i)^2)*dWdp;
        dErrsdp(2,:) = dErrsdp(2,:) + 2*((BB.Z(i)-expdat.Z(i))/expdat.Z(i)^2)*dZdp;
        dErrsdp(3,:) = dErrsdp(3,:) + 2*((BB.D(i)-expdat.D(i))/expdat.D(i)^2)*dDdp;
    end
    
    ErrsWZD = ErrsWZD/length(BB.Q);
    dErrsdp = dErrsdp/length(BB.Q);
end