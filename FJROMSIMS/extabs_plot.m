clc
clear all
addpath('../ROUTINES/')

set(0,'defaultAxesTickLabelInterpreter', 'default');
set(0,'defaultTextInterpreter','latex'); 
set(0, 'DefaultLegendInterpreter', 'latex'); 
set(0,'defaultAxesFontSize',13)

%% Load Reference Data
exx = load('../FULLJOINT_REF/DATS/RUN2.mat', 'QS', 'WS', 'ZS', 'DS','ZSM','BBS');

%% Plot Backbones
figure(1)
clf()
colos = DISTINGUISHABLE_COLORS(7);  colos = colos(end-2:end,:);
aa = gobjects(4,1);

ax1=subplot(2,1,1);
set(ax1, 'DataAspectRatioMode', 'manual')
aa(1) = semilogx(exx.QS, exx.WS/2/pi, 'k-', 'LineWidth', 2); hold on
legend(aa(1), sprintf('Reference (%d DoFs)',size(exx.BBS{1}.U,1)-1))

ax2=subplot(2,1,2);
loglog(exx.QS, exx.ZSM, 'k-', 'LineWidth', 2); hold on

symbs = {'s-', 'd-', 'p-'};
k=1;
for p=[52 124 300]
    load(sprintf('./DATS/RUN_%d.mat',p), 'QS', 'WS', 'ZSM', 'BBS');
    subplot(2,1,1);
    aa(k+1) = semilogx(QS, WS/2/pi, symbs{k}, 'Color', colos(k,:), 'MarkerFaceColor', colos(k,:));
    legend(aa(k+1), sprintf('%d Element ROM (%d DoFs)',p,size(BBS{1}.U,1)-1))
    
    subplot(2,1,2);
    loglog(QS, ZSM, symbs{k}, 'Color', colos(k,:), 'MarkerFaceColor', colos(k,:))
    
    k = k+1;
end
subplot(2,1,1)
xticklabels([])
legend(aa(1:end), 'Location', 'southwest')
ylabel('Natural Frequency (Hz)')
xlim([1e-6 1e-1])

subplot(2,1,2)
xlabel('Modal Amplitude')
ylabel('Damping factor')
xlim([1e-6 1e-1])
ylim([9e-6 1e0])

ax1.Position = [0.13 0.5 0.8 0.45]
ax2.Position = [0.13 0.12 0.8 0.33]
print('./FIGURES/P11580_S-6.00_ELDRYFRICT_BB_FJROM.eps', '-depsc')