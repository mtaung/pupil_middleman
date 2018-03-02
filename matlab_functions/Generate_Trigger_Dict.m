%==========================================================================
% Purpose: Generate a list of triggers for triggerDict and save in a ".py"
% file.  Support function for sample_mm.py.  This is useful if you are
% sending a large variety of trigger/event codes (e.g. 1:255, like in this
% example)
% Author: Tom Bullock, UCSB Attention Lab
% Date: 03.01.18
%==========================================================================

% set number of triggers
nTriggers=255;

fileID = fopen('/Users/Xus/Desktop/BOSS_2017/commonFunctions/triggerDictList.py','w'); % open file, writable

% define triggers
for i=0:nTriggers
    fprintf(fileID,sprintf('def trig%d():\n',i))
    fprintf(fileID,sprintf('    pupilLink.send_trigger(''Event%d'', timestamp=time_fn())\n',i))
end

% spaces
fprintf(fileID,'\n\n')

% create dict list
fprintf(fileID,'triggerDict = {\n')
for i=0:nTriggers
    if i~=nTriggers
        fprintf(fileID,sprintf('    b''%d'': trig%d,\n',i,i))
    else
        fprintf(fileID,sprintf('    b''%d'': trig%d\n',i,i))
    end
end
fprintf(fileID,'    }')    

% close file
fclose(fileID);