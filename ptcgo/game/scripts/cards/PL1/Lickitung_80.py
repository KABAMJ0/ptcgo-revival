from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54571bb1-bca9-5c4f-8e98-06c94e2e1cf8",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Stretch Tongue",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Knock Off",
            game_text="Choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=unimplemented,
        ),
    ],
)