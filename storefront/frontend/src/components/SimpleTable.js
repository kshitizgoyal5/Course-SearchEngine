import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

const row = (x, i, header) =>
  <TableRow key={`tr-${i}`}>
    {header.map((y, k) =>{
            if(header[k].ref){
                return(<TableCell key={`trc-${k}`}>
                    <a href={x.url}>{x[y.prop]}</a>
                    </TableCell>)
            }
            else{
                return(<TableCell key={`trc-${k}`}>
                    {x[y.prop]}
                    </TableCell>)
            }
        }
    )}
  </TableRow>;

export default ({ data, header }) =>{
    if(data.length > 0){
        return (<TableContainer component={Paper} style={{ maxHeight: 700}}>
            <Table stickyHeader sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
                <TableRow>
                {header.map((x, i) =>
                <TableCell key={`thc-${i}`}>
                    {x.name}
                </TableCell>
                )}
                </TableRow>
            </TableHead>
            <TableBody>
                {data.map((x, i) => row(x, i, header))} 
            </TableBody>
            </Table>
        </TableContainer>);
    }
    else{
        return <p>Found Nothing</p>;
    }
}