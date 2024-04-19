# Uwagi do lab Energy Efficient parallel programming

## Przydatne polecenia

- docker run -it --privileged -p 8888:8888 eumaster4hpccyfronet/energy-aware-computing-mooc

## Uwagi instrukcja

- instrukcja instalacji bez NVidia powinna być wyżej
- zawrzeć współistniejące instrukcje uruchomienia - bez NVidia i z NVidia - aktualnie instrukcja jest zbyt nisko
    - docker run -it --rm --privileged -p 8888:8888 eumaster4hpccyfronet/energy-aware-computing-mooc
    - docker run -it --rm --privileged --runtime nvidia -p 8888:8888 eumaster4hpccyfronet/energy-aware-computing-mooc
- możliwość odpalenia w VS Code a nie tylko w przeglądarce
- Instrukcja odpalenia w VS Code
    - pobrać Jupyter extension dla VS Code
    - odpalić dockera 
        ```
        docker run -it --privileged -p 8888:8888 -v `pwd`:/jupyter/ eumaster4hpccyfronet/energy-aware-computing-mooc
        ```
    - wybrać jako kernel istniejący server jupytera
