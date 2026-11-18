from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="feefdff6-4384-54b2-8f89-aa889f512b47",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name",
    display_name="Kingambit",
    searchable_by=["Kingambit", "Stage 2", "Kingambit"],
    subtypes=["Stage 2"],
    collector_number=187,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    family_id=624,
    abilities=[
        Ability(
            title="Leadership",
            game_text="Your Basic Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Hack At",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)