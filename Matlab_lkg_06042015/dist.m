function [ dx,dy,dz ] = dist( ax,ay,az,t )
%UNTITLED3 Summary of this function goes here
%   calculate the distance in x y z directions based on accelerations and
%   time.

dx = .5*ax*t^2;
dy = .5*ay*t^2;
dz = .5*az*t^2;

end

