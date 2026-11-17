from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="25f6741e-87da-592b-a159-78e90a916507",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=436,
    abilities=[
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)