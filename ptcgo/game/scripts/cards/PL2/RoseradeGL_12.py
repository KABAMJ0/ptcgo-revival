from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9404b9f9-8f0f-59bc-8d0a-176883dc7a10",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoseradeGL.Name",
    display_name="Roserade GL",
    searchable_by=["Roserade GL", "Basic", "SP", "RoseradeGL"],
    subtypes=["Basic", "SP"],
    collector_number=12,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=407,
    abilities=[
        Attack(
            title="Poison Bind",
            game_text="The Defending Pok\u00e9mon is now Poisoned and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Long Whip",
            game_text="If the Defending Pok\u00e9mon is affected by any Special Conditions, you may do 30 damage to any 1 Benched Pok\u00e9mon instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)