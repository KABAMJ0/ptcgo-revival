from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f5666dd-bd7c-5cca-b5b8-c7889fad8c88",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    display_name="Combusken",
    searchable_by=["Combusken", "Stage 1", "Combusken"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Lava Burn",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Claws",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 10 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)