from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype, is_pokemon_ex
from ptcgo.game.session.passives import (
    Passive, carrier_pokemon, effective_pokemon_types,
)


class ExcitedPowerPassive(Passive):
    """While a Darkness Mega Evolution Pokemon ex of yours is in play,
    this Pokemon's attacks do 120 more to your opponent's Active."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or calc.attacker is not holder:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if not any(is_pokemon_ex(p) and has_pokemon_subtype(p, "MEGA")
                   and PokemonTypes.DARKNESS.value
                   in effective_pokemon_types(calc.board, p)
                   for p in calc.board.pokemon_in_play(holder.owning_player_id)):
            return
        calc.amount += 120


card = PokemonCardDef(
    guid="05ebab0f-cc26-5de1-95fd-0d8879ae0958",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic", "Seviper"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=336,
    abilities=[
        Ability(
            title="Excited Power",
            game_text="If you have any Darkness Mega Evolution Pok\u00e9mon ex in play, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=ExcitedPowerPassive(),
        ),
        Attack(
            title="Pitch-Black Fangs",
            cost={PokemonTypes.DARKNESS: 3},
            damage=120,
        ),
    ],
)