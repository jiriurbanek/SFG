{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  name = "EEOver";
  buildInputs = with pkgs; [
    boost
    gnumake
    gsl
    gcc
    pkg-config
  ];
  
  shellHook = '''';
  # Some bash command and export some env vars.
}
