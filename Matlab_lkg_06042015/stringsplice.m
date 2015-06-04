function [ ax,ay,az ] = stringsplice( string )
%UNTITLED Summary of this function goes here
%   expects two commas in a string and separates the string into three
%   strings
comma = 0;
for i=1:numel(string)
    if (string(i) == ',')
        comma = comma+1;
    else
        if (comma==0)
            endx = i;
            beginy = i+2;
        elseif(comma==1)
            endy = i;
            beginz = i+2;
        else
            endz = i;
        end
    end
end

ax=string(1:endx);
ay=string(beginy:endy);
az=string(beginz:endz);
end

