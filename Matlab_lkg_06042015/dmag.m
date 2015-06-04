function [ mag ] = dmag( x1,x2,y1,y2,z1,z2 )
%dmag Summary of this function goes here
%   finds the magnitude of the distance between two points

mag = sqrt((x1-x2)^2+(y1-y2)^2+(z1-z2)^2);



end

