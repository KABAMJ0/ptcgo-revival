from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c985a9ad-7317-52cf-a6fc-46de3c4d3774",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Wonder Guard",
            game_text="Prevent all effects of attacks, including damage, done to Shedinja by your opponent's Evolved Pok\u00e9mon and Pok\u00e9mon-ex.",
            effect=unimplemented,
        ),
        Attack(
            title="Damage Curse",
            game_text="Put 1 damage counter, plus 1 more damage counter for each damage counter on Shedinja, on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)