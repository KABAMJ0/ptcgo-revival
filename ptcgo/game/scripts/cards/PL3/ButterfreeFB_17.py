from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a09df1a-8daf-50d2-948c-417d17064e3e",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ButterfreeFB.Name",
    display_name="Butterfree FB",
    searchable_by=["Butterfree FB", "Basic", "SP", "ButterfreeFB"],
    subtypes=["Basic", "SP"],
    collector_number=17,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=12,
    abilities=[
        Ability(
            title="Compound Eyes",
            game_text="If your opponent's Active Pok\u00e9mon has any Pok\u00e9-Bodies, each of Butterfree FB's attacks does 30 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Select Powder",
            game_text="Choose either Burned or Poisoned. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)