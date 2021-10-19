class contaBancaria {
    constructor(nome, numero, agencia, tipo){
        this.nome = nome;
        this.numero = numero;
        this.agencia = agencia;
        this.tipo = tipo;
        this._saldo = 0;
    }

    get saldo(){
        return this._saldo;
    }
    set saldo(valor) {
        this._saldo = valor;
    }

    sacar(valor){
        if (valor > this._saldo){
            return "Saldo Insuficiente!";
        }
        this._saldo = this._saldo - valor;
        return this._saldo;
    }

    depositar(valor) {
        this._saldo = this._saldo + valor;
        return this._saldo;
    }
}


