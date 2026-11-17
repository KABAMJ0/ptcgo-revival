from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a737829b-9ea8-5347-8e04-6948ad889fdb",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VespiquenE4.Name",
    display_name="Vespiquen E4",
    searchable_by=["Vespiquen E4", "Basic", "SP", "VespiquenE4"],
    subtypes=["Basic", "SP"],
    collector_number=35,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=416,
    abilities=[
        Ability(
            title="Royal Gain",
            game_text="When you attach a Grass Energy card from your hand to Vespiquen E4, remove 1 damage counter from Vespiquen E4.",
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Needle",
            game_text="Flip a coin for each Grass Energy attached to Vespiquen E4. This attack does 30 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)