/* =========================================================
   QUIZ DE AUTOAVALIAÇÃO — FORMAÇÃO COMERCIAL HI
   Corrige na hora, sem servidor. Marcação no HTML:

   <form class="quiz">
     <fieldset class="quiz-q" data-certa="b">
       <legend>1. Pergunta</legend>
       <label><input type="radio" name="q1" value="a"> ...</label>
       <label><input type="radio" name="q1" value="b"> ...</label>
       <p class="quiz-explica" hidden>Por que a "b" é a certa.</p>
     </fieldset>
     ...
     <div class="quiz-acoes">
       <button type="submit" class="btn">Corrigir</button>
       <button type="button" class="btn btn-secondary quiz-refazer" hidden>Refazer</button>
     </div>
     <p class="quiz-resultado" aria-live="polite"></p>
   </form>

   O resultado não é salvo: o quiz é para o colaborador
   conferir o próprio entendimento antes de marcar a etapa
   como concluída. A avaliação formal é o estudo de caso
   com o instrutor.
========================================================= */

(function () {

    var APROVACAO = 0.8;

    /* Etiqueta escrita ao lado da alternativa: a cor sozinha
       deixava dúvida sobre qual era a certa e qual a marcada. */
    function etiquetar(label, classe, texto) {
        var tag = document.createElement("span");
        tag.className = "quiz-tag " + classe;
        tag.textContent = texto;
        label.appendChild(tag);
    }

    function corrigir(form) {
        var questoes = form.querySelectorAll(".quiz-q");
        var acertos = 0;

        Array.prototype.forEach.call(questoes, function (q) {
            var certa = q.getAttribute("data-certa");
            var marcada = q.querySelector("input:checked");

            q.classList.remove("certa", "errada", "sem-resposta");
            Array.prototype.forEach.call(q.querySelectorAll("label"), function (l) {
                var input = l.querySelector("input");
                var eCerta = input.value === certa;
                var erro = input.checked && !eCerta;
                l.classList.toggle("gabarito", eCerta);
                l.classList.toggle("marcada-errada", erro);
                if (eCerta) etiquetar(l, "quiz-tag-certa", input.checked ? "✓ Sua resposta está certa" : "✓ Resposta certa");
                if (erro) etiquetar(l, "quiz-tag-errada", "✗ Sua resposta");
                input.disabled = true;
            });

            if (!marcada) {
                q.classList.add("sem-resposta");
            } else if (marcada.value === certa) {
                q.classList.add("certa");
                acertos++;
            } else {
                q.classList.add("errada");
            }

            var explica = q.querySelector(".quiz-explica");
            if (explica) explica.hidden = false;
        });

        var total = questoes.length;
        var pct = total ? acertos / total : 0;
        var resultado = form.querySelector(".quiz-resultado");
        resultado.classList.toggle("aprovado", pct >= APROVACAO);
        resultado.classList.toggle("revisar", pct < APROVACAO);
        resultado.textContent = "Você acertou " + acertos + " de " + total +
            " (" + Math.round(pct * 100) + "%). " +
            (pct >= APROVACAO
                ? "Muito bem: pode marcar a etapa como concluída."
                : "Leia as explicações, revise os trechos da etapa e refaça antes de concluir.");

        form.querySelector('button[type="submit"]').hidden = true;
        form.querySelector(".quiz-refazer").hidden = false;
        resultado.scrollIntoView({ behavior: "smooth", block: "center" });
    }

    function refazer(form) {
        form.reset();
        Array.prototype.forEach.call(form.querySelectorAll(".quiz-q"), function (q) {
            q.classList.remove("certa", "errada", "sem-resposta");
            Array.prototype.forEach.call(q.querySelectorAll("label"), function (l) {
                l.classList.remove("gabarito", "marcada-errada");
                Array.prototype.forEach.call(l.querySelectorAll(".quiz-tag"), function (t) { t.remove(); });
                l.querySelector("input").disabled = false;
            });
            var explica = q.querySelector(".quiz-explica");
            if (explica) explica.hidden = true;
        });

        var resultado = form.querySelector(".quiz-resultado");
        resultado.textContent = "";
        resultado.classList.remove("aprovado", "revisar");
        form.querySelector('button[type="submit"]').hidden = false;
        form.querySelector(".quiz-refazer").hidden = true;
        form.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    Array.prototype.forEach.call(document.querySelectorAll("form.quiz"), function (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            corrigir(form);
        });
        form.querySelector(".quiz-refazer").addEventListener("click", function () {
            refazer(form);
        });
    });

})();
