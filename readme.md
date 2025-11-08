# Component
 - saif_parser
    parser .saif file to python data struct
    
    - how to use
    ```
    import saif_parser as saifp
    output = saifp.parse(data_str)
    ```
    - output struct
        output : dict -> key : header , cells
        cells : dict -> key : cell_name
        cell : dict -> key : cells, net_list
        net_list : dict -> key : net_name
        net : dict -> key : name, t0, t1, tx, tc, ig
 - verilog_parser
    parser .v files to python Design(Modules) data struct 

 - Mydesigner 
    FGATE_OPT DESIGNER
    - Read / parse verilog (only netlist) file
    - change netlist Module design 
    - others, check design status, like net/inst/port/...