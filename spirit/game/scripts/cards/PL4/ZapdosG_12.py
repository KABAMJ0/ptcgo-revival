from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="203cec49-8c61-5812-b1cd-398098d007f6",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZapdosG.Name",
    display_name="Zapdos G",
    searchable_by=["Zapdos G", "Basic", "SP", "ZapdosG"],
    subtypes=["Basic", "SP"],
    collector_number=12,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Flip a coin. If heads, search your discard pile for an Energy card and attach it to Zapdos G.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may discard all Lightning attached to Zapdos G. If you do, this attack's base damage is 80 instead of 40.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)