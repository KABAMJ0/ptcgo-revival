from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ef822dc0-2316-5e1e-910d-b182bfb55b19",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Torrential Heart",
            game_text="Once during your turn, you may put 5 damage counters on this Pok\u00e9mon. If you do, during this turn, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Giant Wave",
            game_text="During your next turn, this Pok\u00e9mon can't use Giant Wave.",
            cost={PokemonTypes.WATER: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)