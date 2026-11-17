from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="451733b2-2a19-5e63-aa3b-18916239a232",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape", "Stage 2", "Annihilape"],
    subtypes=["Stage 2"],
    collector_number=92,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Ability(
            title="Lose Cool",
            game_text="If this Pok\u00e9mon has 2 or more damage counters on it, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Impact Blow",
            game_text="During your next turn, this Pok\u00e9mon can't use Impact Blow.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)