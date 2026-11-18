from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b02f8baf-7ab7-527e-a5c9-a7b40e6ffcff",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomG.Name",
    display_name="Houndoom G",
    searchable_by=["Houndoom G", "Basic", "SP", "HoundoomG"],
    subtypes=["Basic", "SP"],
    collector_number=50,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=229,
    abilities=[
        Attack(
            title="Black Cry",
            game_text="The Defending Pok\u00e9mon can't retreat or use any Pok\u00e9-Powers during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Dark Slash",
            game_text="You may discard a Darkness Energy attached to Houndoom G. If you do, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)