from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3aa5b624-33b8-5d93-b423-30c96f764fa7",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaticateG.Name",
    display_name="Raticate G",
    searchable_by=["Raticate G", "Basic", "SP", "RaticateG"],
    subtypes=["Basic", "SP"],
    collector_number=78,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=20,
    abilities=[
        Attack(
            title="Find",
            game_text="Search your discard pile for a Trainer card or a Supporter card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Biting Fang",
            game_text="Flip a coin, if heads this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)